"""Plaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plaid-home'),
    
    path('get_access_token/', views.AccessTokenCreate.as_view()),
    path('get_public_token/', views.PublicTokenCreate.as_view()),
    path('get_transactions/', views.TransactionsGet.as_view()),
    path('get_transactions_from_db/', views.TransactionsGetDB.as_view()),
    path('get_account_balance/', views.AccountBalance.as_view()),
    path('get_account_balance_from_db/', views.AccountBalanceDB.as_view()),
    
    path('webhook_test/', views.WebhookTest.as_view()),
    path('webhook_transactions/', views.WebhookTransactions.as_view())
]