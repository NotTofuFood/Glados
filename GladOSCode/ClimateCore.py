

from gtts import gTTS
import datetime
import requests



date = datetime.datetime.today()

timeDate = date.strftime('%m-%d-%Y')
language = 'en'
output = gTTS(text=timeDate, lang=language, slow=False)
output.save('currentTime.mp3')


# Weather Support Core

#Thx https://www.youtube.com/watch?v=lcWfSn6-m_8 and https://openweathermap.org/api

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b5c147416cb2c6a9a10b4ac0c8a627c7&q='
city = 'Havana'
url = api_address + city
json_data = requests.get(url).json()
temp_data = json_data['main']['temp']
formattedWeatherData = json_data['weather'][0]['description']
print(formattedWeatherData)

#Aperture Brand Converter C = K - 273.15   and  (K − 273.15) × 9/5 + 32 = °F

Cel = temp_data - 273.15

Fah = (temp_data - 273.15) * 9/5 + 32

tempStringCel = str(round(Cel))
tempStringFah = str(round(Fah))


finalString = 'Today, expect ' + formattedWeatherData + ' and a temperature of ' + tempStringCel + ' degrees celsius and ' + tempStringFah + ' degrees fahrenheit.'

print(finalString)

language = 'en'
output = gTTS(text=finalString, lang=language, slow=False)
output.save('temp.mp3')