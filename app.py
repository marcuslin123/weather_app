from flask import Flask
import config


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my web app!"


if __name__ == "__main__":
    app.run(debug=True)

# test commit