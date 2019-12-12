import requests
import time
count = 10
while count>0:
	r = requests.get('http://185.6.26.128/DataLog.html?RecentEntries=40&id=268435572&FileName=dataLog.csv')
	print(r.text)
	count-=1
	time.sleep(10)