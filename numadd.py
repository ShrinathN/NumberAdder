#!/bin/python
import sys
import pandas as pd
from subprocess import call
import time

def android_input_touch(xy):
	call('adb shell input touchscreen tap ' + xy, shell=True)

def android_input_text(txt):
	call('adb shell input text ' + txt, shell=True)
	
def android_input_swipe(xy1, xy2, milli):
	call('adb shell input touchscreen swipe ' + xy1 + " " + xy2 + " " + milli, shell=True)

if(len(sys.argv) == 1):
	print("USAGE\n",sys.argv[0],"[csv file]")
	exit()

point_new_contact_xy = "510 520"
point_first_name_xy = "384 710"
point_last_name_xy = "390 890"
point1_swipe_down = "724 920"
point2_swipe_down = "724 640"
point_number_xy = "520 760"
point_submit_xy = "860 170"

first_name_tag = "APPDEV"

data = pd.read_csv(sys.argv[1])
for i in range(0, len(data)):
	print('Processing',i,'...',end='')
	android_input_touch(point_new_contact_xy)
	android_input_text(first_name_tag)
	android_input_touch(point_last_name_xy)
	android_input_text(data['Name'][i])
	android_input_swipe(point1_swipe_down, point2_swipe_down, 500)
	android_input_touch(point_number_xy)
	android_input_text(str(data['Number'][i]))
	android_input_touch(point_submit_xy)
	time.sleep(1)
	print('Done')