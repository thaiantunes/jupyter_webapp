import unittest
from food_calc import food_calc

class Test_food_calc(unittest.TestCase):
    def test_basic(self):
        guests = 1
        veggie_guests = 0
        red = 'Yes' 
        chicken = 'Yes'
        corn = 'Yes'
        expected = (1, 1, 1, 1, 250, 250)
        self.assertEqual(food_calc(guests, veggie_guests, red, chicken, corn), expected)

    def test_nochicken(self):
        guests = 1
        veggie_guests = 0
        red = 'Yes' 
        chicken = 'No'
        corn = 'Yes'
        expected = (1, 1, 1, 1, 500, 0)
        self.assertEqual(food_calc(guests, veggie_guests, red, chicken, corn), expected)

    def test_nored(self):
        guests = 1
        veggie_guests = 0
        red = 'No' 
        chicken = 'Yes'
        corn = 'Yes'
        expected = (1, 1, 1, 1, 0, 500)
        self.assertEqual(food_calc(guests, veggie_guests, red, chicken, corn), expected)

    def test_veggiesonly(self):
        guests = 0
        veggie_guests = 2
        red = 'Yes' 
        chicken = 'Yes'
        corn = 'Yes'
        expected = (3, 3, 3, 3, 0, 0)
        self.assertEqual(food_calc(guests, veggie_guests, red, chicken, corn), expected)

    def test_complex(self):
        guests = 1
        veggie_guests = 2
        red = 'Yes' 
        chicken = 'Yes'
        corn = 'No'
        expected = (4, 4, 4, 0, 250, 250)
        self.assertEqual(food_calc(guests, veggie_guests, red, chicken, corn), expected)    
unittest.main()