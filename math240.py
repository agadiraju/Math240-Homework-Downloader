import urllib2
import urllib
import sys
import re
from BeautifulSoup import BeautifulSoup

urllib.urlretrieve("http://www.math.upenn.edu/~ryblair/Math240F12/papers/Homework.pdf", "Homework.pdf")
response = urllib2.urlopen("http://www.math.upenn.edu/~moose/240F2012.html")

page = response.read()
parsed = BeautifulSoup(page)

links = parsed.findAll('a', href=True)
for link in links:
   if "homework" in str(link):
      heads = "http://www.math.upenn.edu"
      mini_link = str(link['href'])
      if "/" in mini_link:
         result = re.findall('[^\/]+$', mini_link)
         urllib.urlretrieve(heads + mini_link, result[0])
      else:
         urllib.urlretrieve(heads + "/~moose/" + mini_link, mini_link)

request = urllib2.urlopen("http://www.math.upenn.edu/~ryblair/Math240F12/index.html")
page2 = request.read()
second = BeautifulSoup(page2)

links2 = second.findAll('a', href=True)
for link in links2:
   if "Slides" in str(link):
      heads = "http://www.math.upenn.edu/~ryblair/Math240F12/"
      mini_link=str(link['href'])
      result = re.findall('[^\/]+$', mini_link)
      urllib.urlretrieve(heads + mini_link, result[0])
