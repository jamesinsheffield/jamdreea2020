from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/flights-out')
def flights_out():
    return render_template('flights-out.html')

@app.route('/flights-return')
def flights_return():
    return render_template('flights-return.html')

if __name__ == "__main__":
    app.run()
