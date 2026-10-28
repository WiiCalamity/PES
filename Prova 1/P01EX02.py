#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 2
"""

import time
import os
def clear():
        os.system("cls" if os.name=="nt" else "clear")

for i in range(10,-1,-1):
        print(i)
        time.sleep(1)
        clear()
print("Fogo!")