import re

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request

import utils
from utils import get_gloves_list, get_glove_prices_laces, get_glove_prices_velcro, get_inventory_table, \
    get_inventory_prices

app = Flask(__name__)


@app.route('/gloves/laces')
def get_laces_gloves():
    list_8_ounce_laces = get_gloves_list("8:finopt:0")
    list_10_ounce_laces = get_gloves_list("9:finopt:0")
    list_12_ounce_laces = get_gloves_list("10:finopt:0")
    list_14_ounce_laces = get_gloves_list("11:finopt:0")
    list_16_ounce_laces = get_gloves_list("12:finopt:0")
    list_18_ounce_laces = get_gloves_list("31:finopt:0")
    glove_prices_list = get_glove_prices_laces()
    return jsonify(
        [
            {
                "type": "laces",
                "ounce": 8,
                "price": glove_prices_list[0],
                "colors": {
                    "black": list_8_ounce_laces[0],
                    "red": list_8_ounce_laces[1],
                    "blue": list_8_ounce_laces[2],
                    "white": list_8_ounce_laces[3]
                }
            },
            {
                "type": "laces",
                "ounce": 10,
                "price": glove_prices_list[1],
                "colors": {
                    "black": list_10_ounce_laces[0],
                    "red": list_10_ounce_laces[1],
                    "blue": list_10_ounce_laces[2],
                    "white": list_10_ounce_laces[3]
                }
            },
            {
                "type": "laces",
                "ounce": 12,
                "price": glove_prices_list[2],
                "colors": {
                    "black": list_12_ounce_laces[0],
                    "red": list_12_ounce_laces[1],
                    "blue": list_12_ounce_laces[2],
                    "white": list_12_ounce_laces[3]
                }
            },
            {
                "type": "laces",
                "ounce": 14,
                "price": glove_prices_list[3],
                "colors": {
                    "black": list_14_ounce_laces[0],
                    "red": list_14_ounce_laces[1],
                    "blue": list_14_ounce_laces[2],
                    "white": list_14_ounce_laces[3]
                }
            },
            {
                "type": "laces",
                "ounce": 16,
                "price": glove_prices_list[4],
                "colors": {
                    "black": list_16_ounce_laces[0],
                    "red": list_16_ounce_laces[1],
                    "blue": list_16_ounce_laces[2],
                    "white": list_16_ounce_laces[3]
                }
            },
            {
                "type": "laces",
                "ounce": 18,
                "price": glove_prices_list[5],
                "colors": {
                    "black": list_18_ounce_laces[0],
                    "red": list_18_ounce_laces[1],
                    "blue": list_18_ounce_laces[2],
                    "white": list_18_ounce_laces[3]
                }
            }
        ]

    )


@app.route('/gloves/velcro')
def get_velcro_gloves():
    list_8_ounce = get_gloves_list("13:finopt:0", url="https://store.winning-usa.com/gloves-velcro.html")
    list_10_ounce = get_gloves_list("14:finopt:0", url="https://store.winning-usa.com/gloves-velcro.html")
    list_12_ounce = get_gloves_list("15:finopt:0", url="https://store.winning-usa.com/gloves-velcro.html")
    list_14_ounce = get_gloves_list("16:finopt:0", url="https://store.winning-usa.com/gloves-velcro.html")
    list_16_ounce = get_gloves_list("17:finopt:0", url="https://store.winning-usa.com/gloves-velcro.html")
    glove_prices_list = get_glove_prices_velcro()
    return jsonify(
        [
            {
                "type": "velcro",
                "ounce": 8,
                "price": glove_prices_list[0],
                "colors": {
                    "black": list_8_ounce[0],
                    "red": list_8_ounce[1],
                    "blue": list_8_ounce[2],
                    "white": list_8_ounce[3]
                }
            },
            {
                "type": "velcro",
                "ounce": 10,
                "price": glove_prices_list[1],
                "colors": {
                    "black": list_10_ounce[0],
                    "red": list_10_ounce[1],
                    "blue": list_10_ounce[2],
                    "white": list_10_ounce[3]
                }
            },
            {
                "type": "velcro",
                "ounce": 12,
                "price": glove_prices_list[2],
                "colors": {
                    "black": list_12_ounce[0],
                    "red": list_12_ounce[1],
                    "blue": list_12_ounce[2],
                    "white": list_12_ounce[3]
                }
            },
            {
                "type": "velcro",
                "ounce": 14,
                "price": glove_prices_list[3],
                "colors": {
                    "black": list_14_ounce[0],
                    "red": list_14_ounce[1],
                    "blue": list_14_ounce[2],
                    "white": list_14_ounce[3]
                }
            },
            {
                "type": "velcro",
                "ounce": 16,
                "price": glove_prices_list[4],
                "colors": {
                    "black": list_16_ounce[0],
                    "red": list_16_ounce[1],
                    "blue": list_16_ounce[2],
                    "white": list_16_ounce[3]
                }
            }
        ]

    )


@app.route('/headgear/open')
def get_open_headgear():
    open_headgear_list = get_inventory_table()
    price = get_inventory_prices()[0]

    return jsonify(
        {
            "type": "FG-2900",
            "price": price,
            "white":
                {
                    "medium": open_headgear_list[4],
                    "large": open_headgear_list[8],
                    "2L": open_headgear_list[12],
                    "3L": open_headgear_list[16]
                },
            "blue":
                {
                    "medium": open_headgear_list[5],
                    "large": open_headgear_list[9],
                    "2L": open_headgear_list[13],
                    "3L": open_headgear_list[17]
                },
            "black":
                {
                    "medium": open_headgear_list[6],
                    "large": open_headgear_list[10],
                    "2L": open_headgear_list[14],
                    "3L": open_headgear_list[18]
                },
            "red":
                {
                    "medium": open_headgear_list[7],
                    "large": open_headgear_list[11],
                    "2L": open_headgear_list[15],
                    "3L": open_headgear_list[19]
                }

        }
    )


@app.route('/headgear/bar')
def get_bar_headgear():
    bar_headgear_list = get_inventory_table()
    price = get_inventory_prices()[1]

    return jsonify(
        {
            "type": "FG-5000",
            "price": price,
            "white":
                {
                    "medium": bar_headgear_list[24],
                    "large": bar_headgear_list[28],
                    "2L": bar_headgear_list[32],
                    "3L": bar_headgear_list[36]
                },
            "blue":
                {
                    "medium": bar_headgear_list[25],
                    "large": bar_headgear_list[29],
                    "2L": bar_headgear_list[33],
                    "3L": bar_headgear_list[37]
                },
            "black":
                {
                    "medium": bar_headgear_list[26],
                    "large": bar_headgear_list[30],
                    "2L": bar_headgear_list[34],
                    "3L": bar_headgear_list[38]
                },
            "red":
                {
                    "medium": bar_headgear_list[27],
                    "large": bar_headgear_list[31],
                    "2L": bar_headgear_list[35],
                    "3L": bar_headgear_list[39]
                }

        }
    )


@app.route('/cup')
def get_cup():
    cup_headgear_list = get_inventory_table()
    price = get_inventory_prices()[2]
    return jsonify(
        {
            "type": "CPS-500",
            "price": price,
            "white":
                {
                    "color": "white",
                    "medium": cup_headgear_list[44],
                    "large": cup_headgear_list[48],
                    "2L": cup_headgear_list[52],
                    "3L": cup_headgear_list[56]
                },
            "blue":
                {
                    "medium": cup_headgear_list[45],
                    "large": cup_headgear_list[49],
                    "2L": cup_headgear_list[53],
                    "3L": cup_headgear_list[57]
                },
            "black":
                {
                    "medium": cup_headgear_list[46],
                    "large": cup_headgear_list[50],
                    "2L": cup_headgear_list[54],
                    "3L": cup_headgear_list[58]
                },
            "red":
                {
                    "medium": cup_headgear_list[47],
                    "large": cup_headgear_list[51],
                    "2L": cup_headgear_list[55],
                    "3L": cup_headgear_list[59]
                }

        }
    )


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api')
def api():
    return render_template("api.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/subscribed', methods=['POST'])
def display_form():
    # get email
    email = request.form.get("email")

    # get gloves
    lace = request.form.get("lace")
    velcro = request.form.get("velcro")

    # get gear
    open_choice = request.form.get("open")
    bar_choice = request.form.get("bar")
    cup_choice = request.form.get("cup")

    if email == "":
        return render_template("badform.html", MSG="please enter an email")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        return render_template("badform.html", MSG="please enter a valid email")

    if lace is None and velcro is None and open_choice is None and bar_choice is None and cup_choice is None:
        return render_template("badform.html", MSG="you must select something to be notified about")

    return render_template("subscribed.html", EMAIL=email, OPEN=open_choice, BAR=bar_choice,
                           CUP=cup_choice, LACE=lace, VELCRO=velcro)


if __name__ == '__main__':
    app.run()
