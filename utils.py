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


def get_inventory_table():
    url = "https://store.winning-usa.com/inventory.html"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    list = []
    rows = doc.findAll("td", {"style": "width: 20%; height: 18px; text-align: center;"})
    for i in range(60):
        if (len(rows[i].text) < 2):
            list.append("available")
        else:
            list.append(rows[i].text)
    return list


def get_inventory_prices():
    headgear_url = "https://store.winning-usa.com/headgear.html"
    result1 = requests.get(headgear_url).text
    doc1 = BeautifulSoup(result1, "html.parser")

    cup_url = "https://store.winning-usa.com/cup-protector.html"
    result2 = requests.get(cup_url).text
    doc2 = BeautifulSoup(result2, "html.parser")

    prices1 = doc1.findAll("span", {"class": "saleprice"})
    prices2 = doc2.findAll("span", {"class": "saleprice"})

    open_price = int(re.search(r'\d+', str(prices1[0])).group())
    bar_price = int(re.search(r'\d+', str(prices1[1])).group())
    cup_price = int(re.search(r'\d+', str(prices2[0])).group())

    return [open_price, bar_price, cup_price]
