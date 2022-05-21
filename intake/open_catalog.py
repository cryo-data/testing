#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

from intake import open_catalog

cat = open_catalog("/home/adrien/UZH/cryo-data/testing/intake/catalog_example3.yaml")

list(cat)

data = cat.states

cat.states.read()
