import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

# OpenWeather API endpoint && key
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

# Twillio Account SID and Auth Token set as environment variables
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


# NYC used here for lat & long
weather_params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# OpenWeather API request
response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
# Get weather conditions for the next 12 hours
weather_slice = weather_data["hourly"][:12]

will_rain = False

# Loop over every hour to check if it will rain or snow
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
        client = Client(account_sid, auth_token)
        
# Text message alert to send if rain or snow will arrive
if will_rain:
    message = client.messages \
                .create(
                     body="It's going to rain today, Don't forget an umbrella!!!",
                     from_=os.environ.get("TWILIO_PHONE_NUMBER"),
                     to=os.environ.get("PHONE_NUMBER_TO_RECEIVE")
                 )
    print(message.status)


