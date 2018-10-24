#!/usr/bin/env python
# encoding: utf-8
"""
@author: binshao
@file: lib.py
@time: 2018/10/23 12:02 AM
"""
import eggsample


@eggsample.hookimpl
def eggsample_add_ingredients():
    spices = ['salt', 'pepper']
    you_can_never_have_enough_eggs = ["egg", "egg"]
    ingredients = spices + you_can_never_have_enough_eggs
    return ingredients


@eggsample.hookimpl
def eggsample_prep_condiments(condiments):
    condiments["mint sauce"] = 1
