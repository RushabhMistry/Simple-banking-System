SELECT  A.*,
        SUM(IF(B.type=1,B.amount,0))-SUM(IF(B.type=2,B.amount,0)) AS Balance
FROM Customer AS A
    LEFT JOIN Transaction AS B ON A.user_id=B.user_id
GROUP BY A.user_id
ORDER BY A.name ASC



SELECT  A.*, SUM(IF(B.type=1,B.amount,0))-SUM(IF(B.type=2,B.amount,0)) AS Balance FROM Customer AS A LEFT JOIN Transaction AS B ON A.user_id=B.user_id GROUP BY A.user_id ORDER BY A.name ASC


SELECT USER_ID, NAME, EMAIL FROM CUSTOMER INNER JOIN TRANSACTION ON CUSTOMER.USER_ID = TRANSACTION.USER_ID;


                                                    
SELECT
    Customer.name,
    SUM(IF(Txnn.type=1,Txnn.amount,0))-SUM(IF(Txnn.type=2,Txnn.amount,0)) AS Balance
FROM Customer
INNER JOIN Txnn ON Customer.user-id = Txnn.user_id
GROUP BY Customer.user_id
ORDER BY Customer.name

SELECT Customer.name, SUM(IF(Transaction.type=1,Transaction.amount,0))-SUM(IF(Transaction.type=2,Transaction.amount,0)) AS Balance FROM Customer INNER JOIN Transaction ON Customer.user-id = Transaction.user_id GROUP BY Customer.user_id ORDER BY Customer.name






# def customers(request):
#     customers = Customer.objects.all()
#     customers = Transaction.objects.all()
#     with connection.cursor() as cursor:
#         query = """
#         SELECT
#             Customer.name,
#             SUM(IF(Transaction.type=1,Transaction.amount,0))-SUM(IF(Transaction.type=2,Transaction.amount,0)) AS Balance
#         FROM Customer
#         INNER JOIN Transaction ON Customer.user-id = Transaction.user_id
#         GROUP BY Customer.user_id
#         ORDER BY Customer.name
#         """
#         cursor.execute(query)
#         row = cursor.fetchone()
#     return render(request, 'customers.html', {'row': row})




SELECT
   artists.ArtistId, 
   AlbumId
FROM
   artists
LEFT JOIN albums ON
   albums.ArtistId = artists.ArtistId
ORDER BY
   AlbumId;


SELECT a.user_id, a.name, a.email,
       b.amount, b.type, b.type, b.narration, b.date
FROM Customers a 
LEFT JOIN Txnns b
ON a.user_id = c.user_id;



con = sqlite3.connect('Customer.db', 'Txnn.db')
    cur = con.cursor()
    cur.execute("""
        SELECT
            Customer.name,
            SUM(IF(Txnn.type=1,Txnn.amount,0))-SUM(IF(Txnn.type=2,Txnn.amount,0)) AS Balance
        FROM Customer
        INNER JOIN Txnn ON Customer.user-id = Txnn.user_id
        GROUP BY Customer.user_id
        ORDER BY Customer.name
    """)
    results = cur.fetchall()