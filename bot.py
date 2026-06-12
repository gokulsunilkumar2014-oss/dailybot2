import requests
from datetime import datetime

LATITUDE = 9.93
LONGITUDE = 76.26

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&current=temperature_2m"
)

data = requests.get(url, timeout=30).json()

temperature = data["current"]["temperature_2m"]

summary = f"""
DAILY WEATHER REPORT
====================

Date: {datetime.now().strftime('%Y-%m-%d')}

Current Temperature: {temperature}°C
"""

print(summary)

with open("daily_report.txt", "w", encoding="utf-8") as f:
    f.write(summary)
