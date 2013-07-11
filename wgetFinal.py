# For any queries, mail me at sjs7007@gmail.com!

import os
import urllib2

base_link='https://class.coursera.org/startup-001/lecture/index'
base_source=urllib2.urlopen(base_link).read()
#print base_source

def FindDownloadLinks(ip): #find download links of videos
	if(ip=='0'):	
		count=0
	else:
		string=ip[:ip.find('.')]
		count=int(string)
	
	initial=FindStart(ip)
	print initial
	for i in range (0,1000):
		count=count+1
		start_link=base_source.find('href="https://class.coursera.org/startup-001/lecture/downloa',initial)+6
		end_link=base_source.find('"',start_link)
		link=base_source[start_link:end_link]		
		#print start_link
		os.system("wget -c %s" %link)	
		RenameFiles(link,count)
		FindTitles(start_link,count)
		initial=end_link
		if (i==0):
			breakval=initial
		if(initial==breakval and i!=0):
			print "break!"
			break

def RenameFiles(link,count): #rename files in order to numbers
	file_name=link[47:]
	toName=str(count)+'.'+file_name[24:]+'.mp4'
	#print file_name
	#print toName
	os.system("mv %s %s" %(file_name,toName))	

def FindTitles(start_link,count):
	startTitle=base_source.find('hidden">Video (MP4) for ',start_link)+24
	endTitle=base_source.find('</div>',startTitle)
	title=base_source[startTitle:endTitle]
	print title
	os.system("echo %d. %s | cat >> log.txt"%(count,title))

def FindStart(ip): #find from where to start downloading based on name of last file
	if(ip=='0'):
		return 0
	else:
		vid=ip[ip.find('.')+1:]
		toFind='https://class.coursera.org/startup-001/lecture/download.mp4?lecture_id='+str(vid)
		#print toFind		
		startPos=base_source.find(toFind)+len(toFind)+10
		return startPos

ip=raw_input("Enter file name of last video downloaded(like 1.57) or 0 as input if using the script for first time : ") 
FindDownloadLinks(ip)
os.system("echo ------------------------------------------------------------------------------------------------- | cat >> log.txt")

