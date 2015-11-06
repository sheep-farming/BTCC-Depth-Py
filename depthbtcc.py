import pysocketio_client as io
import logging
import time
import json
import re
import hmac
import hashlib
import base64
import os
from termcolor import colored
import pysocketio_client as io

socket = io.connect('https://websocket.btcc.com/')

def a(data):
	os.system('clear')
	rAsk=data['grouporder']['ask']
	rBid=data['grouporder']['bid']
	for e in rAsk[0:4]:
		print colored("%.2f"%e['price'],'red'),e['totalamount']
	print colored("%.2f"%rAsk[4]['price'],'red',attrs=['bold','reverse']),rAsk[4]['totalamount']
	print colored("%.2f"%rBid[0]['price'],'green',attrs=['bold','reverse']),rBid[0]['totalamount']
	for e in rBid[1:5]:
		print colored("%.2f"%e['price'],'green'),e['totalamount']


@socket.on('connect')
def connected():
	print "Connected!"
	socket.emit('subscribe', 'grouporder_cnybtc');



@socket.on('ticker')
def ticker(data):
	#	print data
	a=1

@socket.on('grouporder')
def grouporder(data):
	#print data
	a(data)
while 1:
	if (raw_input()=='quit'):
		os._exit(0)