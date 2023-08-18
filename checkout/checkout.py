class Checkout():

    def __init__(self, request):
        self.session = request.session
        
        # returning user obtain existing session
        checkout = self.session.get('session-key')

        # new user generate a new session
        if 'session-key' not in request.session:
            checkout = self.session['session-key'] = {}

        self.checkout = checkout