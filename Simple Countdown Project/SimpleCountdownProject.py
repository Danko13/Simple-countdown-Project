# A simple countdown script.

import time, subprocess

timeleft = 60

while timeleft > 0:
    print(timeleft, end='\n')
    time.sleep(1)
    timeleft = timeleft - 1


# TO DO: At the end of the countdown, play a sound.

subprocess.Popen(['start', 'alarm.wav'], shell=True)
