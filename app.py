import json
import requests
from flask import Flask, render_template, url_for, redirect
from randfacts import get_fact

api_url = 'https://api.api-ninjas.com/v1/riddles'
API_KEY = 'bbc42566d6c19f9a84dd668b4a98ec48'
VIDEO = 'https://www.youtube.com/watch?v=hfmq2foLnvE'

app = Flask(__name__)


@app.route('/riddle')
def riddle():
    riddle_data = get_riddle()
    if riddle_data is not None:
        riddle = riddle_data[0]
        answer = riddle_data[1]
        return render_template('riddle.html', riddle=riddle, answer=answer)
    else:
        return "Error: Unable to retrieve riddle"


@app.route('/')
def index():
    return render_template('logo.html')


@app.route('/video')
def video():
    return render_template('video.html', video=VIDEO)


@app.route('/weather')
def weather():
    cluj_napoca = get_weather('Cluj-Napoca')
    grand_rapids = get_weather('Grand Rapids')
    return render_template('weather.html', cluj_napoca=cluj_napoca, grand_rapids=grand_rapids,
                           get_icon_url=get_icon_url)


@app.route('/funfact')
def funfact():
    fact = get_fact()
    return render_template('funfact.html', fact=fact)


def get_icon_url(icon):
    return f'http://openweathermap.org/img/w/{icon}.png'


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    temperature = round(data['main']['temp'])
    humidity = round(data['main']['humidity'])
    feels_like = round(data['main']['feels_like'])
    description = data['weather'][0]['description'].capitalize()
    icon = data['weather'][0]['icon']
    icon_filename = f"{icon}.png"
    return {
        'city': city,
        'temperature': temperature,
        'description': description,
        'icon': icon_filename,
        'feels_like': feels_like,
        'humidity': humidity,
    }


def get_riddle():
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            riddle = data[0]['question']
            answer = data[0]['answer']
            return riddle, answer
    return None, None



if __name__ == '__main__':
    app.run(debug=True)
