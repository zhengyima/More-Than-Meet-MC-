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
	sno = request.GET['sno']
	cursor.execute("select Seller.sno,sname,sgender,sage,sheight,sweight,sxz,sschool,smajor,sgrade,stime,srange,swage,sinfo,simg,slike,scharm,snum from Seller where Seller.sno = %s",(sno,))
	raw = dictfetchall(cursor)
	cursor.close()

	lcursor = connections['default'].cursor()
	lcursor.execute("select lno,lname from Seller,Seller_label where Seller.sno = Seller_label.sno and Seller_label.sno = %s",(sno,))
	raw[0]['labels'] = dictfetchall(lcursor)
	lcursor.close()

	icursor = connections['default'].cursor()
	icursor.execute("select ino,iurl from Seller,Seller_image where Seller.sno = Seller_image.sno and Seller_image.sno = %s",(sno,))
	raw[0]['images'] = dictfetchall(icursor)
		#rawitem['arr'] = arr
	#snoraw = fetchall(cursor)
	#for item in snoraw:
		#sno  = snoraw[0]
		#cursor.execute()
	icursor.close()			
	response = HttpResponse(json.dumps(raw),content_type="application/json")	
	return response


def like(request):
	scursor = connections['default'].cursor()
	scursor.execute("select * from Seller_like where sno = %s and bno = %s",(request.GET['sno'],request.GET['bno'],))
	raw = dictfetchall(scursor)
	data = {}
	if(len(raw)>0):
		data['status'] = 2
		response = HttpResponse(json.dumps(data),content_type="application/json")
		return response
	
	lcursor = connections['default'].cursor()
	flag1 = lcursor.execute("insert into Seller_like values(%s,%s)",(request.GET['sno'],request.GET['bno'],))
	if flag:
		ucursor = connections['default'].cursor()
		flag2 = ucursor.execute("update seller set snum = snum + 1 where seller.sno = %s",(request.GET['sno'],))
		if flag2:
			data['status'] = 1
			response = HttpResponse(json.dumps(data),content_type="application/json")
			return response
	data['status'] = 0
	response = HttpResponse(json.dumps(data),content_type="application/json")
	return response