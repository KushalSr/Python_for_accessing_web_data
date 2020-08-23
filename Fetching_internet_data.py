import urllib.request

webUrl = urllib.request.urlopen("http://www.google.com")

print("Result code: " + str(webUrl.getcode()))
data = webUrl.read()
print(data)

