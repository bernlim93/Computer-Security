#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """           GaD�^����[�iX� ���4j:�J��֝ܪ��4��B�	&�L���3B=�G���1?}HR�t_�DG����g1�}"=hZ
�� P7`h�ӓ"X���;�@LT�V�m���7t��y���\
  """
from pymd5 import md5
message = "this should make the same hash"
h = md5(message)
print h.hexdigest()
h.update(blob)
print h.hexdigest()
