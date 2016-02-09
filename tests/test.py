# encoding: utf-8

import xxtea
import unittest

class TestXXTEA(unittest.TestCase):
    def test_xxtea1(self):
        text = b"Hello World! 你好，中国！"
        key = b"1234567890"
        encrypt_data = xxtea.encrypt(text, key)
        decrypt_data = xxtea.decrypt(encrypt_data, key)
        self.assertEqual(text, decrypt_data)
    def test_xxtea2(self):
        text = u"Hello World! 你好，中国！"
        key = u"1234567890"
        encrypt_data = xxtea.encrypt(text, key)
        decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
        self.assertEqual(text, decrypt_data)

if __name__ == '__main__':
    unittest.main()
