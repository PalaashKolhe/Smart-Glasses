# client code (raspberry pi)
import dropbox 
from picamera import PiCamera
from time import sleep

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
