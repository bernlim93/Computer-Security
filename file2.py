#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          kkΫ�Ќ���f���\���C�ve5>>������ՃZ�QJ�E-l��#]��C"����+٥��6\aP��,�^����K�x>5M���-�za&��gn_�I���]��m����wңJ��L�"""
from hashlib import sha256
print sha256(blob).hexdigest()