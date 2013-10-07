import urllib
from pymd5 import md5, padding
message = "testing"
token = md5(message).hexdigest()
m_len = 8 + len(message)
bits = (m_len + len(padding(m_len*8)))*8

h = md5(state=token.decode("hex"), count=bits)
k = md5(state=token.decode("hex"), count=bits)
killamessage = "&command3=DeleteAllFiles"
testmessage = "&command3=DeleteAllFilez"
h.update(killamessage)
k.update(testmessage)
killatoken = h.hexdigest()


print md5(message + padding(len(message)*8)).hexdigest()
print token


# from pymd5 import md5, padding
# a = open("guess.ps", "w") 
# out_file = """/Times-Roman findfont
# 12 scalefont
# setfont
# newpath
# 100 200 moveto
# (tingcten guesses 3) show"""
# a.write(out_file)
# a.close()

# hexvalue = md5(out_file).hexdigest()
# submit_file = """/Times-Roman findfont
# 12 scalefont
# setfont
# newpath
# 100 200 moveto
# (tingcten guesses 3) show
# /blob ("""
# collision = False
# while(not collision):
#     submit_file += padding(len('out_file')*8)
#     tmp = submit_file + ")"
#     print md5(tmp).hexdigest()
#     if(hexvalue == md5(tmp).hexdigest()):
#         print "FOUND A COLLISION!!!"
#         submit_file = tmp
#         collision = True
# b = open("submit.ps","w")
# b.write(tmp)
# b.close()
