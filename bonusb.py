message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """Â‹ 0°5L!Ê †ŒÀíX"ôîÇğâ4B	‹EË¦óÄ~Œ•ók0?D­/EEó£úfêıxº¶¯I¨8ìñÊ^LCyó'¸Rô¼CY"e„Ûq(­Åàß—_H·Ï-8—H/4ºûI<£\ı××•=‡Û®ó%Šhíø:"""
h.update(blob)
print h.hexdigest()