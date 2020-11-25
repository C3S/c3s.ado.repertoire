#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society_docker

"""
Set German language translatable
"""

from proteus import Model

DEPENDS = [
    'upgrade',
]


def generate():
    Language = Model.get('ir.lang')
    german_language, = Language.find([('code', '=', 'de_DE')])
    german_language.translatable = True
    german_language.save()
