import cv2
import subprocess
import time
import pyscreenshot as ImageGrab

im = ImageGrab.grab([2400, 550, 3350, 780])
im.save('sc.png')
bashCommand = "tesseract sc.png output"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
replacements = {'.':'.,', ',':'.,'}
with open('output.txt') as infile, open('output1.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)
    time.sleep(1)
text = open('output1.txt', 'r').read().strip().replace('\n',' ')
for ch in text:
    subprocess.call(["xdotool", "type", ch])
    time.sleep(.001)
