XXTEA for Python
================

.. image:: https://travis-ci.org/xxtea/xxtea-python.svg?branch=master
    :target: https://travis-ci.org/xxtea/xxtea-python

Introduction
------------

XXTEA is a fast and secure encryption algorithm. This is a XXTEA library for Python.

It is different from the original XXTEA encryption algorithm. It encrypts and decrypts raw binary data instead of 32bit integer array, and the key is also the raw binary data.

Installation
------------

::

    pip install xxtea-python


Usage
-----------

Python2:

.. code-block:: python

    import xxtea
    text = "Hello World! 你好，中国！"
    key = "1234567890"
    encrypt_data = xxtea.encrypt(text, key)
    decrypt_data = xxtea.decrypt(encrypt_data, key)
    print(text == decrypt_data);


Python3:

.. code-block:: python

    import xxtea
    text = "Hello World! 你好，中国！"
    key = "1234567890"
    encrypt_data = xxtea.encrypt(text, key)
    decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
    print(text == decrypt_data);
