import urllib.request

"""
"SimplerClient" operated at a higher level than "SimpleClient" due to it's use of URLs which cannot be found at socket level, and only occur at HTTP level.
"""

fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

for line in fhand:
    print(line.decode().strip())