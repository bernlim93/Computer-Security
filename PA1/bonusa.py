#!/usr/bin/python
# -*- coding: utf-8 -*-
message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """ 0�5L!ʠ����X"t����4B	�E�˦��~���k0?D��EE��f��x�����8���^LCy�'�R��CY"e���q(���ߗ_H��-8�H/4��I<����ו=�ۮ�%����: """
h.update(blob)
print h.hexdigest()