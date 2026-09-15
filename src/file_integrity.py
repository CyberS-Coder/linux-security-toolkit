#!/usr/bin/env python3
import os
import hashlib
import json
import argparse

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byteblock in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byteblock)
        return sha256_hash.hexdigest()
    except (FileNotFoundError, PermissionError, OSError):
        return None

def get_target_files(target_path):
    target_files = []
    abs_path = os.path.abspath(target_path)
    if os.path.isfile(abs_path):
        target_files.append(abs_path)
    elif os.path.isdir(abs_path):
        for root, _, files in os.walk(abs_path):
            for file in files:
                target_files.append(os.path.join(root, file))
    return target_files

def scan_directory(target_path):
    files = get_target_files(target_path)
    baseline = {}
    for f in files:
        h = calculate_hash(f)
        if h:
            baseline[f] = h
    return baseline

def main():
    parser = argparse.ArgumentParser(description="Host File Integrity Monitor (FIM)")
    parser.add_argument("-t", "--target", required=True, help="Path to file or directory to monitor")
    parser.add_argument("-b", "--baseline", default="fim_baseline.json", help="Path to baseline JSON file")
    parser.add_argument("--init", action="store_true", help="Generate and save a new baseline")
    parser.add_argument("--check", action="store_true", help="Check target path against existing baseline")

    args = parser.parse_args()

    if args.init:
        print(f"Generating new baseline for target: {args.target}")
        baseline = scan_directory(args.target)
        with open(args.baseline, "w") as f:
            json.dump(baseline, f, indent=4)
        print(f"Baseline saved to {args.baseline}")

    elif args.check:
        if not os.path.exists(args.baseline):
            print(f"Error: Baseline file '{args.baseline}' not found. Run with --init first.")
            return

        with open(args.baseline, "r") as f:
            saved_baseline = json.load(f)

        print(f"Verifying integrity of: {args.target}")
        current_state = scan_directory(args.target)

        # 1. Check for MODIFIED and MISSING files
        for file_path, original_hash in saved_baseline.items():
            if file_path not in current_state:
                print(f"ALERT!: MISSING FILE -> {file_path}")
            elif current_state[file_path] != original_hash:
                print(f"ALERT!: MODIFIED FILE -> {file_path}")
            else:
                print(f"OK: {file_path}")

        # 2. Check for ADDED (untracked) files
        for file_path in current_state:
            if file_path not in saved_baseline:
                print(f"ALERT!: NEW UNTRACKED FILE ADDED -> {file_path}")

if __name__ == "__main__":
    main()
