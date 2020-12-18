from he import key, encryption, decryption, computation
import gmpy2
from numpy.polynomial import polynomial as npp


print(key.complexroot(5))

print(f"inttopoly(257, 7): {encryption.inttopoly(257, 7)}")
print(f"inttopoly(18, 7): {encryption.inttopoly(18, 7)}")
# num - number, base = r (7) from example
print("\n ----------------- \n")

key_ = key.newkey(sec=2)
print(f"key: {key_}")
# print(encryption.poly([5, 1, 5]))
# print(f"new key: {key.newkey(sec=2)}")
# print(f"encrypt to lambda: {encryption.encrypttolambda(257, (key.newkey(sec=2)))}")
encr1 = encryption.encrypttolambda(257, key_)
encr2 = encryption.encrypttolambda(18, key_)
add_res = computation.add(encr1, encr2)
multi_res = computation.multi(encr1, encr2)
div_res = computation.div(encr1, encr2)
print(f"add_res: {add_res(key_[1])}")
print(f"multi_res: {multi_res(key_[1])}")
print(f"div_res: {div_res(key_[1])}")


# print(gmpy2.digits.__doc__)
# print(gmpy2.digits(257, 7))
# print(gmpy2.digits(5, 2))
