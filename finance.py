# -*- coding:utf8 -*-
from sys import argv
import urllib2
import json
import time
from datetime import datetime

class GoogleFinanceAPI:
	def __init__(self):
		self.prefix = "http://finance.google.com/finance/getprices?q=%d&x=TPE&i=%d&p=%s&f=d,c,h,l,o,v"
	
	def get(self,stock_id,time_offset,duration):
		url = self.prefix %(stock_id,time_offset,duration)
		u = urllib2.urlopen(url)
		content = u.read()
		splitContent = content.split("\na")
		i_timestamp = 0
		i_timestampBase = 0
		print '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
		for line in splitContent[1].split():
			splitLine = line.split(',')
			if i_timestamp == 0:
				i_timestampBase = int(splitLine[0])
				i_timestamp = i_timestampBase
			else:
				i_timestamp = i_timestampBase + int(splitLine[0])*time_offset
			
			print datetime.fromtimestamp(i_timestamp).strftime('%Y-%m-%d %H:%M:%S'),
			print "\t%.2f \t%.2f \t%d" %(float(splitLine[1]),float(splitLine[4]),int(splitLine[5])/1000)
		
		print '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
		#partitionContent = content.partition("TIMEZONE_OFFSET=")
		#print partitionContent[2]
		#obj = json.loads(content[3:])
		#return obj[0]
		
		
if __name__ == "__main__":
	c = GoogleFinanceAPI()
	
	script, id, t, d = argv
	while 1:
		#quote = c.get(2499,86400,"3d")
		c.get( int(id), int(t), d)
		#print quote
		time.sleep(60)
		
