message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """ 0�5L!ʠ����X"�����4B	�E�˦��~���k0?D�/EE��f��x���I�8���^LCy�'�R��CY"e��q(���ߗ_H��-8�H/4��I<�\��ו=�ۮ�%�h��:"""
h.update(blob)
print h.hexdigest()