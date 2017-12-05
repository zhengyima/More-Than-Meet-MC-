from django.http import HttpResponse

import json
from django.db import connections
from datetime import date, datetime
import pytz
tz  = pytz.timezone('Asia/Shanghai')
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

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
	cursor.execute("select Orders.ono,ostatus,Seller.sno,sname,simg,otime from Orders,Seller where Orders.sno = Seller.sno and Orders.bno = %s and ostatus = 1",(bno,))

	raw = dictfetchall(cursor)
	#now = datetime.utcnow().replace(tzinfo=<Asia/Shanghai>)
	now = datetime.now(pytz.timezone('Asia/Shanghai'))
	for item in raw:
		item['otime'] = item['otime'].replace(tzinfo=pytz.timezone('Asia/Shanghai'))
		item['oday'] = (now-item['otime']).days
		item['now'] = json_serial(now)
		item['osecond'] = (now-item['otime']).seconds
		#item['ominute'] = (now-item['otime']).minutes
		item['ohour'] =item['oday']*24+ ((now-item['otime']).seconds - item['oday']*24*60*60)/(60*60)
		minutes = (item['osecond'] % 3600)
		item['ominute'] = minutes - item['oday']*24*60 - item['ohour']*60
		item['otime'] = json_serial(item['otime'])
		
	cursor.close()

	response = HttpResponse(json.dumps(raw),content_type="application/json")	
	return response
