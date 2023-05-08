from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
import subprocess
import time
import autoconnect
import evdev




autoconnect.connect()


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(14, GPIO.OUT)

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == "Xbox Wireless Controller":
		gamepad = InputDevice(str(device.path))
		print(f"Connected to {device.name}")
		break



servo = Servo(14)

#gamepad = InputDevice('/dev/input/event4')

#values

#codes
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308
rTrig = 9
lTrig = 10


def run_cmd(command: str):
	process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	stdout, stderr = process.communicate()
	return stdout.decode("utf-8")



def mapvalues(num, inMin, inMax, outMax, outMin):
	return outMin + (float(num-inMin) / float(inMax - inMin) * (outMax-outMin))


#print(run_cmd("bluetoothctl connect 9C:AA:1B:D3:FF:03 "))

for event in gamepad.read_loop():
#	if event.type == ecodes.EV_KEY:
	if event.code == aBtn and event.value == 1:
		print("A clicked")
		#print(event.value)
		#GPIO.output(14, True)
		servo.value = -1
	if event.code == bBtn and event.value == 1:
		print("B Clicked")
		#GPIO.output(14, False)
		servo.value = 1
	if event.code == rTrig:
		print("Right Trigger")
		print(event.value)
		if event.value >= 5:
			servo.value = mapvalues(event.value, 0, 1023, -1, 0)
	if event.code == lTrig:
		print("Left Trigger")
		print(event.value)
		if event.value >= 5:
			servo.value = mapvalues(event.value, 0, 1023, 1, 0)
	if event.code == xBtn and event.value == 1:
		print("X Clicked")
	if event.code  == yBtn and event.value == 1:
		print("Y Clicked")

