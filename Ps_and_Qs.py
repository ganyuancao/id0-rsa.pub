# RSA - low entropy prime number 
# paper reference: https://factorable.net/weakkeys12.extended.pdf
# N = p * q for RSA keys
# N_1 = p * q_1, N_2 = p * q_2 for key_1, key_2 
# Find p with p = gcd(N_1, N_2)

from Crypto.PublicKey import RSA
from Crypto.Util import number

ciphertext = 0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da

key1 = RSA.import_key(open('key1.pub').read())
key2 = RSA.import_key(open('key2.pub').read())

n1 = key1.n
n2 = key2.n 

e = key1.e

p = number.GCD(n1,n2)
q1 = n1 // p
q2 = n2 // 1

phi = (p - 1) * (q1 - 1)
d = number.inverse(e, phi)

plaintext = pow(ciphertext, d, n1)
print(hex(plaintext))