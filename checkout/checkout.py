from decimal import Decimal
from shop.models import Product

class Checkout():

    def __init__(self, request):
        self.session = request.session
        
        # returning user obtain existing session
        checkout = self.session.get('session-key')

        # new user generate a new session
        if 'session-key' not in request.session:
            checkout = self.session['session-key'] = {}

        self.checkout = checkout


    def add(self, product, product_qty): 

        product_id = str(product.id)  

        if product_id in self.checkout:
            self.checkout[product_id]['qty'] = product_qty

        else:

            self.checkout[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True 


    def delete(self, product):

        product_id = str(product)  

        if product_id in self.checkout:

            del self.checkout[product_id] 
             
        self.session.modified = True  


    def update(self, product, qty):

        product_id = str(product)
        product_quantity = qty

        if product_id in self.checkout:

            self.checkout[product_id]['qty'] = product_quantity

        self.session.modified = True         


    def __len__(self):

        return sum(item['qty'] for item in self.checkout.values()) 


    def __iter__(self): 

        all_product_ids = self.checkout.keys()

        products =  Product.objects.filter(id__in=all_product_ids)

        import copy

        checkout = copy.deepcopy(self.checkout)

        for product in products:
            checkout[str(product.id)]['product'] = product

        for item in checkout.values():
            item['price'] = Decimal(item['price']) 

            item['total'] = item['price'] * item['qty']

            yield item     


    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.checkout.values())         
       