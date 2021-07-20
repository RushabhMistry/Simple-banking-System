from django.urls import path
from django.contrib import admin
from . import views
# from simpleBankingSystem.views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('transferMoney/', views.transferMoney, name='transferMoney'),
    path('transactionRecords/', views.transactionRecords, name='transactionRecords'),
    # path('ajax-posting/', ajax_posting, name='ajax_posting')
]