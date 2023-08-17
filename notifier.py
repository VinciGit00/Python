import time
import requests
import subprocess
from datetime import datetime

link = "https://blockchain.info/tobtc?currency=USD&value=1"
r = requests.get(link)

myobj = datetime.now()


CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

if myobj.minute == 00:
    value = round(1/float(r.text))
    notify("Value of the bitcoin", f"1 bitcoin value is {value} $")
    time.sleep(5)
