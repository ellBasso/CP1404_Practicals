from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<H1>Hello World!</h1>'


@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    try:
        result = (float(celsius) * float(9 / 5)) + float(32)
        return f"""<h1>Fahrenheit: {result}</h1>
        <h1>Celsius: {celsius}</h1>"""
    except:
        return "Please enter a valid number"


if __name__ == '__main__':
    app.run()
