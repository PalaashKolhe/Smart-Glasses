# client code (raspberry pi)
import dropbox 
from picamera import PiCamera
from time import sleep
import time
import requests

# library for display
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)

device = ssd1306(serial, rotate=1)

############## Weather
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Waterloo'
url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
current_temp = round(json_data['main']['temp']-273.15)

print(url)
print(formatted_data)
print(str(current_temp)+'C' )

# Load default font.
# font = ImageFont.load_default()

while True:
	with canvas(device) as draw:
        # draw.text((x, top),       "My name is Palaash ",  font=font, fill=255)
        	draw.text((0, 0), formatted_data.title(), fill=255)
        	draw.text((0, 10), str(current_temp) + 'C', fill=255)
        	draw.text((0, 20), "___________", fill = "white")
	
	takePicture = input("Take picture? Y/n: ")
	if takePicture in ('Y','y'):
		############### Take Image with Camera
		camera 	= PiCamera()
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



		metadata, f = client.files_download('/output/out.txt')
		out = open("outputText.txt", 'wb')
		out.write(f.content)
		out.close()

		f = open("outputText.txt")
		content = []
		content.append(f.read())
		f.close()
			
		for i in range(len(content)):
			content[i] = content[i].split('\n')
		print(content)
		
		# for i in range(1, len(content[0]), 1):
		for i in range(1, len(content[0]), 2):
			with canvas(device) as draw:
				draw.text((0, 10), content[0][i], fill=255)
				try:
					draw.text((0, 20), content[0][i+1], fill=255)
				except IndexError:
					pass
				sleep(4) 

 




