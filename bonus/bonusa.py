#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          �<���L�n$d���e��}����y�,�.��!�������;<X��׿�-""�[Hto�V�M�F|j���%����4Z�/zAb�W��Yq]�P޶-(�[�ѯ�}{�
�����6�N�$��J """
from pymd5 import md5
message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
h.update(blob)
print h.hexdigest()