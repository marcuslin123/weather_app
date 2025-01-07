from flask import Flask, render_template
import requests
import config


app = Flask(__name__)

def get_weather(city):
    try:
        response = requests.get(config.URL)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except Exception as e:
        print(f"Error fetching weather: {e}")
    except KeyError as e:
        print(f"Data format error: Missing key {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return None


@app.route("/", methods=["GET", "POST"])
def home():
    city = config.DEFAULT_CITY
    weather_data = get_weather(city)

    return render_template("index.html", weather=weather_data)


if __name__ == "__main__":
    app.run(debug=True)