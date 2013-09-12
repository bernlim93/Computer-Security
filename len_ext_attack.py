import httplib, urlparse, sys
url = sys.argv[1]

# Your code to modify url goes here

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()