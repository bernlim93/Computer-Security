#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """           GaD�^����[�iXq ���4j:�J��֝ܪ��4��B�	��L���3B=�G��L1?}HR�t_�DG����g1�}"�hZ
�� P7`h�ӓ"X���;�@LT0V�m���7t������\""""""
from hashlib import sha256
print sha256(blob).hexdigest()