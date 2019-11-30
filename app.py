from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'JAMDREEA2020'

if __name__ == "__main__":
    app.run()
