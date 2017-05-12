import os
import fnmatch
import subprocess
dic1 = {}
dic2 = {}
d = {}
for dirname,dirs,files in os.walk('/var/bigbluebutton/published/presentation',topdown = False):
	list1 = []
	for name in files:
		var1 = os.path.join(dirname,name)
                if fnmatch.fnmatch(name,'*.ogg'):
			#print var1
                        audio_output = var1.replace('ogg','mp3')
                        stringz = 'ffmpeg -i '+var1+' -acodec libmp3lame -y '+audio_output
                        #subprocess.call(stringz,shell=True)
                        teststring = dirname.rsplit('/',1)
                        result = teststring[0]
			#list1.append(var1)
			dic1[result] = audio_output
#print dic1		

for dirname,dirs,files in os.walk('/var/bigbluebutton/published/presentation',topdown = False):
        list1=[]
	for name in files:
		var1 = os.path.join(dirname,name)
		if fnmatch.fnmatch(var1,'*/final3.mp4'):
			#print var1
                        teststring = dirname.rsplit('/',2)
                        result = teststring[0]
			list1.append(name)
			dic2[result] = var1
#print dic2

for key in set(dic1.keys()+dic2.keys()):
	try:
		d.setdefault(key,[]).append(dic1[key])
        except KeyError:
		pass
        try:
                d.setdefault(key,[]).append(dic2[key])
        except:
		pass


#print d
count = 0
for key,value in d.iteritems():
        os.chdir(key)
        if len(value) > 1:
             audio = value[0]
	     video = value[1]
	     string = 'sudo ffmpeg '+'-i'+' '+audio+' '+'-i'+' '+video+' '+'-vcodec copy -shortest -y ' +key+'/'+ 'result.mp4'
             #print string
             #string2 = 'sudo ffmpeg '+'-i'+' '+audio+' '+'-i'+' '+video+' '+'-vcodec copy -y '+key+'/'+'result.mp4'
             print string
             subprocess.call(string,shell=True)
