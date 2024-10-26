import time
import requests
from datetime import datetime
from smtplib import SMTP

MY_MAIL = "jadevictor247@gmail.com"
PASSWORD = "#YOUR-PASSWORD"

MY_LAT = 6.451140 # Your latitude
MY_LONG = -3.388400 # Your longitude


def iss_overhead():
    # If the ISS is close to my current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <=iss_latitude <= MY_LAT+5 and MY_LONG-5 <=iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # and it is currently dark
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    with SMTP('smtp.gmail.com') as conn:
        # Then send me an email to tell me to look up.
        conn.starttls()
        conn.login(user=MY_MAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg=f"Subject:Look Up! \n\nThe ISS is above you in the sky."
        )
