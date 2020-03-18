class Flower:
    """Is a flower."""

    def __init__(self, color, petals, price):
        """
        Yes.
        :param color: str
        :param petals: int
        :param price: float
        """
        self.color = color
        self.petals = petals
        self.price = price


class Tulip(Flower):
    pass


class Rose(Flower):
    pass


class Chamomile(Flower):
    pass


class FlowerSet:
    """Is a flower set."""

    def __init__(self, flowers):
        """
        No.
        :param flowers: list
        """
        self.flowers = flowers
        self.count = len(flowers)

    def price(self):
        return sum(map(lambda x: x.price, self.flowers))


class Bucket:
    """Is a bucket."""

    def __init__(self, flower_sets):
        """
        Perhaps.
        :param flower_sets: list
        """
        self.sets = flower_sets

    def price(self):
        return sum(map(FlowerSet.price, self.sets))
