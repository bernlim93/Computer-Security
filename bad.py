#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          ���HE7�	Y��Y5�M�խ#2B�n�Ŵܱ��+�}g"XśU��ݨUc���O�2s��kcsq�}K����W8�\1&r����F��ET�шKUW�x�Y�@�m��\"�� """
from hashlib import sha256
if sha256(blob).hexdigest() == '1506c3071ba767b38c2311a046009bc200f30015860fd52feba3fade653c30a3':
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
