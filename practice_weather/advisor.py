from weather_api import fetch_weather

def get_clothing_advice(city):
    try:
        result = fetch_weather(city)

        temperature = result['temp']

        if temperature > 30:
            return 'Wear Shorts'
        if temperature < 10 :
            return "Wear a Coat"
        return "Jeans"
    except TimeoutError:
        # Specifically handles if the API took too long
        return "Stay Home"
    