class Promo:

    MAX_USAGE: int = 2

    def __init__(self, amount: int, bonus: int, usage: int) -> None:

        if usage <= 0 or usage > self.MAX_USAGE:
            raise ValueError('Usage can be either 1 or 2')

        self.usage = usage
        self.amount = amount
        self.bonus = bonus
        self.total_amount = self.amount * self.usage
