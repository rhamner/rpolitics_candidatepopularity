import praw
import matplotlib.pyplot as plt
import datetime
import numpy as np

reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     password='*',
                     user_agent='*',
                     username='*')

num = 0						#number of posts					
dailyFile = open('C:\Temp\candidatesDaily.txt', 'w')
dailyFile.write("time\tTrump\tClinton\tCruz\tSanders\tRubio\tBush\tCarson\tKasich\n")
start=1479168000				#start on July 14th, 2017
while(start > 1431648000):
	stop = start + 86399			#stop at the end of the current day
	trump = 0
	clinton = 0
	cruz = 0
	sanders = 0
	rubio = 0
	bush = 0
	carson = 0
	kasich = 0
	for submission in reddit.subreddit('politics').submissions(start, stop):
		lowerTitle = submission.title.lower()
		num = num + 1
		print(num)
		try:
			if((lowerTitle.find('donald') >= 0) or (lowerTitle.find('trump') >= 0)):
				trump = trump + 1
			if((lowerTitle.find('hillary') >= 0) or (lowerTitle.find('clinton') >= 0)):
				clinton = clinton+ 1
			if((lowerTitle.find('ted') >= 0) or (lowerTitle.find('cruz') >= 0)):
				cruz = cruz + 1
			if((lowerTitle.find('bernie') >= 0) or (lowerTitle.find('sanders') >= 0)):
				sanders = sanders + 1
			if((lowerTitle.find('marco') >= 0) or (lowerTitle.find('rubio') >= 0)):
				rubio = rubio + 1
			if((lowerTitle.find('jeb') >= 0) or (lowerTitle.find('bush') >= 0)):
				bush = bush + 1
			if((lowerTitle.find('carson') >= 0)):
				carson = carson + 1
			if((lowerTitle.find('kasich') >= 0)):
				kasich = kasich + 1
				
		except:
			print('something happened')
	
	dailyFile.write(str(start + 43200) + "\t" + str(trump) + "\t" + str(clinton) + "\t" + str(cruz) + "\t" + str(sanders) + "\t" + str(rubio) + "\t" + str(bush) + "\t" + str(carson) + "\t" + str(kasich) + "\n")
	start = start - 86400			#move to the next day
	print(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'))

dailyFile.close()				#dump data to file
