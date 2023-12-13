from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Здесь вы можете взаимодействовать с SWAPI и получить нужную информацию
    # Например, получим информацию о первых 5 персонажах
    response = requests.get('https://swapi.dev/api/people/')
    characters = response.json()['results'][:5]

    return render_template('index.html', characters=characters)

if __name__ == '__main__':
    app.run(debug=True)
