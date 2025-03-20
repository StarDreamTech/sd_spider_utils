from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name="spider_utils",
    version="1.0.0",
    description="爬虫工具包，写爬虫更快！！！",
    long_description=long_description,
    author="星梦",
    author_email="cpython666@gmail.com",
    url="https://space.bilibili.com/1909782963",
    install_requires=[],
    license="MIT License",
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
