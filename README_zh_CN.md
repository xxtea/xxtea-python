# XXTEA 加密算法的 Python 实现

[![Build Status](https://travis-ci.org/xxtea/xxtea-python.svg?branch=master)](https://travis-ci.org/xxtea/xxtea-python)
[![PyPI](https://img.shields.io/pypi/v/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/l/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/pyversions/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/implementation/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/status/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/dm/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/dw/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)
[![PyPI](https://img.shields.io/pypi/dd/xxtea-python.svg)](https://pypi.python.org/pypi/xxtea-python)

## 简介

XXTEA 是一个快速安全的加密算法。本项目是 XXTEA 加密算法的 Python 实现。

它不同于原始的 XXTEA 加密算法。它是针对原始二进制数据类型进行加密的，而不是针对 32 位 int 数组。同样，密钥也是原始二进制数据类型。

## 安装

```sh
pip install xxtea-python
```

## 使用

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
text = "Hello World! 你好，中国！"
key = "1234567890"
encrypt_data = xxtea.encrypt(text, key)
decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
print(text == decrypt_data);
```
