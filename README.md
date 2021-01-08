# Shady Assistant - Wearable Text Recognition/Translation Technology

Shady Assistant are smart glasses with built-in text recognition and translation technology. The glasses have a camera, OLED display, and a Raspberry Pi Zero W mounted on them. 

## How they work
* When the user asks the glasses to translate the text in front of them, the camera takes a picture of everything their eyes would see. 
* The Python script running on the Rasberry Pi Zero W then uploads these images to a remote Dropbox server through the Dropbox API. 
* Our server then downloads these images and runs the OpenCV powered text recognition and outputs the text in a .txt file, which then get translated to English through the Google Translate API. 
* This translated text is then uploaded to the Dropbox server, where our smart glasses then download and display this text to the OLED display. 

## Link to video
[![POLICY 71: Shady Assistant](http://img.youtube.com/vi/h-YQnXVjZhs/maxresdefault.jpg)](https://youtu.be/h-YQnXVjZhs)
