import pywhatkit as kt

print("Program to convert Images to ASCII art")

source_path = 'DSC_5462.jpg'
target_path = 'ascii_art1.text'

kt.image_to_ascii_art(source_path, target_path)
