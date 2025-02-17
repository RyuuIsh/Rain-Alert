# Rain-Alert-Notification-System
A Python-based weather alert system that notifies users via SMS if it's going to rain. This project fetches real-time weather forecasts using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected.

## Features
- Fetches hourly weather data for the next few hours.
- Checks for rainy weather conditions based on OpenWeatherMap weather codes.
- Sends an SMS alert if rain is predicted, reminding the user to carry an umbrella.

## Tech-Stack
- Python – Core programming language
- Requests – Fetching weather data from OpenWeatherMap API
- Twilio API – Sending SMS notifications
- OpenWeatherMap API – Fetching weather forecast

## How-It-Works
1. Fetch Weather Data – Uses OpenWeatherMap API to get the forecast.
2. Check Rain Conditions – Scans weather codes for potential rain.
3. Send SMS Alert – Uses Twilio API to notify the user via text.

## Future-Enhancements
- Add multiple location support
- Integrate with Telegram for alerts
- Set up a web dashboard for weather tracking

Stay dry and never forget your umbrella again!
