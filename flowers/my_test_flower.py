import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.flower1 = Flower("blue", 3, 5.5)
        self.flower2 = Flower("yellow", 4, 4.0)
        self.set1 = FlowerSet([self.flower1, self.flower2])

        self.tulip = Tulip("pink", 5, 15.0)
        self.rose = Rose("red", 15, 26.5)
        self.chamomile = Chamomile("white", 7, 11.5)
        self.set2 = FlowerSet([self.tulip, self.rose, self.chamomile])

        self.bucket = Bucket([self.set1, self.set2])

    def test_init(self):
        self.assertEqual(self.flower1.colour, "blue", "The 'colour' attribute doesn't work.")
        self.assertEqual(self.tulip.colour, "pink", "The 'colour' attribute doesn't work.")
        self.assertEqual(self.rose.colour, "red", "The 'colour' attribute doesn't work.")
        self.assertEqual(self.chamomile.colour, "white", "The 'colour' attribute doesn't work.")
    
        self.assertEqual(self.flower1.petals, 3, "The 'petals' attribute doesn't work.")
        self.assertEqual(self.tulip.petals, 5, "The 'petals' attribute doesn't work.")
        self.assertEqual(self.rose.petals, 15, "The 'petals' attribute doesn't work.")
        self.assertEqual(self.chamomile.petals, 7, "The 'petals' attribute doesn't work.")

        self.assertEqual(self.flower1.price, 5.5, "The 'price' attribute doesn't work.")
        self.assertEqual(self.tulip.price, 15.0, "The 'price' attribute doesn't work.")
        self.assertEqual(self.rose.price, 26.5, "The 'price' attribute doesn't work.")
        self.assertEqual(self.chamomile.price, 11.5, "The 'price' attribute doesn't work.")

        self.assertIs(self.set1.flowers[0], self.flower1, "The 'flowers' attribute doesn't work.")
        self.assertIs(self.set2.flowers[2], self.chamomile, "The 'flowers' attribute doesn't work.")

        self.assertEqual(self.set1.amount, 2, "The 'amount' attribute doesn't work.")
        self.assertEqual(self.set2.amount, 3, "The 'amount' attribute doesn't work.")

    def test_methods(self):
        self.assertEqual(self.set1.set_price(), 9.5, "The 'set_price' method of FlowerSet doesn't work.")
        self.assertEqual(self.set2.set_price(), 53, "The 'set_price' method of FlowerSet doesn't work.")

        self.assertEqual(self.bucket.bucket_price(), 62.5, "The 'bucket_price' method of Bucket doesn't work.")


if __name__ == '__main__':
    unittest.main()
