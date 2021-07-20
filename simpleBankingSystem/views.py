from django.shortcuts import render
from django.http import HttpResponse
from . models import Customer
from . models import Txnn
# from .forms import err
from django.db import connection
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def customers(request):

    query = """
        SELECT  A.*,
            SUM(IF(B.type=1,B.amount,0))-SUM(IF(B.type=2,B.amount,0)) AS Balance
        FROM simplebankingsystem_customer AS A
            LEFT JOIN simplebankingsystem_txnn AS B ON A.user_id=B.user_id
        GROUP BY A.user_id
        ORDER BY A.name ASC
    """
    cursor = connection.cursor()
    cursor.execute(query)
    results = dictfetchall(cursor)
    return render(request, 'customers.html', {'results': results})

def transferMoney(request):
    query = """
        SELECT  A.*,
            SUM(IF(B.type=1,B.amount,0))-SUM(IF(B.type=2,B.amount,0)) AS Balance
        FROM simplebankingsystem_customer AS A
            LEFT JOIN simplebankingsystem_txnn AS B ON A.user_id=B.user_id
        GROUP BY A.user_id
        ORDER BY A.name ASC
    """
    if request.method=="POST":
        user_id = request.POST['drId']
        amount = request.POST['amount']
        narration = request.POST['narration']
        date = request.POST['date']
        type = '2'
        ins = Txnn(user_id=user_id, amount=amount, narration=narration, date=date, type=type)
        ins.save()

    #     if form.is_valid():
    #         redirect('transferMoney')
    
    # else:
    #     form = 

    if request.method=="POST":
        user_id = request.POST['crId']
        amount = request.POST['amount']
        narration = request.POST['narration']
        date = request.POST['date']
        type = '1'
        ins = Txnn(user_id=user_id, amount=amount, narration=narration, date=date, type=type)
        ins.save()
        print("Stored")

    cursor = connection.cursor()
    cursor.execute(query)
    results = dictfetchall(cursor)
    return render(request, 'transferMoney.html', {'results': results})

def transactionRecords(request):
    query = """
        SELECT  A.*, IF(B.type=1,'Cr','Dr') AS type, B.narration, B.amount, B.date, B.time
        FROM simplebankingsystem_customer AS A
            LEFT JOIN simplebankingsystem_txnn AS B ON A.user_id=B.user_id
        ORDER BY  B.date ASC, B.time DESC
    """
    cursor = connection.cursor()
    cursor.execute(query)
    results = dictfetchall(cursor)
    return render(request, 'transactionRecords.html', {'results': results})
    
# def ajax_posting(request):
#     if request.is_ajax():
#         amt = request.POST.get('amt', None) 
#         bal = request.POST.get('bal', None)
#         if amt >= bal: 
#             response = {
#                 'msg':'Your amount must not be greater than available balance.'
#             }
#         return JsonResponse(response)