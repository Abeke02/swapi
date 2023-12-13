from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def get_film_titles(film_urls):
    film_titles = []
    for film_url in film_urls:
        response = requests.get(film_url)
        if response.status_code == 200:
            film_info = response.json()
            film_titles.append(film_info['title'])
    return film_titles

def get_planet_info(planet_url):
    response = requests.get(planet_url)
    if response.status_code == 200:
        planet_info = response.json()
        return planet_info
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result_for_planet/<path:planet_url>')
def result_for_planet(planet_url):
    planet_info = get_planet_info(planet_url)
    
    if planet_info:
        return render_template('result_for_planet.html', planet_info=planet_info)
    else:
        return render_template('result_for_planet.html', error='Ошибка запроса')


@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        x = int(request.form['x'])
        response = requests.get(f'https://swapi.dev/api/people/{x}/')

        if response.status_code == 200:
            character = response.json()
            planet_info = get_planet_info(character['homeworld'])
            film_titles = get_film_titles(character['films'])
            return render_template('result.html', character=character, planet_info=planet_info, film_titles=film_titles)
        else:
            return render_template('result.html', error='Ошибка запроса')

    except ValueError:
        return render_template('index.html', error='Пожалуйста, введите корректное число.')

@app.route('/result')
def result():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
