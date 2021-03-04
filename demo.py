
import requests
import django
import smtp
import dateutil
import yaml

web = requests.get('http://www.google.com')

print(web.status_code)
