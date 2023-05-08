import subprocess
import time

def run_cmd(command: str):
	process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	stdout, stderr = process.communicate()
	return stdout.decode("utf-8")


print(run_cmd("bluetoothctl connect 9C:AA:1B:D3:FF:03"))


def connect():



	while "Connection successful" not in run_cmd("bluetoothctl connect 9C:AA:1B:D3:FF:03"):
		print("not connected")
		time.sleep(1)
	print("connected")
	return True
