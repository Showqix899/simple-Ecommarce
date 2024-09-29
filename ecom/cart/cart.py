
class Cart():

    def __init__(self,request):
        self.session=request.session

        #if session key exist get the session key
        cart=self.session.get('session_key')

        #if the user is new ,no session key! create one
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}


        #make sure session works on every page of the website

        self.cart=cart