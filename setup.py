import subprocess
from subprocess import Popen, PIPE, STDOUT

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
subprocess.run(["sudo apt-get purge firefox", "-y"])