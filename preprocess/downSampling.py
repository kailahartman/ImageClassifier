from PIL import Image

# Load the original image
image = Image.open("hi.png")

# Resize the image to 32x32 pixels
resized_image = image.resize((32, 32), Image.ANTIALIAS)

# Save the resized image
resized_image.save("resized_image.png")
