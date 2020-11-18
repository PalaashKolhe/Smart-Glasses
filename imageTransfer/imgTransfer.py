# client code (raspberry pi)
import dropbox 

# might have to regenerate access token
dropbox_access_token= "sl.Alxxk63lVsN44PXEqT4fP_tch34U0otPUb67jBIgu7qG2q2OpC2VcUEfwhMMzaUSomAxahATNKpndpEFE3ikf8lM4sxUf8nIPy4cWft9A-WrYebvISgzoLGfjv85qOD5Yb4tze2zDK0"    #Enter your own access token
dropbox_path= "/image1.jpg"
#change computer path as required
computer_path="/home/michelle/se101/imageTransfer/testImages/image1.jpg"

client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))

metadata, f = client.files_download(dropbox_path)
out = open("downloadedimage1.jpg", 'wb')
out.write(f.content)
out.close()

