#!/usr/bin/env python
# encoding: utf-8
"""
@author: binshao
@file: __init__.py.py
@time: 2018/10/22 11:52 PM
"""
import pluggy

# Marker to be imported and used in plugins (and for own implementations)
hookimpl = pluggy.HookimplMarker('eggsimple')
