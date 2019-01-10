from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Person!"

@app.route('/ncss', methods=['GET', 'POST'])
def greet_ncss():
    return "Hello, welcome to NCSS!"

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    print(request.values)
    name = request.values.get("name")
    return f'hi {name}!'

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    weather = float(request.values.get('weather'))
    if weather > 30:
        return "it's so hot"
    else:
        return f"the temperature is {weather}"

@app.route('/Good Morning', methods=['GET', 'POST'])
def morning():
    name = request.values.get("name")
    return f'Good Morning {name}'

@app.route('/feeling', methods=['GET', 'POST'])
def feeling():
    mood = request.values.get("mood")
    return f"I am also feeling {mood}"

if __name__ == '__main__':
    app.run()