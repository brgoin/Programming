import requests

def show_data(data):
    if (data['cod'] != 200):
        print("Unable to find weather data for your location...")
        print("")
        return
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    description = data['weather'][0]['description']

    print('Current Temperature: {} degree fahrenheit'.format(temp))
    print('High Temmperature:{} degree fahrenheit'.format(hightemp))
    print('Low Temperature:{} degree fahrenheit'.format(lowtemp))
    print('Description:{}.format(description)')

    
def main():
    appid = "77054dd191def419d01555dd283282ae"
    print('Welcome to your weather.')

    while True:
        zip = get_zip()
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={appid}&zip={zip}"
        weatherData = getWeatherData(url)
        show_data(weatherData.json())

        again = input("Would you like to search again? (y/n) ")
        if again == 'n':
            print("Thank you for visiting, see you next time...")
            break

def getWeatherData(url):
    try:
        response = requests.get(url)
        print("Connection to web service successful...")
        print(f'{url}')
    except:
        print("Unable to connect to webservice...")
        print(f"URL: {url}")

    return response

def get_zip():
    while True:
        zip = input("Please enter a zip code: ")
        # Validate zip input
        if (zip.isdigit() and len(zip) == 5):
            break
        else:
            print("Invalid input, please enter a 5 digit zip code... ")
    return zip
<Allen Vvoelcker> <2/18/2022> <Application for weather> <Source Code>

main()
