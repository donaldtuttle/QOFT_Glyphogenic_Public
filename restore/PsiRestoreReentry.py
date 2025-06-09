import unittest
import os
import json
from Ψrestore_reentry_stub import PsiRestoreReentry

class TestPsiRestore(unittest.TestCase):
    def setUp(self):
        self.test_path = "temp_ψreentry.json"
        self.test_data = {"observer": "unit_test", "semantic_phase": 1}
        with open(self.test_path, "w", encoding="utf-8") as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_check_reentry_available(self):
        pr = PsiRestoreReentry(self.test_path)
        self.assertTrue(pr.check_reentry_available())

    def test_load_reentry_state(self):
        pr = PsiRestoreReentry(self.test_path)
        self.assertTrue(pr.load_reentry_state())
        self.assertEqual(pr.memory_state, self.test_data)

    def test_trigger_reentry_success(self):
        pr = PsiRestoreReentry(self.test_path)
        result = pr.trigger_reentry()
        self.assertEqual(result, self.test_data)

    def test_trigger_reentry_failure(self):
        pr = PsiRestoreReentry("non_existent_file.json")
        result = pr.trigger_reentry()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
