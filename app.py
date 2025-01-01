from flask import Flask
import config


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)