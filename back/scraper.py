#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools, random, os, cchardet, lxml, traceback, re
from bs4 import BeautifulSoup
from lxml import html
import html as htmll
from datetime import datetime
from functools import partial
from random import randrange

def unescape(text):
    name_match = re.search('><h1>(.*)<span', str(text))

    if name_match:
        # Extract the matched group and replace HTML entities manually
        name = re.sub(r'&lt;', '<', name_match.group(1))
        name = re.sub(r'&gt;', '>', name)
        # Add more replacements if needed

        return name
    else:
        return ""

def extract_number(meh):
    # god, this is so dumb
    if "N/A" in meh:
        return ""

    currency = "eur"
    if "u00a3" in meh:
        meh.replace("u00a3", "")
        currency = "pnd" # pound sterling
    
    
    try:
        if currency == "eur":
            mehh = re.search(r'([0-9]*(\.|))*,[0-9]*', meh).group(0)
            mehh_arr = str(mehh).split(",")
            mehhh1 = mehh_arr[0].replace(".", "")
            strr=str(mehhh1)+"."+str(mehh_arr[1])
            
        else:
            mehh = re.search(r'([0-9]*(\.|))*\.[0-9]*', meh).group(0)
            mehh_arr = str(mehh).split(".")
            mehhh1 = mehh_arr[0].replace(",", "")
            strr=str(mehhh1)+"."+str(mehh_arr[1])
        return strr
    except Exception as e:
        print(e)
        return ""

def cm_parser(url, response):
    # Assuming 'response' is the object containing the HTTP response
    xml_content = response.text
    # Use regex to extract the HTML part from the XML
    html_match = re.search(r'<html.*?</html>', xml_content, re.DOTALL)
    html_content = ""
    if html_match:
        html_content = html_match.group(0).replace("\\", "")
    else:
        return []
    title_raw = re.findall(r'<div class="flex-grow-1">(.*?)</div>', html_content)[0]
    title = re.findall(r'<h1>(.*?)<span', title_raw)[0]
    infos = re.findall(r'<dd class="col-6 col-xl-7">(.*?)</dd>', html_content)
    prices_raw = infos[-5:]
    prices = []
    for price in prices_raw :
        prices.append(extract_number(price))
    rarity = re.findall(r"data-original-title=\"(.*?)\"", infos[0])
    expansion = re.findall(r"aria-label=\"(.*?)\"", infos[1])
    img = re.findall(r"<img src=\"(.*?)\" alt=\"", html_content)
    true_price_raw = re.findall(r"<div id=\"articleRow(.*?)<div id=\"articleRow", html_content)
    try: 
        true_price_raw_one = true_price_raw[0]
        true_price_raw_one_only_price = re.findall(r"<div class=\"price-container(.*?)</div", true_price_raw_one)[0]
        true_price_graw = re.findall(r"color-primary small text-end text-nowrap fw-bold \">(.*?)<", true_price_raw_one_only_price)[0]
        true_price = extract_number(true_price_graw)
    except:
        true_price = ""
    prices.append(true_price)
    return [title, prices, rarity, expansion, img[1]]
