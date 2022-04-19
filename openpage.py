import urllib.request

webUrl = urllib.request.urlopen('https://maximus.design/sakura')

print("result code: " + str(webUrl.getcode()))

