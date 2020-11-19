# client code (raspberry pi)
import dropbox 
from picamera import PiCamera
from time import sleep
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

############## Weather
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Waterloo'
url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
current_temp = round(json_data['main']['temp']-273.15)

print(url)
print(formatted_data)
print(str(current_temp)+'°C' )

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
num = 0
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    # cmd = "hostname -I | cut -d\' \' -f1"
    # IP = subprocess.check_output(cmd, shell = True )
    # cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    # CPU = subprocess.check_output(cmd, shell = True )
    # cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    # MemUsage = subprocess.check_output(cmd, shell = True )
    # cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    # Disk = subprocess.check_output(cmd, shell = True )

    # Write two lines of text.

    draw.text((x, top),       "My name is Palaash ",  font=font, fill=255)
    draw.text((x, top), formatted_data, font=font, fill=255)
    draw.text((x, top), current_temp + '°C', ont=font, fill=255)
    # draw.text((x, top+8),     str(CPU), font=font, fill=255)
    # draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
    # draw.text((x, top+25),    str(Disk),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)



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
# loop to take multiple pictures
camera.start_preview()
camera.capture('/home/pi/ProjectImages/image.jpg')
camera.stop_preview()

# might have to regenerate access token
dropbox_access_token= "HyKnLMnTXVMAAAAAAAAAARiPgdCGYaDC8-ne9zsm3VbXxXlLSkbihvSjsmiFAqlW"    #Enter your own access token
dropbox_path= "/image.jpg"
#change computer path as required
computer_path="/home/pi/ProjectImages/image.jpg"
client = dropbox.Dropbox(dropbox_access_token)

client.files_delete('/image.jpg')

print("[SUCCESS] dropbox account linked")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))


'''
metadata, f = client.files_download(dropbox_path)
out = open("downloadedimage1.jpg", 'wb')
out.write(f.content)
out.close()
'''
