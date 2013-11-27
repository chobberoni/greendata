#thhis is a csvcruncher
import datetime
import csv
import time
import os

##################grab files#########
import subprocess
#subprocess.call(['rm','STATUS.txt'])

mylis = subprocess.Popen(['ls | grep mb'],shell=True, stdout=subprocess.PIPE)
#mylist = subprocess.Popen(['grep','mb'],shell=True, stdin=mylis.stdout)

out, err = mylis.communicate()
out = str(out)
#print out

outt = open("Outtx.txt","w")
outt.write(out)
outt.close()

listofmbs = open("Outtx.txt","r")
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
#		print len(arrayhh)
		with open (innyz, 'rb') as f:
			reader = csv.reader(f,delimiter=',')
			for row in reader:
				colmn1 = row[0]
				if datetoday in colmn1:
#					print datetoday
					woret = csv.writer(now)
					woret.writerows(reader)
with open(nowfile) as pww:
	pwss = csv.reader(pww)
	print list(pwss)
