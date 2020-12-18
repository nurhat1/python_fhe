from he import key, encryption, decryption, computation
import gmpy2
from numpy.polynomial import polynomial as npp


print(key.complexroot(5))

print(encryption.inttopoly(257, 7))
print(encryption.inttopoly(18, 7))
# num - number, base = r (7) from example
print()

print(encryption.poly([5, 1, 5]))
print(key.newkey())
print(encryption.encrypttopoly(257, (key.newkey())))


print(gmpy2.digits.__doc__)
print(gmpy2.digits(257, 7))
print(gmpy2.digits(5, 2))
