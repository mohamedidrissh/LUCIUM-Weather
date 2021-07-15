#LUCIUM Weather App Version 1.5 (Original Source Code)
#Author: Mohamed Idris
#CODENAME: Arcadium
#Date of creation (Version 1): June 10th 2021
#Latest version creation date: June 11th 2021
#Scheduled for Github release on June 11h 2021

import tkinter as tk
import requests 
import time

#root=tk.Tk()
#winicon=tk.PhotoImage(file='icon.png')
#root.iconphoto(False, winicon)

def getWeather(canvas):
	city = textfield.get()
	api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=972c302ea06e38d8a492f5b55b2fe129"

	json_data = requests.get(api).json()
	condition = json_data['weather'][0]['main']
	temp = int(json_data['main']['temp'] -273.15)
	min_temp = int(json_data['main']['temp'] -275)
	max_temp = int(json_data['main']['temp'] -273.15)
	pressure = json_data['main']['pressure']
	humidity = json_data['main']['humidity']
	wind = json_data['wind']['speed']
	sunrise = time.strftime('%I:%M', time.gmtime(json_data['sys']['sunrise'] - 21600))
	sunset = time.strftime('%I:%M', time.gmtime(json_data['sys']['sunset'] - 21600))	
	final_info = condition + "\n" + str(temp) + "°C"
	final_data = "\n" + "Highest: " + str(max_temp) + "°C" + "\n" + "Lowest: " + str(min_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "Pa" + "\n" "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + "mph" + "\n" + "Sunrise: " + sunrise + "am" + "\n" + "Sunset: " + sunset + "pm"
	final_disclaimer = "\n" + "\n" "Weather info sourced by OpenWeatherMap.org"
	#final_appauthor = "App created by Mohamed Idris"
	final_appname = "\n" + "LUCIUM Weather"
	final_appversion = "Version 1.5"
	label1.config(text = final_info)
	label2.config(text = final_data)
	label3.config(text = final_disclaimer)
#	label4.config(text = final_appauthor)
	label5.config(text = final_appname)
	label6.config(text = final_appversion)

canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("LUCIUM Weather")
canvas.configure(bg='slategrey')

#Text configurations
a = ("roboto", 15, "bold")
b = ("Google Sans", 35, "italic", "bold")
c = ("Comic Sans MS", 35, "bold", "italic")
d = ("roboto", 10, "bold", "italic")
e = ("roboto", 10, "bold")
f = ("Courier New", 10, "bold")

#The part where you enter the city name.
textfield = tk.Entry(canvas, justify='center', width = 15, font = b,)
textfield.configure(bg='lavender')
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

#The part that gives you the weather info.
#label1 = The main weather info
#label2 = other info about the weather
#Label 3 = Disclamer section
label1 = tk.Label(canvas, font=c)
label1.pack()
label1.configure(bg='slategrey')

label2 = tk.Label(canvas, font=a)
label2.pack()
label2.configure(bg='slategrey')

label3 = tk.Label(canvas, font=d)
label3.pack()
label3.configure(bg='slategrey')

#label4 = tk.Label(canvas, font=d)
#label4.pack()
#label4.configure(bg='slategrey')

label5 = tk.Label(canvas, font=e)
label5.pack()
label5.configure(bg='slategrey')

label6 = tk.Label(canvas, font=f)
label6.pack()
label6.configure(bg='slategrey')
# End of label

canvas.mainloop()

# Contact Idris for source info.