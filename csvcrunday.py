import datetime
import csv
import os

##################grab files#########
import subprocess



import time
from apscheduler.scheduler import Scheduler

def somejob():

		mylis = subprocess.Popen(['ls | grep mb'],shell=True, stdout=subprocess.PIPE)
		#mylist = subprocess.Popen(['grep','mb'],shell=True, stdin=mylis.stdout)

		out, err = mylis.communicate()
		out = str(out)
		#print out

		outt = open("Outt.txt","w")
		outt.write(out)
		outt.close()

		listofmbs = open("Outt.txt","r")
		arrayhh = []
		for line in listofmbs:
			arrayhh.append(line)
		listofmbs.close()

		#print len(arrayhh)
		file_name_start = arrayhh[0]

		#for item in arrayhh:
		#	print item
		#print len(arrayhh)


		###############Date Group######################
		datee = datetime.date.today()
		datetoday = datee.strftime("%Y-%m-%d")
		#tempdate = '2013-11-22'
		#print datetoda
		#print type(datetoday)
		catstring = "_obviuscsv.csv"
		nowfile = "newf/" + datetoday + catstring
		#print nowfile
		################################################


		##############Loop and Execute Part#############
		with open(nowfile, 'wb') as now:
			for index in range(0,len(arrayhh)):
				innys = (arrayhh[index])
				innyz = innys[0:-1]
				with open (innyz, 'rb') as f:
					reader = csv.reader(f)
					for row in reader:
						colmn1 =  row[0]
						if datetoday in colmn1:
							writer = csv.writer(now)
		 					writer.writerows(reader)
#		retcode = subprocess.Popen('rm mb*', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		
		

if __name__ == '__main__':
      sched = Scheduler()
      sched.start()
      sched.daemonic = False
      sched.add_cron_job(somejob,day='*/1')


while True:
      time.sleep(2)
sched.shutdown()
