import os
import fnmatch
import subprocess
from natsort import natsorted
import re
import numpy
#from itertools import groupby
#from operator import itemgetter
dic1 = {}
dic2 = {}



for dirname,dirs,files in os.walk('/var/bigbluebutton/published/presentation',topdown = False):
	list1=[]
	for name in files:
		var1 = os.path.join(dirname,name)
		if fnmatch.fnmatch(name,'*mpg'):
			#print var1
			list1.append(name)
                        dic1[dirname] = list1
for key,value in dic1.iteritems():
	input = ""
	result = ""
        inputstring = ""
        #print key
        
	for k in natsorted(value):
		
		rgx = re.compile(r'slide-\d+-\d+\.mpg')
		if rgx.match(k):
                        value = k
			#valuestring = value.split('-',1)
                       # reverse_value = value.rsplit('-',2)
                        #print valuestring
                        #print reverse_value
                        #slide_number = valuestring[1]
                        
			inputstring = inputstring + " "+ k 
                        
	        else:
		     if len(value) > 1:
		    	 input = input + k + "|"
                    
       # print inputstring
        value = inputstring.split(' ')
        del value[0]
        
        values_list= [int(el.split("-")[-2]) for el in value]
        #print values_list
        gap_loc = [idx  + 1  
           for (idx, el), next_el in zip(enumerate(values_list[:-1]), values_list[1:])
           if (next_el - el) > 1] 
        if (len(gap_loc)) > 0:
              first = value[:gap_loc[0]]
              second = value[gap_loc[0]:]
              input_result1 = value

              n = len(first)/2
              n2 = len(second)/2
              one_array = first[:n]
              two_array = first[n:]
              third_array = second[:n2]
              forth_array = second[n2:]
             # print (one_array)
             # print (two_array)
              list1 = []
              list2 = []
              for i,j in zip(one_array,two_array):
		list1.append(i)
                list1.append(j)
              #print list1
              new_string = " ".join(list1)
              
              for i,j in zip(third_array,forth_array):
		list2.append(i)
                list2.append(j)
              #print list2
              new_string1 = " ".join(list2)
              #print (new_string1)
              #inputstring = new_string+ " "+ new_string1
              #print (inputstring)
           

              value = input.split(' ')
              del value[0]
              for i,el in enumerate(value):
		pp = re.sub('\.mp4','',el)
		value[i] = pp
              values_list = [int(el.split("-")[-1])for el in value]
              
              split_location = [idx  + 1 for (idx, el), next_el in zip(enumerate(values_list[:-1]), values_list[1:])
              if (next_el - el) > 1] 
              
             # first_split = input_result1[:split_location[0]]
             
              #third_split = input_result1[split_location[0]:split_location[1]]
              #forth_split = input_result1[split_location[1]:]
             # new_string  = " ".join(first_split)+" "+new_string+" "+" ".join(third_split)+" "+new_string1+" "+" ".join(forth_split)
              value_array = input.split(' ')
              del value_array[0]
              if len(split_location) > 1:
             	first_half_input = value_array[:split_location[0]]
              	second_half_input = value_array[split_location[0]:split_location[1]]
              	third_half_input = value_array[split_location[1]:]
              
              	input = " ".join(first_half_input)+"|"+new_string+"|"+" ".join(second_half_input)+"|"+new_string1+"|"+" ".join(third_half_input)
           
              
        else:
		if len(value) > 1: 
                                             
                         v = numpy.diff(values_list)
                         location =(numpy.where(v)[0]+1)
                         result = numpy.split(value,location)
                         #print result                       
                         one_array = result[0]
                         
                         two_array = result[1]
                         
                         third_array = result[2]
                        
                         list2 = []
                         for i,j in zip(one_array,two_array):
                             list2.append(i)
                             list2.append(j)
                        
                         new_string = " ".join(list2)
                         
                         last_value = two_array[-1]
                         n = len(third_array)/2
                         one = third_array[:n]
                         two = third_array[n:]
                         new_string =  new_string + " "+" ".join(one)+" "+ last_value+ " "+" ".join(two)
                         value = input.split(' ')
             		 del value[0]
                         input_result = input.split(' ')
                         del input_result[0]
                         
             		 for i,el in enumerate(value):
               			 pp = re.sub('\.mp4','',el)
               			 value[i] = pp
            	         values_list = [int(el.split("-")[-1])for el in value]
                        
                         split_location = [idx  + 1 for (idx, el), next_el in zip(enumerate(values_list[:-1]), values_list[1:])
                         if (next_el - el) > 1]
                         if len(split_location) > 0: 
                         	first_split = input_result[:split_location[0]]
                         
                         	third_split = input_result[split_location[0]:]
                        
                         
                         	input = " ".join(first_split)+" "+new_string+" "+" ".join(third_split)
                        
                         #print input
        inut = key
        location_string = inut.rsplit('/',2)
        output_location = location_string[0]
        #print output_location           
        #print (input)
        os.chdir(key)
        print 'directory'
        print os.getcwd()
       
        if (len(input)> 0 ):
        	command = 'sudo ffmpeg -i '+'\"concat' +":"+input + ""+"\""+' '+'-bufsize 3000k -q:v 3 -c copy -y '+' '+ key+ '/final3.mpg'
        	#print command
        	subprocess.call(command,shell=True)

