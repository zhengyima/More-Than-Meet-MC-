from django.http import HttpResponse

import json
import hashlib
from django.db import connections

import random
import string
import datetime
import time
import urllib2
import requests
#cursor = connections['default'].cursor()

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]
def dict_to_xml(dict_data):
    '''
    dict to xml
    :param dict_data:
    :return:
    '''
    xml = ["<xml>"]
    for k, v in dict_data.iteritems():
        xml.append("<{0}>{1}</{0}>".format(k, v))
    xml.append("</xml>")
    return "".join(xml)

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
   	 sign = hashlib.md5(stringSignTemp).hexdigest().upper()

    	 data['sign'] = sign
	 data = dict_to_xml(data)
    	 url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    	 #req = urllib2.Request(url, data, headers={'Content-Type': 'application/xml'})
    	 #result = urllib2.urlopen(req, timeout=10000).read()
    	 headers = {
	'Content-Type': 'application/xml',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'x-devtools-emulate-network-conditions-client-id': "6d9ff6c0-092e-41e9-970a-169d453074a6",
    'upgrade-insecure-requests': "1",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "no-cache",
    		}

    	 response = requests.request("POST", url, headers=headers, params=data)
    
    	 resp = HttpResponse(json.dumps(response.text), content_type="application/json")
    	 return resp

def notify(request):

    	 data= {}
    	 data['status'] = 1
    	 response = HttpResponse(json.dumps(data), content_type="application/json")
    	 return response

