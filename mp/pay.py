from django.http import HttpResponse

import json
import hashlib
from django.db import connections
import logging
import random
import string
import datetime
import time
import urllib2
import requests
#cursor = connections['default'].cursor()
import xml.etree.ElementTree as ET
#from flask import Flask, request, jsonify


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

def xml_to_dict(xml_data):
    '''
    xml to dict
    :param xml_data:
    :return:
    '''
    xml_dict = {}
    root = ET.fromstring(xml_data)
    for child in root:
        xml_dict[child.tag] = child.text
    return xml_dict

def create_sign(pay_data,merchant_key):
        
	stringA = '&'.join(["{0}={1}".format(k, pay_data.get(k))for k in sorted(pay_data)])
        stringSignTemp = '{0}&key={1}'.format(stringA, merchant_key)
        sign = hashlib.md5(stringSignTemp).hexdigest()
        return sign.upper()

def index(request):
	#cursor = connections['default'].cursor()	    
    #return HttpResponse("Hello world ! ")
	 bno = request.GET['bno']
	#cursor.execute("select Orders.ono,ostatus,Seller.sno,sname,simg from Orders,Seller where Orders.sno = Seller.sno and Orders.bno = %s",(bno,))

	#raw = dictfetchall(cursor)
	#cursor.close()
	 now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   	 my_out_trade_no = str(int(time.time()))
	 data = {
        	'appid': 'wx249ce8c7c0899bfc',
         	'mch_id': '1338576301',
        	'nonce_str': now,
       	 	'body': 'aa-bb',
        	'out_trade_no': my_out_trade_no,
       	 	'total_fee': 1,
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
	 #resp = HttpResponse(data, content_type="application/xml")
         #return resp
    	 url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    	 #req = urllib2.Request(url, data, headers={'Content-Type': 'application/xml'})
    	 #result = urllib2.urlopen(req, timeout=10000).read()
#    	 headers = {
#	'Content-Type': 'application/xml',
 #   		}
#
 #   	 response = requests.request("POST", url, headers=headers, params=data)
	 req = urllib2.Request(url, data, headers={'Content-Type': 'application/xml'})	
	 result = urllib2.urlopen(req, timeout=30).read()
    	 prepay_id = xml_to_dict(result).get('prepay_id')
	 paySign_data = {
                'appId': 'wx249ce8c7c0899bfc',
                'timeStamp': my_out_trade_no,
                'nonceStr': now,
                'package': 'prepay_id={0}'.format(prepay_id),
                'signType': 'MD5',
            }
	 paySign = create_sign(paySign_data,'n29sni59xnn593hdm3mpds8y3n386uop')
	 paySign_data.pop('appId')
	 paySign_data['paySign'] = paySign 
	
    	 resp = HttpResponse(json.dumps(paySign_data), content_type="application/json")
    	 return resp

def notify(request):

    	# data= {}
    	# data['status'] = 1
    	# response = HttpResponse(json.dumps(data), content_type="application/json")
    	# return response
	tcursor = connections['default'].cursor()
	tcursor.execute("insert into logs values(null,'test',sysdate())")
        tcursor.close()	
#	rstr = str(request)
#	file_object = open('/static/thefile.txt', 'w')
#	file_object.write("b")
#	file_object.close( )
	if request.method == 'POST':
		dict_data = xml_to_dict(request.body)
        	#logging.info(dict_data)
		cursor = connections['default'].cursor()
		cursor.execute("insert into logs values(null,%s,sysdate())",(dict_data['appid'],))
		cursor.close()
        	result_data = {
            		'return_code': 'SUCCESS',
            		'return_msg': 'OK'
        	}
        	return HttpResponse(dict_to_xml(result_data),content_type="application/xml")
	result_data = {
                        'return_code': 'SUCCESS',
                        'return_msg': 'OK'
        }
	
#	return dict_to_xml(result_data), {'Content-Type': 'application/xml'}	
	return(HttpResponse(result_data, content_type="application/xml"))
