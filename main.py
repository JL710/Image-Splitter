import PIL
from PIL import Image

original_image_path = input("original image: ")
output_location = input("outputlocation: ")
piece_width = int(input("piece width: "))
piece_height = int(input("piece height: "))


original_image = Image.open(original_image_path)
original_image_width, original_image_height = original_image.size
columns = original_image_width // piece_width
rows = original_image_height // piece_height

for column in range(columns):
    for row in range(rows):
        print(row, column)
        top = row * piece_height
        left = column * piece_width
        #print(left, top, left + piece_width, top + piece_height)
        piece_image = original_image.crop((left, top, left + piece_width, top + piece_height))
        #piece_image.show()
        piece_image.save(f"{output_location}/{row}{column}.png")
