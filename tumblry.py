import string
import webbrowser
import urllib.request
import os

a=input('link:')
b=a.replace("500","1280")
print(b)
Bol=b.split("/")
newpath = "D:\\batuhan"
if not os.path.exists(newpath):
    os.makedirs(newpath)
d='/batuhan/'+Bol[4]
urllib.request.urlretrieve(b,d)
