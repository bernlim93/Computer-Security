#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          kkΫ�Ќ���f��\���C�ve5>>������ՃZ�QʘE-l��#]��C�����+٥��6\aP��,�^�D��K�x>5M���-�za&��gn_�I�d�]��m����wңJW�L�"""
from hashlib import sha256
print sha256(blob).hexdigest()