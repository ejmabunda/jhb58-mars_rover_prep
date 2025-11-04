import unittest
from smart_fridge import SmartFridge

class TestSmartFridgeCommands(unittest.TestCase):

    def setUp(self):
        self.fridge = SmartFridge()

    # Add command tests
    def test_add_new_item(self):
        self.fridge.add_item('milk', 2)
        self.assertEqual(self.fridge.inventory.get('milk'), 2)

    def test_add_existing_item_increments_quantity(self):
        self.fridge.add_item('milk', 2)
        self.fridge.add_item('milk', 3)
        self.assertEqual(self.fridge.inventory.get('milk'), 5)

    def test_add_item_case_insensitive(self):
        self.fridge.add_item('Milk', 2)
        self.fridge.add_item('milk', 3)
        self.assertEqual(self.fridge.inventory.get('milk'), 5)
        self.assertNotIn('Milk', self.fridge.inventory)

    def test_add_item_with_float_quantity(self):
        self.fridge.add_item('milk', 1.5)
        self.assertEqual(self.fridge.inventory.get('milk'), 1.5)

    # Use command tests
    def test_use_existing_item(self):
        self.fridge.add_item('eggs', 10)
        self.fridge.use_item('eggs', 4)
        self.assertEqual(self.fridge.inventory.get('eggs'), 6)

    def test_use_item_insufficient_quantity_removes_all(self):
        self.fridge.add_item('eggs', 3)
        qty_used = self.fridge.use_item('eggs', 5)
        self.assertEqual(qty_used, 3)
        self.assertNotIn('eggs', self.fridge.inventory)

    def test_use_nonexistent_item(self):
        qty_used = self.fridge.use_item('bread', 1)
        self.assertEqual(qty_used, 0)
        self.assertNotIn('bread', self.fridge.inventory)

    def test_use_item_case_insensitive(self):
        self.fridge.add_item('Cheese', 5)
        self.fridge.use_item('cheese', 3)
        self.assertEqual(self.fridge.inventory.get('cheese'), 2)

    # Report command tests
    def test_report_empty_fridge(self):
        report = self.fridge.report()
        self.assertEqual(report, "The fridge is empty.")

    def test_report_with_items(self):
        self.fridge.add_item('milk', 2)
        self.fridge.add_item('eggs', 3)
        report = self.fridge.report()
        self.assertIn("milk: 2", report)
        self.assertIn("eggs: 3", report)

    # Clear command tests
    def test_clear_fridge(self):
        self.fridge.add_item('milk', 2)
        self.fridge.clear()
        self.assertEqual(self.fridge.inventory, {})

if __name__ == "__main__":
    unittest.main()
