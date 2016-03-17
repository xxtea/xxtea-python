import sys
from setuptools import setup
if sys.version_info < (2, 6):
    print >> sys.stderr, 'error: python 2.6 or higher is required, you are using %s' %'.'.join([str(i) for i in sys.version_info])
    sys.exit(1)

tests_require = ['nose']
if sys.version_info < (2, 7):
    tests_require.append('nose_extra_tools')

setup(
    name = 'xxtea-py',
    version = '1.0.2',
    description = 'XXTEA is a fast and secure encryption algorithm. This is a XXTEA library for Python. It is based on CFFI, so it is fast and support both cpython and pypy.',
    long_description = open('README.rst', 'r').read(),
    keywords = 'xxtea crypt encrypt decrypt xtea tea',
    author = 'Ma Bingyao',
    author_email = 'mabingyao@gmail.com',
    url = 'https://github.com/xxtea/xxtea-python',
    license = 'MIT',
    platforms = 'any',
    packages = ['xxtea'],
    include_package_data = False,
    zip_safe = False,
    package_data = {'xxtea': ['*.py', '*.c', '*.h']},
    setup_requires = ['cffi', 'nose'],
    test_suite = 'nose.collector',
    tests_require = tests_require,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent']
)
