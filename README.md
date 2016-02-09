# XXTEA for Python

[![Build Status](https://travis-ci.org/xxtea/xxtea-python.svg?branch=master)](https://travis-ci.org/xxtea/xxtea-python)

## Introduction

XXTEA is a fast and secure encryption algorithm. This is a XXTEA library for Python.

It is different from the original XXTEA encryption algorithm. It encrypts and decrypts raw binary data instead of 32bit integer array, and the key is also the raw binary data.

## Installation

```sh
pip install xxtea-py
```

## Usage

Python2:
```python
import xxtea
text = "Hello World! 你好，中国！"
key = "1234567890"
encrypt_data = xxtea.encrypt(text, key)
decrypt_data = xxtea.decrypt(encrypt_data, key)
print(text == decrypt_data);
```

Python3:
```python
import xxtea
text = b"Hello World! 你好，中国！"
key = b"1234567890"
encrypt_data = xxtea.encrypt(text, key)
decrypt_data = xxtea.decrypt(encrypt_data, key)
print(text == decrypt_data);
```
