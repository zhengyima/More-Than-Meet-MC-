from django.http import HttpResponse

import json
import hashlib
from django.db import connections

#cursor = connections['default'].cursor()

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]

def index(request):
	#cursor = connections['default'].cursor()	    
    #return HttpResponse("Hello world ! ")
	bno = request.GET['bno']
	#cursor.execute("select Orders.ono,ostatus,Seller.sno,sname,simg from Orders,Seller where Orders.sno = Seller.sno and Orders.bno = %s",(bno,))

	#raw = dictfetchall(cursor)
	#cursor.close()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'appid': 'wx249ce8c7c0899bfc',
        'mch_id': '1338576301',
        'nonce_str': now,
        'body': 'aa-bb',
        'out_trade_no': str(int(time.time())),
        'total_fee': '1',
        'spbill_create_ip': '118.89.233.180',
        'notify_url': 'https://mina.mapglory.com/pay_notify',
        'attach': '{"msg": "test"}',
        'trade_type': 'JSAPI',
        'openid': bno
    }
    stringA = '&'.join(["{0}={1}".format(k, data.get(k)) for k in sorted(data)])
    stringSignTemp = '{0}&key={1}'.format(stringA, "n29sni59xnn593hdm3mpds8y3n386uop")
    sign = hashlib.md5(stringSignTemp).hexdigest()

    data['sign'] = sign
    url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    req = urllib2.Request(url, data, headers={'Content-Type': 'application/xml'})
    result = urllib2.urlopen(req, timeout=10000).read()

    response = HttpResponse(json.dumps(result), content_type="application/json")
    return response

def notify(request)

    data= {}
    data['status'] = 1
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response

