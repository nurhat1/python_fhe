'''
Functioт for decrypting.
'''


def decrypt(func, key):
    '''

    :param func: labda function obtained from the server
    :param key: secret key
    :return: decrypted value
    '''
    return func(key[0])
