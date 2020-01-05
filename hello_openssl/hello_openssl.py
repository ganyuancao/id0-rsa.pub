# use pycryptodome instead of Crypto
# pip install pycryptodome

from Crypto.PublicKey import RSA 

c = 0x6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42

keyfile = open('priv').read()
key = RSA.import_key(keyfile)
d = key.d
n = key.n

m = pow(c, d, n)

print(hex(m))