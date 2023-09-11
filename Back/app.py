from flask import Flask
from flask_cors import CORS
api = Flask(__name__)
CORS(api)

students =[
    {"name":"waga","age":12},
    {"name":"baga","age":10}
]

@api.route('/')
def hello():
    return students


if __name__ == '__main__':
    api.run(debug=True)