# -*- coding: utf-8 -*-
"""Webscrapping

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L-z3tXzwZszN5FWZUt3Scu6Rn2ow7YI4
"""

import requests 
from bs4 import BeautifulSoup

url="https://pricebaba.com/refrigerators/pricelist/all-refrigerators-sold-in-india"

response=requests.get(url)

response

cam=BeautifulSoup(response.text)

cam

ref=cam.select('.ellips-line-ell-2')

ref

fridge_name=[]

for item in ref:
  fridge_name.append(item.text)
  link="https://pricebaba.com/"+item["href"]

fridge_name

price=cam.select('.d-block .txt-al-c')

price

fridge_price=[]

for item in price:
  fridge_price.append(item.text)

fridge_price

vfm=cam.select('.vfm__txt')

vfm

fridge_vfm=[]

for item in vfm:
  fridge_vfm.append(item.text)

fridge_vfm

import pandas as pan

san=pan.DataFrame(fridge_name,columns=['fridge name'])

san

san['price']=fridge_price

san

san['vfm']=fridge_vfm

san

