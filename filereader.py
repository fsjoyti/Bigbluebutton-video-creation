import os
import fnmatch
import json
import subprocess
import xmltodict
import datetime
import time
time_in = 0.0
time_out = 130.0
for dirname,dirs,files in os.walk('/var/bigbluebutton/published/presentation',topdown = False):
	for name in files:
		var1 = os.path.join(dirname,name)
		if fnmatch.fnmatch(var1,'*/shapes.svg'):
			with open(var1,"rb") as f:
				d = xmltodict.parse(f)
				json_string = json.dumps(d,indent = 4)

                                data = json.loads(json_string)
				for key,value in data.iteritems():
					info_dic = dict((innerk,innerv)for innerk,innerv in value.iteritems() if innerk == 'image')
				for key,value in info_dic.iteritems():

					for dic in value:
						if '@height' in dic:
							del dic['@height']
                                                if  '@width' in dic:
							del dic['@width']
					        if   '@x' in dic:
							del dic['@x']
                                                if  '@text' in dic:
							del dic['@text']
                                                if   '@id' in dic:
							del   dic ['@id']
                                                if   '@visibility' in dic:
							del dic ['@visibility']
                                       

                                output = var1.rsplit('/',1)
				directory = output[0]

                                for key,value in info_dic.iteritems():
					for dic in value:

                                                if '@xlink:href' in dic:
						   fileinput = directory+'/'+ dic['@xlink:href']
                                                   print fileinput

                                                   inputstring = str(dic['@in'])
                                                   outputstring = str(dic['@out'])
                                                   if ' ' in inputstring and ' ' in outputstring:
							input_array = inputstring.split(' ')
                                                        output_array = outputstring.split(' ')
                                                        print(input_array)
                                                        print(output_array)
                                                        count = 0
                                                  
                                                        for i,j in zip(input_array,output_array):
                                                               time_in = float(i)

                                                               time_out = float(j)

                                                               count = count + 1

                                                               duration = time_out - time_in



							       print (duration)
                                                               valuestring = fileinput
                                                               output = valuestring.rsplit('/',1)

                                                               os.chdir(output[0])
                                                               output_value = output[1].replace('png','mp4')
                                                               output_file_name = output_value.split('.')
                                                               output_name = str(output_file_name[0]) +'-'+ str(count) +'.'+ str(output_file_name[1]) 

                                                               string = 'sudo ffmpeg -loop 1'+' '+ '-i'+ ' '+output[1]+' '+ '-c:v libx264 -framerate 24 -maxrate 3000k -bufsize 3000k -t' + ' '+str(duration) +' '+'-pix_fmt yuv420p -vf scale=720:480'+' '+'-y'+' '+ output_name                                            
                                                            subprocess.call(string,shell = True)

                                                   else:  
							time_in = float(dic['@in'])
                                                        
                                                        time_out = float(dic['@out'])

                                                        duration = time_out - time_in
                                                        print (duration)

                                                        minutes = duration%3600/60

                                                        valuestring = fileinput
                                                        output = valuestring.rsplit('/',1)

                                                        os.chdir(output[0])
                                                        output_value = output[1].replace('png','mp4')
                                                        string = 'sudo ffmpeg -loop 1 -i'+' '+output[1] +' '+ '-c:v libx264 -framerate 24 -maxrate 3000k -bufsize 3000k -t'+' '+str(duration)+' '+ '-pix_fmt yuv420p -vf scale=720:480'+' '+'-y'+' '+ output_value

                                                        subprocess.call(string,shell = True)
                                                        
