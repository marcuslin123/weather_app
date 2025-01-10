from flask import Flask, render_template, request
import requests
import config


app = Flask(__name__)

def get_weather(city):
    try:
        city = city.strip().title()

        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}&units=imperial", config.DEFAULT_URL)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "temp_min": round(data["main"]["temp_min"]),
            "temp_max": round(data["main"]["temp_max"]),
            "description": data["weather"][0]["description"].title()
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
    if request.method == "POST":
        city = request.form.get("city", "Berkeley").strip().title()
    else:
        city = "Berkeley"

    weather_data = get_weather(city)

    return render_template("index.html", weather=weather_data)


if __name__ == "__main__":
    app.run(debug=True)