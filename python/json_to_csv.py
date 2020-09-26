#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_json(r'PATH/TO/file.json')
df.to_csv('output_file_name.csv')
