import unittest
import os
import tempfile
from src.file_integrity import calculate_hash

class TestFileIntegrity(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(b"Hello Security World")
        self.test_file.close()

    def tearDown(self):
        # Clean up temporary file
        os.remove(self.test_file.name)

    def test_hash_consistency(self):
        # Verify that hashing the same file twice produces identical output
        hash1 = calculate_hash(self.test_file.name)
        hash2 = calculate_hash(self.test_file.name)
        self.assertEqual(hash1, hash2)

    def test_hash_modification_detection(self):
        # Verify that modifying the file changes the hash
        initial_hash = calculate_hash(self.test_file.name)

        with open(self.test_file.name, "ab") as f:
            f.write(b" extra bytes")

        modified_hash = calculate_hash(self.test_file.name)
        self.assertNotEqual(initial_hash, modified_hash)

if __name__ == "__main__":
    unittest.main()
