#!/usr/bin/env python
# encoding: utf-8
"""
@author: binshao
@file: setup.py
@time: 2018/10/25 12:00 PM
"""
from setuptools import setup

setup(
    name="eggsample-spam",
    install_requires="eggsample",
    entry_points={"eggsample": ["spam = eggsample_spam"]},
    py_modules=["eggsample_spam"],
)
