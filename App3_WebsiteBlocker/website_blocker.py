from platform import system
from time import sleep
from datetime import datetime

hosts_path = ""

if system() == 'Windows':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = "/etc/hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if 8 <= datetime.now().hour <= 16:
        print("Working hours...")
    else:
        print("Relax time.")
    sleep(10)