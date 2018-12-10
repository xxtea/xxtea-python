# encoding: utf-8
from cffi import FFI
import sys
from os.path import join, dirname

__PATH = dirname(__file__)
__SOURCES = [join(__PATH, 'xxtea.c')]

ffi = FFI()
ffi.cdef('''
    void * xxtea_encrypt(const void * data, size_t len, const void * key, size_t * out_len);
    void * xxtea_decrypt(const void * data, size_t len, const void * key, size_t * out_len);
    void free(void * ptr);
''')
lib = ffi.verify('#include <xxtea.h>', sources = __SOURCES, include_dirs=[__PATH])

if sys.version_info < (3, 0):
    def __tobytes(v):
        if isinstance(v, unicode):
            return v.encode('utf-8')
        else:
            return v
else:
    def __tobytes(v):
        if isinstance(v, str):
            return v.encode('utf-8')
        else:
            return v

def encrypt(data, key):
    '''encrypt the data with the key'''
    data = __tobytes(data)
    data_len = len(data)
    data = ffi.from_buffer(data)
    key = ffi.from_buffer(__tobytes(key))
    out_len = ffi.new('size_t *')
    result = lib.xxtea_encrypt(data, data_len, key, out_len)
    ret = ffi.buffer(result, out_len[0])[:]
    lib.free(result)
    return ret

def decrypt(data, key):
    '''decrypt the data with the key'''
    data_len = len(data)
    data = ffi.from_buffer(data)
    key = ffi.from_buffer(__tobytes(key))
    out_len = ffi.new('size_t *')
    result = lib.xxtea_decrypt(data, data_len, key, out_len)
    ret = ffi.buffer(result, out_len[0])[:]
    lib.free(result)
    return ret

def decrypt_utf8(data, key):
    '''decrypt the data with the key to string'''
    return decrypt(data, key).decode('utf-8')

if __name__ == "__main__":
    text = "Hello World! \0你好，中国！"
    key = "1234567890"
    encrypt_data = encrypt(text, key)
    if sys.version_info < (3, 0):
        decrypt_data = decrypt(encrypt_data, key)
    else:
        decrypt_data = decrypt_utf8(encrypt_data, key)
    assert(text == decrypt_data)
