# 877b09d9754153c4532c745d638868ba

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "877b09d9754153c4532c745d638868ba"

@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:

                weather = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "icon": data["weather"][0]["icon"]
                }

            else:
                error = "City not found!"

        except Exception as e:
            error = "Something went wrong!"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
