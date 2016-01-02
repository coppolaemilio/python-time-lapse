import pyscreenshot as ImageGrab
import os
import datetime
import time
import sys

working_dir = "projects"
project = datetime.datetime.now().strftime("%I%M%S%b%d%Y")
screenshot_rate = 1

#Create project folder
os.mkdir(os.path.join(working_dir, project))

def get_file_number(number):
    n = '%05d' % number
    return n

def render_movie(project_dir):
    os.system("ffmpeg -f image2 -r 1/0.1 -i " + project_dir + "/scr_%05d.png -vcodec mpeg4 -vb 20M -y " + project + ".mp4")
    return True


#Start taking screenshots
def record(countdown = 0, screenshot_number = 0):
    print "[+] Countdown:", countdown, "/ Starting position:", screenshot_number
    try:
        while True:
            if countdown > 0:
                print "[+] Staring in", str.replace(str(countdown), "-", "")
                countdown -= 1 
            else:
                print "[+] Taking Screenshot number", screenshot_number
                ImageGrab.grab_to_file(os.path.join(working_dir, project, 'scr_' + get_file_number(screenshot_number) + '.png'))
                screenshot_number += 1
            time.sleep(screenshot_rate)
    except KeyboardInterrupt:
        print "[+] Saving video..."
        if raw_input("Paused, continue? y/n: ") == "y":
            record(0,screenshot_number)
        else:
            if raw_input("Render recorded video? y/n: ") == "y":
                render_movie(os.path.join(working_dir, project))
        pass

if len(sys.argv) > 1:
    if sys.argv[1] == "h":
        print """
python-time-lapse v0.1 Screen time-lapse creator.
Copyright (c) 2016, Evelend, Emilio Coppola <emilio@evelend.com>
python app.py"""
    else:
        number = int(sys.argv[1])
        record(countdown = 3, screenshot_number = number)
else:
    record(countdown = 3)
