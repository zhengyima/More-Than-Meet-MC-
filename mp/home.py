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
	cursor.execute("select Seller.sno,sname,sgender,sage,sheight,sweight,sxz,sschool,smajor,sgrade,stime,srange,swage,sinfo,simg,slike from Seller,Seller_display where Seller.sno = Seller_display.sno and Seller_display.sflag = 1")
	raw = dictfetchall(cursor)
	for rawitem in raw:
		sno = rawitem['sno']
		lcursor = connections['default'].cursor()
		lcursor.execute("select lno,lname from Seller,Seller_label where Seller.sno = Seller_label.sno and Seller_label.sno = %s",(sno,))
		rawitem['labels'] = dictfetchall(lcursor)

		icursor = connections['default'].cursor()
		icursor.execute("select ino,iurl from Seller,Seller_image where Seller.sno = Seller_image.sno and Seller_image.sno = %s",(sno,))
		rawitem['images'] = dictfetchall(icursor)
		#rawitem['arr'] = arr
	#snoraw = fetchall(cursor)
	#for item in snoraw:
		#sno  = snoraw[0]
		#cursor.execute()
			
	response = HttpResponse(json.dumps(raw),content_type="application/json")	
	return response
