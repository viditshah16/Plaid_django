from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from datetime import timedelta

from .models import Item, Transaction, Account
from .serializers import TransactionSerializer, AccountSerializer
from .pclient import Pclient
# from .utils import clean_accounts_data
# from .tasks import save_transactions_to_db, delete_transactions_from_db
from Plaid.settings import NGROK_ID

client = Pclient.getInstance()

def home(request):
    return HttpResponse('<h1>Finance app on Django rest framework using plaid apis</h2>')


class PublicTokenCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # institution_id = ins_109512
        institution_id = request.data['institution_id']

        res = client.Sandbox.public_token.create(
            institution_id=institution_id,
            initial_products=['transactions'],
            webhook="http://" + NGROK_ID + ".ngrok.io/webhook_transactions/"
        )
        
        public_token = res['public_token']
        print(public_token)
        
        data = {
            "public_token": public_token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class AccessTokenCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        global access_token, item_id
        public_token = request.data['public_token']

        response = client.Item.public_token.exchange(public_token)
        access_token = response['access_token']
        item_id = response['item_id']
        print(access_token, item_id)
        
        item = Item.objects.create(user=self.request.user, item_id=item_id, access_token=access_token)
        item.save()

        # save_transactions_to_db.delay(item_id, 50)

        data = {
            "access_token": access_token,
            "item_id": item_id
        }
        return Response(data, status=status.HTTP_201_CREATED)