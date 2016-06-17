import os
import sys
from setuptools import setup

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = 'https://github.com/WALL-E/dubbo-telnet-py'
DOWNLOAD_BASEURL = "https://github.com/WALL-E/dubbo-telnet-py/raw/master/dist/"

try:
    major = sys.version_info.major
    minor = sys.version_info.minor
except AttributeError:
    major = sys.version_info[0]
    minor = sys.version_info[1]

DOWNLOAD_URL = DOWNLOAD_BASEURL + "dubbo_telnet-%s-py%s.%s.egg" % (VERSION, major, minor)

setup(name='dubbo_telnet',
    version=VERSION,
    description='Dubbo Telnet Client of python',
    long_description=open("README.PYPI").read(),
    keywords=(
        "dubbo, dubbo_telnet, telnet,"
    ),
    url=HOMEPAGE,
    download_url=DOWNLOAD_URL,
    author='zhangzheng',
    author_email='zhangzheng@qianbao.com',
    license='unlicense',
    packages=['dubbo_telnet'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Java Libraries",
    ],
    zip_safe=False
)
