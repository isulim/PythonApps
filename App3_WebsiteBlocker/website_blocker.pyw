"""
A Python script blocking certain websites in specified hours.
Script blocks sites by redirecting their URLs to localhost
by editing 'hosts' file.
"""

from platform import system
from time import sleep
from datetime import datetime

hosts_path = "hosts"

if system() == 'Windows':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = "/etc/hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if 8 <= datetime.now().hour <= 15:
        print("Working hours...")
        with open(hosts_path, 'r+') as hosts:
            content = hosts.read()
            for website in website_list:
                if website not in content:
                    hosts.write(redirect + "\t" + website + "\n")
    else:
        print("Relax time.")
        with open(hosts_path, 'r+') as hosts:
            lines = hosts.readlines()
            hosts.seek(0) # move cursor
            for line in lines:
                if not any (website in line for website in website_list):
                    hosts.write(line)
            hosts.truncate() # delete all after cursor
    sleep(60)