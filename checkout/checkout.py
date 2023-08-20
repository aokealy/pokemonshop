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