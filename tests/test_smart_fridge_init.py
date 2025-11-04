import unittest
from smart_fridge import SmartFridge

class TestSmartFridgeInit(unittest.TestCase):

    def test_fridge_starts_empty(self):
        fridge = SmartFridge()
        self.assertEqual(fridge.inventory, {}, "Fridge should start with an empty inventory.")

    def test_fridge_init_with_items(self):
        initial_items = {"milk": 2, "eggs": 12}
        fridge = SmartFridge(initial_items)
        self.assertEqual(fridge.inventory, initial_items, "Fridge should initialize with provided items.")

    def test_fridge_init_creates_copy(self):
        items = {"milk": 1}
        fridge = SmartFridge(items)
        items["milk"] = 99  # mutate the original dict
        self.assertEqual(fridge.inventory["milk"], 1, "Fridge should store a copy of the initial dict.")

if __name__ == "__main__":
    unittest.main()
