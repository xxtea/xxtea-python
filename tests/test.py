# encoding: utf-8
import sys
import xxtea
import unittest

class TestXXTEA(unittest.TestCase):
    def test_xxtea1(self):
        if sys.version_info < (3, 0):
            text = "Hello World! 你好，中国！"
            key = "1234567890"
        else:
            text = "Hello World! 你好，中国！".encode("utf-8")
            key = "1234567890".encode("utf-8")
        encrypt_data = xxtea.encrypt(text, key)
        decrypt_data = xxtea.decrypt(encrypt_data, key)
        self.assertEqual(text, decrypt_data)
    def test_xxtea2(self):
        if sys.version_info < (3, 0):
            text = "Hello World! 你好，中国！".decode("utf-8")
            key = "1234567890".decode("utf-8")
        else:
            text = "Hello World! 你好，中国！"
            key = "1234567890"
        encrypt_data = xxtea.encrypt(text, key)
        decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
        self.assertEqual(text, decrypt_data)

if __name__ == '__main__':
    unittest.main()
