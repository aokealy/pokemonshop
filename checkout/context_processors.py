from .checkout import Checkout


def checkout(request):
    return {'checkout': Checkout(request)}
    