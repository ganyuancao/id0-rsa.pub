#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
plaintext = 'id0-rsa.pub'.encode('utf-8')
hash1 = hashlib.sha256(plaintext).hexdigest().encode('utf-8')
hash2 = hashlib.md5(hash1).hexdigest()

print(hash2)
