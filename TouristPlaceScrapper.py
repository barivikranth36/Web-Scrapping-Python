#Holidify.com

import re
import urllib.request

place = input("Enter your destination = ").strip().lower()

url = 'https://www.holidify.com/places/'+place+'/sightseeing-and-things-to-do.html#packageModal'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
htm = urllib.request.urlopen(req).read()

result = re.findall(r'<h3 class="card-heading">(.*?)</h3>', str(htm))
for x in result:
        print(x)
