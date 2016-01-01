import pyscreenshot as ImageGrab
import os
import datetime
import time
import sys

working_dir = "projects"
project = datetime.datetime.now().strftime("%I%M%S%b%d%Y")
screenshot_rate = 1
recording = True

#Create project folder
os.mkdir(os.path.join(working_dir, project))

def get_file_number(number):
    n = '%05d' % number
    return n

def render_movie(project_dir):
    os.system("ffmpeg -f image2 -r 1/0.1 -i " + project_dir + "/scr_%05d.png -vcodec mpeg4 -vb 20M -y " + project + ".mp4")
    return True


#Start taking screenshots
def record(countdown = 0):
    screenshot_number = 0 - countdown
    try:
        while True:
            if screenshot_number >= 0:
                print "[+] Taking Screenshot number", screenshot_number
                ImageGrab.grab_to_file(os.path.join(working_dir, project, 'scr_' + get_file_number(screenshot_number) + '.png'))
            else:
                print "[+] Staring in", str.replace(str(screenshot_number), "-", "")
            screenshot_number += 1
            time.sleep(screenshot_rate)
    except KeyboardInterrupt:
        print "[+] Saving video..."
        if raw_input("Render recorded video? y/n: ") == "y":
            render_movie(os.path.join(working_dir, project))
        pass

if len(sys.argv) > 1:
    if sys.argv[1] == "h":
        print """
python-time-lapse v0.1 Screen time-lapse creator.
Copyright (c) 2015-2016, Evelend, Emilio Coppola <emilio@evelend.com>
python app.py"""
else:
    record(countdown = 3)
