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
		if fnmatch.fnmatch(name,'*mp4'):
		
						output = var1.replace('mp4','ts')
						print 'convert mp4 files to ts files'
						string2 = 'sudo ffmpeg -i '+var1+' -c copy '+'-f mpegts -y '+output
						subprocess.call(string2,shell = True)
						valuestring = output.rsplit('/',1)
						if(valuestring[1] != 'final3.ts'):
							 list1.append(valuestring[1])
						dic1[dirname] = list1
for key,value in dic1.iteritems():
	input = ""
	result = ""
		inputstring = ""


	for k in natsorted(value):
		
		rgx = re.compile(r'slide-\d+-\d+\.ts')
		if rgx.match(k):
						value = k
			inputstring = inputstring + " "+ k 


			else:
			 if len(value) > 1:
				 input = input + k + "|"



		value = inputstring.split(' ')
		del value[0]

		values_list= [int(el.split("-")[-2]) for el in value]


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


			  list1 = []
			  list2 = []
			  for i,j in zip(one_array,two_array):
				list1.append(i)
				list1.append(j)

			  new_string = " ".join(list1)

			  for i,j in zip(third_array,forth_array):
		        list2.append(i)
				list2.append(j)

			  new_string1 = " ".join(list2)

			  inputstring = input
			  value = inputstring.split('|')
			  value_array = inputstring.split('|')

			  del value[len(value)-1]
			  del value_array[len(value_array)-1]
			  for i,el in enumerate(value):
		pp = re.sub('\.ts','',el)
		value[i] = pp
			  values_list = [int(el.split("-")[-1])for el in value]

			  split_location = [idx  + 1 for (idx, el), next_el in zip(enumerate(values_list[:-1]), values_list[1:])
			  if (next_el - el) > 1]


			  if len(split_location) > 1:

				first_half_input = value_array[:split_location[0]]

				second_half_input = value_array[split_location[0]:split_location[1]]

				third_half_input = value_array[split_location[1]:]


				input = " ".join(first_half_input).replace(' ','|')+"|"+new_string.replace(' ','|')+"|"+" ".join(second_half_input).replace(' ','|')+"|"+new_string1.replace(' ','|')+"|"+" ".join(third_half_input).replace(' ','|')


		else:
		if len(value) > 1: 

						 v = numpy.diff(values_list)
						 location =(numpy.where(v)[0]+1)
						 result = numpy.split(value,location)

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

						 firstring = input

						 input_result = firstring.split('|')
						 second_list  = firstring.split('|')



						 del input_result[len(input_result)-1]
						 del second_list [len(input_result)-1]


					 for i,el in enumerate(input_result):
						 pp = re.sub('\.ts','',el)
						 input_result[i] = pp

						 lll_list = [int(el.split("-")[-1])for el in input_result]


						 split_location = [idx  + 1 for (idx, el), next_el in zip(enumerate(lll_list[:-1]), lll_list[1:])
						 if (next_el - el) > 1]
						 if len(split_location) > 0:
							first_split = second_list[:split_location[0]]

							third_split = second_list[split_location[0]:]

								first_split_string = " ".join(first_split)
								third_split_sring =  " ".join(third_split)
							input =  first_split_string.replace(' ','|')+"|"+new_string.replace(' ','|')+"|"+third_split_sring.replace(' ','|')


		inut = key
		location_string = inut.rsplit('/',2)
		output_location = location_string[0]

		os.chdir(key)
		print os.getcwd()

		if (len(input)> 0 ):
			command = 'sudo ffmpeg -i '+'\"concat' +":"+input + ""+"\""+' '+'-c copy -bsf:v h264_mp4toannexb -f mpegts -y'+' '+ key+ '/final3.mp4'
			#print command
			subprocess.call(command,shell=True)

