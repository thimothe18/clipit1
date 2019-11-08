import subprocess
from subprocess import Popen, PIPE, STDOUT
import sys
#subprocess.call(["ipconfig"])
# subprocess.run(["sudo apt update"])
# subprocess.run(["sudo apt install python3-pip"])
# subprocess.run(["pip3 install selenium"])
# subprocess.run(["pip3 install clipboard"])
# subprocess.run(["pip3 install pymongo"])
# subprocess.run(["pip3 install keyboard"])
# subprocess.run(["pip3 install boto3"])
# subprocess.run(["pip3 install streamlink"])
# subprocess.run(["wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz"])
# subprocess.run(["tar -xvzf geckodriver-v0.26.0-linux64.tar.gz"])
# subprocess.run(["chmod +x geckodriver"])
# subprocess.run(["sudo apt-get install firefox"])
packages = ["sudo apt update", 
"sudo apt install python3-pip", 
"pip3 install selenium", 
"pip3 install clipboard", 
"pip3 install pymongo",
"pip3 install boto3",
"pip3 install streamlink",
"pip3 install keyboard",
"wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz",
"tar -xvzf geckodriver-v0.26.0-linux64.tar.gz",
"chmod +x geckodriver",
"sudo apt-get install firefox"
 ]

def install(package):
    subprocess.call([sys.executable, package])
for package in packages:
	install(package)