#!/usr/bin/python
# -*- coding: utf-8 -*-
message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """                                                             X:<�ߊ�݋�#Ҍh�HĎ�>;�	+Zx������,��Ҋ�e��t;��YD��+o�����˃skN��hC0����Cٮh��뒎n��Ka#�q@�-(��j��0ٸ�t�-�����٦�W� """
h.update(blob)
print h.hexdigest()