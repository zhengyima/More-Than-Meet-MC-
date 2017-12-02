from django.http import HttpResponse

import json
from django.db import connections

cursor = connections['default'].cursor()

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]
def index(request):
	    
    #return HttpResponse("Hello world ! ")
	cursor.execute("select * from Seller,Seller_display where Seller.sno = Seller_display.sno and Seller_display.sflag = 1")
	raw = dictfetchall(cursor)		
	response = HttpResponse(json.dumps(raw),content_type="application/json")	
	return response
