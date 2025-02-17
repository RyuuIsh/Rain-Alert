import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your_Api_Key"
account_sid = "Your_Account_Sid"
auth_token = "Your_Authentication_Token"

weather_params = {
    "lat": Your_Latitude,
    "lon": Your_Longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today. Remember to bring your Umbrella.",
        from_="+17076257950",
        to="+919818205507"
    )
    print(message.status)
