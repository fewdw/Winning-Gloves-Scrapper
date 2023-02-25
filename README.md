# Winning-Gloves-Scrapper
SCRAPES [winning website](https://store.winning-usa.com/index.html)
You can either subscribe to receive emails or use my api

[Deployment](https://winning-api.herokuapp.com/)

## API Documentation

### Lace Gloves
#### Request
GET
```
https://winning-api.herokuapp.com/gloves/laces
```
#### Response
```
{
"colors": {
"black": "available",
"blue": "available",
"red": "available",
"white": "1mo"
},
"ounce": 8,
"price": 275,
"type": "laces"
}
```
Returns list of objects. Each Object represents a glove 8oz,10oz,12oz,14oz,16oz,18oz
In the object you get the ounce of the glove, the price, the type (laces) and the colors.
available means gloves are available. 1mo means it is 1 month backorder. 2mo 2 months backorder, etc...

### Velcro Gloves
#### Request
GET
```
https://winning-api.herokuapp.com/gloves/velcro
```
#### Response
```
{
"colors": {
"black": "available",
"blue": "available",
"red": "available",
"white": "1mo"
},
"ounce": 8,
"price": 275,
"type": "velcro"
}
```
Returns list of objects. Each Object represents a glove 8oz,10oz,12oz,14oz,16oz
In the object you get the ounce of the glove, the price, the type (laces) and the colors.
available means gloves are available. 1mo means it is 1 month backorder. 2mo 2 months backorder, etc...

### Open Headgear
#### Request
GET
```
https://winning-api.herokuapp.com/headgear/open
```
#### Response
```
"black": {
"2L": "2mo",
"3L": "available",
"large": "1mo",
"medium": "2mo"
}
```
Returns Dictionaries.
Color with each size and backorder months
You can also get the price and type
```
"price": 275
"type": "FG-2900"
```
Which are provided in the json

### Bar Headgear
#### Request
GET
```
https://winning-api.herokuapp.com/headgear/bar
```
#### Response
```
"black": {
"2L": "2mo",
"3L": "available",
"large": "1mo",
"medium": "2mo"
}
```
Returns Dictionaries.
Color with each size and backorder months
You can also get the price and type
```
"price": 490
"type": "FG-5000"
```
Which are provided in the json

### Cup
#### Request
GET
```
https://winning-api.herokuapp.com/cup
```
#### Response
```
"black": {
"2L": "2mo",
"3L": "available",
"large": "1mo",
"medium": "2mo"
}
```
Returns Dictionaries.
Color with each size and backorder months
You can also get the price and the type
```
"price": 200
"type": "CPS-500"
```
Which are provided in the json