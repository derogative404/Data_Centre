import urllib2
response = urllib2.urlopen('https://wordpress.org/plugins/about/readme.txt')
data = response.read()