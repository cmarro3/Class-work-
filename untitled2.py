#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:17:08 2020

@author: christophermarroquin
"""
import pandas as pd

def CTA():
    s = pd.read_csv('nasdaq-data-2019.csv', names=['Date','Open','High','Low','Close','AdjClose','Volume'], skiprows=[0])
    print(s)
CTA()