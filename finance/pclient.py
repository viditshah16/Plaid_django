from plaid import Client
from Plaid.settings import PLAID_CLIENT_ID, PLAID_SECRET
# from .views import PublicTokenCreate

class Pclient:
    __instance = None

    @staticmethod 
    def getInstance():
        if Pclient.__instance == None:
            Pclient()
        return Pclient.__instance

    def __init__(self):
        if Pclient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Pclient.__instance = Client(
                # public_key=PublicTokenCreate(),
                client_id=PLAID_CLIENT_ID,
                secret=PLAID_SECRET,
                environment='sandbox'
            )