#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:19:07 2022

@author: roxy
"""

def clean_text(str_in):
    import re
    sent_a_clean = re.sub('[^A-Za-z]+', " ", str_in.lower())
    return sent_a_clean


def clean_file(file):
    f = open(file, 'r', encoding = 'utf-8')
    text = f.read()
    text = clean_text(text)
    f.close
    return text

print(clean_text("this $%^&#@ IS AN example!!!"))


path = '/Users/roxy/desktop/5067/lecture/data/'

def file_reader(path_in):
    import os
    import pandas as pd
    data = pd.DataFrame()
    for root, dirs, files in os.walk(path, topdown = False):
        for name in files:
            try:
                label = root.split("/")[-1:][0]
                file_path = root + "/" + name
                text = clean_file(file_path)
                data = data.append(
                    {'label': label, 'body':text}, ignore_index = True)
            except:
                print(file_path)
                pass
    return data

data = file_reader(path)
