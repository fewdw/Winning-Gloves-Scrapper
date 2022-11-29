from flask import Flask, render_template, jsonify
from utils import get_gloves_list, get_glove_prices_laces, get_glove_prices_velcro

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
                "type": "8 ounce laces",
                "price": glove_prices_list[0],
                "color_black": list_8_ounce_laces[0],
                "color_red": list_8_ounce_laces[1],
                "color_blue": list_8_ounce_laces[2],
                "color_white": list_8_ounce_laces[3]
            },
            {
                "type": "10 ounce laces",
                "price": glove_prices_list[1],
                "color_black": list_10_ounce_laces[0],
                "color_red": list_10_ounce_laces[1],
                "color_blue": list_10_ounce_laces[2],
                "color_white": list_10_ounce_laces[3]
            },
            {
                "type": "12 ounce laces",
                "price": glove_prices_list[2],
                "color_black": list_12_ounce_laces[0],
                "color_red": list_12_ounce_laces[1],
                "color_blue": list_12_ounce_laces[2],
                "color_white": list_12_ounce_laces[3]
            },
            {
                "type": "14 ounce laces",
                "price": glove_prices_list[3],
                "color_black": list_14_ounce_laces[0],
                "color_red": list_14_ounce_laces[1],
                "color_blue": list_14_ounce_laces[2],
                "color_white": list_14_ounce_laces[3]
            },
            {
                "type": "16 ounce laces",
                "price": glove_prices_list[4],
                "color_black": list_16_ounce_laces[0],
                "color_red": list_16_ounce_laces[1],
                "color_blue": list_16_ounce_laces[2],
                "color_white": list_16_ounce_laces[3]
            },
            {
                "type": "18 ounce laces",
                "price": glove_prices_list[5],
                "color_black": list_18_ounce_laces[0],
                "color_red": list_18_ounce_laces[1],
                "color_blue": list_18_ounce_laces[2],
                "color_white": list_18_ounce_laces[3]
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
                "type": "8 ounce velcro",
                "price": glove_prices_list[0],
                "color_black": list_8_ounce[0],
                "color_red": list_8_ounce[1],
                "color_blue": list_8_ounce[2],
                "color_white": list_8_ounce[3]
            },
            {
                "type": "10 ounce velcro",
                "price": glove_prices_list[1],
                "color_black": list_10_ounce[0],
                "color_red": list_10_ounce[1],
                "color_blue": list_10_ounce[2],
                "color_white": list_10_ounce[3]
            },
            {
                "type": "12 ounce velcro",
                "price": glove_prices_list[2],
                "color_black": list_12_ounce[0],
                "color_red": list_12_ounce[1],
                "color_blue": list_12_ounce[2],
                "color_white": list_12_ounce[3]
            },
            {
                "type": "14 ounce velcro",
                "price": glove_prices_list[3],
                "color_black": list_14_ounce[0],
                "color_red": list_14_ounce[1],
                "color_blue": list_14_ounce[2],
                "color_white": list_14_ounce[3]
            },
            {
                "type": "16 ounce velcro",
                "price": glove_prices_list[4],
                "color_black": list_16_ounce[0],
                "color_red": list_16_ounce[1],
                "color_blue": list_16_ounce[2],
                "color_white": list_16_ounce[3]
            }
        ]

    )


@app.route('/headgear/open')
def get_open_headgear():
    return jsonify({"open headgear": "coming soon"})


@app.route('/headgear/bar')
def get_bar_headgear():
    return jsonify({"bar headgear": "coming soon"})


@app.route('/cup')
def get_cup():
    return jsonify({"cup": "coming soon"})


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
