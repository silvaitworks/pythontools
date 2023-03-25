from PIL import Image

def remove_background(image_path, threshold, image_name):
    image = Image.open(image_path) 

    grayscale = image.convert('L') 

    mask = Image.eval(grayscale, lambda x: 255 if x <= threshold else 0) 

    transparent = Image.new('RGBA', image.size, (0, 0, 0, 0)) 
    transparent.paste(image, (0, 0), mask=mask) 

    transparent.save(image_name)

image_path = input("What's the image you want to remove the background from? ")
threshold = int(input("Select the threshold you want (0-255): "))
image_name = input("What's the name you want for the image after the background removal? ")

remove_background(image_path, threshold, image_name)
