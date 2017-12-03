from django.http import HttpResponse

import json
from django.db import connections

#cursor = connections['default'].cursor()

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]

def index(request):
	cursor = connections['default'].cursor()	    
    #return HttpResponse("Hello world ! ")
	bno = request.GET['bno']
	cursor.execute("select Orders.ono,ostatus,Seller.sno,sname,simg from Orders,Seller where Orders.sno = Seller.sno and Orders.bno = %s",(bno,))
	raw = dictfetchall(cursor)
	cursor.close()

	response = HttpResponse(json.dumps(raw),content_type="application/json")	
	return response
