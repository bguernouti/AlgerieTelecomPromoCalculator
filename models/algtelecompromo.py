from enum import Enum

from .promo import Promo


class Subscriptions(Enum):

    mb_10: int = 1600
    mb_15: int = 1999
    mb_20: int = 2599
    mb_50: int = 2999


class AlgTelecomPromo:

    DAYS_STEP: int = 30

    def __init__(self, subscription: Subscriptions, promo: Promo) -> None:
        self.promo = promo
        self.subscription = subscription
        self.cost_per_day = AlgTelecomPromo.__day_cost(subscription.value)
        self.amount_days = self.__days(amount=promo.amount)
        self.bonus_days = self.__days(amount=promo.bonus)
        self.promo_days = self.__promo_days()
        self.cost_with_no_bonus = self.promo_days * self.cost_per_day

    @classmethod
    def __day_cost(cls, amount: float) -> float:
        return round(amount / cls.DAYS_STEP, 2)

    def __days(self, amount: float) -> float:
        return round(amount / self.cost_per_day, 2) * self.promo.usage

    def __promo_days(self) -> float:
        return round(self.amount_days + self.bonus_days, 2)

    def explain(self) -> None:
        print(f'>> Promo used {self.promo.amount} x {self.promo.usage} for a subscription {self.subscription.name} <<')
        print(f'------------------------------------------------------------------------')
        print(f'Without a bonus days = {self.amount_days}')
        print(f'Promo days = {self.promo_days}')
        print(f'Days won = {round(self.promo_days - self.amount_days, 2)}')
        print(f'------------------------------------------------------------------------')
        print(f'Without a bonus cost ({self.promo_days} days) = {self.cost_with_no_bonus}')
        print(f'Promo Cost = {self.promo.total_amount},')
        print(f'Saved money = {round(self.cost_with_no_bonus - self.promo.total_amount, 2)}')
        print(f'------------------------------------------------------------------------')
