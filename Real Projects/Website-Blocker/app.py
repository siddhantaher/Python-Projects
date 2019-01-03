from datetime import datetime as dt

import time
from io import open

host_temp="hosts"
# host_path='C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'
website_list=["www.facebook.com","facebook.com"]

while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,19):
        print('working hours')
        with open(host_temp,'r+') as newfile:
            content=newfile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    newfile.write(unicode(redirect+ " "+ website+"\n"))

    else:
        with open(host_temp, 'r+') as newfile:
            content = newfile.readlines()
            newfile.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    newfile.write(line)
            newfile.truncate()
            print('fun Hours')
    time.sleep(5)