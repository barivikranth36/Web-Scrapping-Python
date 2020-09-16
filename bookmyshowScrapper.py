import re
import urllib.request

city = input("Enter your city name = ").strip().lower()
url = 'https://in.bookmyshow.com/'+city+'/movies'
theaterUrl = 'https://in.bookmyshow.com/'+city+'/cinemas'

#Request for webpage with User-Agent as Mozilla/5.0         default User-Agent = Python-urllib/3.0
req = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req)

reqth = urllib.request.Request(theaterUrl, headers={"User-Agent": "Mozilla/5.0"})
thhtml = urllib.request.urlopen(reqth).read()

result = re.findall(r'<div class="card-title">(.*?)</div>', str(html))
thResult = re.findall(r'<div class="__cinema-text">(.*?)</div>', str(thhtml))

i = 1
for r in result:
    mname = r[28:]
    mname = mname[:mname.find('<')]
    print(str(i)+'.', mname)
    i += 1

print()
print("**************************Cineplex***********************************")
print()

i = 1
for mname in thResult:
    mname = mname[mname.find('>') + 1:]
    mname = mname[:mname.find('<')]
    print(str(i)+'.', mname)
    i += 1
