#!/usr/bin/env python
from setuptools import setup


setup(
    name='scrapy-tg-export',
    version='0.0.1',
    packages=['scrapy_tg_export'],
    install_requires=[
        'python-telegram-bot',
    ],
    license='MIT license',
    description="Send Scrapy items to Telegram chat",
    url='https://github.com/zergey/scrapy-tg-export',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
