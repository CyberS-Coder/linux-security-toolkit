import os
import hashlib
import json

def calculate_hash_value(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byteblock in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byteblock)
        return sha256_hash.hexdigest()
    except (FileNotFoundError, PermissionError, OSError):
        return None

def get_baseline_filename(target_path):
    # Convert the path into a unique, safe filename for disk storage
    abs_path = os.path.abspath(target_path)
    safe_name = abs_path.strip(os.sep).replace(os.sep, "_").replace(":", "")
    return f"baseline_{safe_name}.json"

def get_target_files(target_path):
    target_files = []
    absolute_path = os.path.abspath(target_path)

    if os.path.isfile(absolute_path):
        target_files.append(absolute_path)
    elif os.path.isdir(absolute_path):
        for root, dirs, files in os.walk(absolute_path):
            for file in files:
                target_files.append(os.path.join(root, file))
    else:
        print(f"Error: Path does not exist -> {target_path}")

    return target_files

def create_file_baseline(file_list):
    print("Generating file integrity baseline...")
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
        print(f"Error saving baseline: {e}")

def load_baseline_from_disk(filename):
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

def verify_file_integrity(original_baseline, new_baseline):
    print("Verifying file integrity...")
    for file_path, original_hash in original_baseline.items():
        if file_path not in new_baseline:
            print(f"WARNING! - FILE MISSING: {file_path}")
            continue

        current_hash = new_baseline[file_path]
        if current_hash != original_hash:
            print(f"WARNING! - FILE MODIFIED: {file_path}")
        else:
            print(f"OK - Unchanged: {file_path}")

def main():
    user_input = input("Enter file or directory path to monitor: ").strip()
    target_list = get_target_files(user_input)

    if not target_list:
        print("No valid files found to monitor. Exiting.")
        return

    # Dynamically generate the baseline filename based on the user's target path
    baseline_file = get_baseline_filename(user_input)

    baseline = load_baseline_from_disk(baseline_file)

    if baseline is None:
        print(f"No existing baseline found for this path. Creating initial baseline...")
        baseline = create_file_baseline(target_list)
        if baseline:
            save_baseline_to_disk(baseline, baseline_file)
    else:
        current_check = create_file_baseline(target_list)
        verify_file_integrity(baseline, current_check)

if __name__ == "__main__":
    main()
