#!/usr/bin/env python
# encoding: utf-8
"""
@author: binshao
@file: eggsample_spam.py
@time: 2018/10/25 11:52 AM
"""
import eggsample


@eggsample.hookimpl
def eggsample_add_ingredients(ingredients):
    if "egg" in ingredients:
        spam = ["lovely spam", "wonderous spam"]
    else:
        spam = ["splendiferous spam", "magnificent spam"]
    return spam


@eggsample.hookimpl
def eggsample_prep_condiments(condiments):
    try:
        del condiments['steak sauce']
    except KeyError:
        pass
    condiments['spam sauce'] = 42
    return f"Now this is what I call a condiments. tray!"
