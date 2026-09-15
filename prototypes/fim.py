import os
import hashlib
import json

TARGET_FILES = ["./text.txt"]
BASELINE_FILE = "baseline.json"

def calculate_hash_value(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byteblock in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byteblock)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found -> {filepath}")
        return None
    except PermissionError:
        print(f"Error: Permission denied -> {filepath}")
        return None
    except OSError as e:
        print(f"Error: Could not read file {filepath}: {e}")
        return None

def create_file_baseline(file_list):
    print("Scanning files for baseline...")
    file_baseline = {}
    for filepath in file_list:
        file_hash = calculate_hash_value(filepath)
        if file_hash:
            file_baseline[filepath] = file_hash
            print(f"Hashed: {filepath}")
    return file_baseline

def save_baseline_to_disk(baseline, filename):
    try:
        with open(filename, "w") as f:
            json.dump(baseline, f, indent=4)
        print(f"Baseline successfully saved to {filename}")
    except OSError as e:
        print(f"Error saving baseline to disk: {e}")

def load_baseline_from_disk(filename):
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, "r") as f:
            print(f"Found existing baseline file: {filename}. Loading...")
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Baseline file is corrupted.")
        return None
    except OSError as e:
        print(f"Error loading baseline: {e}")
        return None

def verify_file_integrity(original_baseline, new_baseline):
    print("Verifying file integrity against saved baseline...")
    for file_path, original_hash in original_baseline.items():
        if file_path not in new_baseline:
            print(f"WARNING! - FILE MISSING OR SKIPPED: {file_path}")
            continue

        current_hash = new_baseline[file_path]
        if current_hash != original_hash:
            print(f"WARNING - FILE HAS BEEN MODIFIED: {file_path}")
        else:
            print(f"OK - File unchanged: {file_path}")

def main():
    # 1. Check if a baseline already exists on disk
    baseline = load_baseline_from_disk(BASELINE_FILE)

    if baseline is None:
        # 2. If no baseline exists, create a new one and save it to disk
        print("No existing baseline found. Creating initial baseline...")
        baseline = create_file_baseline(TARGET_FILES)
        if baseline:
            save_baseline_to_disk(baseline, BASELINE_FILE)
        else:
            print("Error: Could not generate baseline. Exiting.")
            return
    else:
        # 3. If a baseline exists, run an immediate audit check against current file states
        current_check = create_file_baseline(TARGET_FILES)
        verify_file_integrity(baseline, current_check)

if __name__ == "__main__":
    main()
