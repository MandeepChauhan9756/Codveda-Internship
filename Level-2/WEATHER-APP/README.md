# Weather API App 🌦

This is a simple weather application made using Python and Flask.  
The app connects with the OpenWeather API and shows live weather information of any city entered by the user.

I created this project to practice:
- API Integration
- Flask
- Handling JSON data
- Frontend + Backend connection

---

## Features

- Search weather using city name
- Shows temperature
- Displays humidity and wind speed
- Weather condition with icon
- Error handling for invalid cities
- Simple and clean UI

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Requests Library
- OpenWeather API

---

## Project Structure

```bash
weather_app/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Installation

First install the required libraries:

```bash
pip install flask requests
```

---

## API Key Setup

Go to the OpenWeather website and create a free account:

https://openweathermap.org/api

Generate your API key and paste it inside `app.py`

Example:

```python
API_KEY = "your_api_key"
```

---

## Run the Project

```bash
python app.py
```

After running, open this in browser:

```bash
http://127.0.0.1:8000
```

---

## What I Learned

While making this project I learned:
- How APIs work
- How to fetch data using requests
- How to handle API responses
- How Flask connects frontend and backend
- Basic error handling

---
