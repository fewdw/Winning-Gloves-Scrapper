import requests as requests
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import re

def get_gloves_list(form_code, url="https://store.winning-usa.com/pro-gloves.html"):
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    list = []
    select = doc.find("select", {"name": form_code})
    option = select.findChildren("option", recursive=False)
    for o in option:
        if o['value'] != '(Color);n':
            if len(str(o['value'])) < 6:
                list.append("available")
            else:
                backorder = int(re.search(r'\d+', str(o['value'])).group())
                list.append(f"{backorder}mo")
    return list


def get_glove_prices_laces():
    url = "https://store.winning-usa.com/pro-gloves.html"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    list = []
    prices = doc.findAll("span", {"class": "saleprice"})
    for i in range(6):
        # find integer in string :D
        price = int(re.search(r'\d+', str(prices[i])).group())
        list.append(price)
    return list


def get_glove_prices_velcro():
    url = "https://store.winning-usa.com/gloves-velcro.html"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    list = []
    prices = doc.findAll("span", {"class": "saleprice"})
    for i in range(5):
        # find integer in string :D
        price = int(re.search(r'\d+', str(prices[i])).group())
        list.append(price)
    return list