import sys
import dpkt
import socket

filename = str(sys.argv[1])
infile = open(filename)
pcap = dpkt.pcap.Reader(infile)

syndict = {}
synackdict = {}
suspicious = []

for ts, buf in pcap:
	try: 
		eth = dpkt.ethernet.Ethernet(buf)
		ip = eth.data
		if (type(ip.data) == dpkt.tcp.TCP):
			tcp = ip.data
			ipaddr = str(socket.inet_ntoa(ip.src))

			ack_flag = tcp.flags & dpkt.tcp.TH_ACK
			syn_flag = tcp.flags & dpkt.tcp.TH_SYN

			# SYN
			if (syn_flag and ack_flag <= 0):
				if (syndict.has_key(ipaddr)):
					syndict[ipaddr] += 1
				
				else:
					syndict[ipaddr] = 1

			#SYN-ACK
			if (syn_flag and ack_flag):
				if (synackdict.has_key(ipaddr)):
					synackdict[ipaddr] += 1
				
				else:
					synackdict[ipaddr] = 1

	except:
		#IGNORE MALFORMED DATA
		continue



print syndict
print synackdict

for key in syndict:
		if (not synackdict.has_key(key) or (syndict[key] > (synackdict[key] * 3))):
			print key


infile.close()