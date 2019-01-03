import urllib, os
link = "http://python.org"
print "opening url:", link
site = urllib.urlopen(link)
meta = site.info()
print "Content-Length:", meta.getheaders("Content-Length")[0]

fa = open("outs.txt", "w+")
print "faile on disk:",len(fa.read())
fa.close()


fa = open("outs.txt", "w+")
fa.write(site.read())
site.close()
fa.close()

fa = open("outs.txt", "r+")
print "faile on disk afater download:",len(fa.read())
fa.close()

print "os.stat().st_size returns:", os.stat("outs.txt").st_size
