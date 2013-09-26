#!/usr/bin/python
# -*- coding: utf-8 -*-
message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """Â‹ 0°5L!Ê †ŒÀíX"tîÇğâ4B	‹EË¦óÄ~Œ•ók0?D­¯EEó£úfêıxº¶¯É¨8ìñÊ^LCyó'¸Rô¼CY"eŸ„Ûq(­Åàß—_H·Ï-8—H/4ºûI<£Üı××•=‡Û®ó%Šèíø: """
h.update(blob)
print h.hexdigest()