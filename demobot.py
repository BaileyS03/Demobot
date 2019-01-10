from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Person!"

@app.route('/ncss')
def greet_ncss():
    return "Hello, welcome to NCSS!"

@app.route('/greet')
def greet_person():
    name = request.values.get("name")
    return f'hi {name}!'

@app.route('/weather')
def weather():
    weather = float(request.values.get('weather'))
    if weather > 30:
        return "it's so hot"
    else:
        return f"the temperature is {weather}"

if __name__ == '__main__':
    app.run()