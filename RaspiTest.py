# client code (raspberry pi)
import dropbox 
from picamera import PiCamera
from time import sleep
import requests

# imports for display
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

# Raspberry Pi pin configuration for display:
# RST = None 
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

############## Weather
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Waterloo'
url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
current_temp = round(json_data['main']['temp']-273.15)

print(url)
draw.text(formatted_data)
print(formatted_data)
draw.text(current_temp + '°C')
print(str(current_temp)+'°C' )

############### Take Image with Camera
camera = PiCamera()
camera.start_preview()
# make preview slightly see-through (to see errors)
camera.start_preview(alpha=200)
# sleep for at least 2 seconds before capturing image
sleep(5) 
# Taking pictures
camera.capture('/home/pi/ProjectImages/image.jpg')
camera.stop_preview()
# rotate preview:
camera.rotation = 270

camera.start_preview()
camera.capture('/home/pi/ProjectImages/image.jpg')
camera.stop_preview()

# might have to regenerate access token
dropbox_access_token= "HyKnLMnTXVMAAAAAAAAAARiPgdCGYaDC8-ne9zsm3VbXxXlLSkbihvSjsmiFAqlW"
dropbox_path= "/image.jpg"
computer_path="/home/pi/ProjectImages/image.jpg"
client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

# Clear dropbox folder contents
client.files_delete('/image.jpg')
print("[CLEAR] dropbox files deleted")

# Upload image to dropbox folder
client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))


'''
metadata, f = client.files_download(dropbox_path)
out = open("downloadedimage1.jpg", 'wb')
out.write(f.content)
out.close()
'''


