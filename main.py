from models.algtelecompromo import AlgTelecomPromo, Subscriptions
from models.promo import Promo


if __name__ == "__main__":
    my_subscription: Subscriptions = Subscriptions(value=1600)
    used_promo: Promo = Promo(amount=3000, bonus=1000, usage=2)
    app: AlgTelecomPromo = AlgTelecomPromo(subscription=my_subscription, promo=used_promo)

    app.explain()
