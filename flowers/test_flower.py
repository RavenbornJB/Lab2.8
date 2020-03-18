import unittest
from flowers.flower import *


class Test(unittest.TestCase):
    def setUp(self):
        self.flower1 = Flower("red", 5, 10.0)

        self.tulip1 = Tulip("yellow", 10, 5.0)
        self.tulip2 = Tulip("green", 10, 5.0)
        self.tulip3 = Tulip("blue", 10, 5.0)
        self.flowerset1 = FlowerSet([self.tulip1, self.tulip2, self.tulip3])

        self.rose1 = Rose("red", 6, 7.0)
        self.rose2 = Rose("red", 4, 7.0)
        self.flowerset2 = FlowerSet([self.rose1, self.rose2])

        self.chamomile1 = Chamomile("white", 12, 3.0)
        self.chamomile2 = Chamomile("white", 14, 3.0)
        self.flowerset3 = FlowerSet([self.chamomile1, self.chamomile2])

        self.bucket = Bucket([self.flowerset1, self.flowerset2, self.flowerset3])

    def test_init(self):
        self.assertEqual(self.flower1.color, "red", "Attribute color not working properly")
        self.assertEqual(self.flower1.petals, 5, "Attribute petals not working properly")
        self.assertEqual(self.flower1.price, 10.0, "Attribute price not working properly")

        self.assertEqual(self.tulip1.color, "yellow", "Attribute color not working properly")
        self.assertEqual(self.tulip1.petals, 10, "Attribute petals not working properly")
        self.assertEqual(self.tulip1.price, 5.0, "Attribute price not working properly")

        self.assertEqual(self.rose1.color, "red", "Attribute color not working properly")
        self.assertEqual(self.rose1.petals, 6, "Attribute petals not working properly")
        self.assertEqual(self.rose1.price, 7.0, "Attribute price not working properly")

        self.assertEqual(self.chamomile1.color, "white", "Attribute color not working properly")
        self.assertEqual(self.chamomile1.petals, 12, "Attribute petals not working properly")
        self.assertEqual(self.chamomile1.price, 3.0, "Attribute price not working properly")

        self.assertEqual(self.flowerset1.count, 3, "Attribute count not working properly")
        self.assertEqual(self.flowerset2.count, 2, "Attribute count not working properly")
        self.assertEqual(self.flowerset3.count, 2, "Attribute count not working properly")

        self.assertIs(self.flowerset1.flowers[0], self.tulip1, "Attribute flowers not working properly")
        self.assertIs(self.flowerset1.flowers[1], self.tulip2, "Attribute flowers not working properly")
        self.assertIs(self.flowerset1.flowers[2], self.tulip3, "Attribute flowers not working properly")

        self.assertIs(self.flowerset2.flowers[0], self.rose1, "Attribute flowers not working properly")
        self.assertIs(self.flowerset2.flowers[1], self.rose2, "Attribute flowers not working properly")

        self.assertIs(self.flowerset3.flowers[0], self.chamomile1, "Attribute flowers not working properly")
        self.assertIs(self.flowerset3.flowers[1], self.chamomile2, "Attribute flowers not working properly")

    def test_methods(self):
        self.assertEqual(self.flowerset3.price(), 6.0, "Method price() not working properly")
        self.assertEqual(self.flowerset2.price(), 14.0, "Method price() not working properly")
        self.assertEqual(self.flowerset1.price(), 15.0, "Method price() not working properly")
        self.assertEqual(self.bucket.price(), 35.0, "Method price() not working properly")


if __name__ == '__main__':
    unittest.main()
