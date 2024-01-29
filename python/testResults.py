#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:45:13 2024

@author: raja
"""

import pandas as pd

input_file = 'new_file.csv'


csv_reader = pd.read_csv(input_file)

print(csv_reader.head(5))