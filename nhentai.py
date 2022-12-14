import shutil
import requests
from bs4 import BeautifulSoup
from pySmartDL import SmartDL
from time import sleep
import sys , getopt
import os
import img2pdf
dest='./downloads/'
try:
	code = sys.argv[1]
except:
    code = input("your code :")
      
print("the item youre searching for is :" "https://nhentai.to/g/" + code)
url = "https://nhentai.website/g/"
source= requests.get(url + code ).text
soup = BeautifulSoup(source, 'lxml')
for i in soup.find_all("img" , {"is" : "lazyload-image"}):
	print(i["data-src"])
	obj = SmartDL(i["data-src"] ,dest=dest)
	if obj.start():
    		continue
imgs = []
for fname in os.listdir(dest):
	if not fname.endswith(".jpg"):
		continue
	path = os.path.join(dest, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open("nhentai.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))

#os.remove("name.pdf")
shutil.rmtree(dest)
#removes the downloads folder
