from unittest import TestCase

from index_mas import index


class TestIndex(TestCase):

    def test_index_case(self):
        self.assertEqual(index(65, 192), 17.63)
        self.assertEqual(index(40, 192), 10.85)
        self.assertEqual(index(86, 192), 23.33)
        self.assertEqual(index(95, 192), 25.77)
        self.assertEqual(index(120, 192), 32.55)
        self.assertEqual(index(130, 192), 35.26)
        self.assertEqual(index(150, 192), 40.69)

    def test_values(self):
        self.assertRaises(ValueError, index, 0, -1)
        self.assertRaises(ValueError, index, -2, 0)

    def test_types(self):
        self.assertRaises(TypeError, index, 5+2, 'd')
        self.assertRaises(TypeError, index, 'fer', 'd')
        self.assertRaises(TypeError, index, [16], [12, 25])





