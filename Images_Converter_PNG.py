from PIL import Image
import os

# using forward slashes
input_dir = "C:/Users/R/Downloads"

output_dir = "C:/Users/R/Desktop/esty"


# loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".WEBP") or filename.endswith(".bmp") or filename.endswith(".gif"):
        # open the image file
        with Image.open(os.path.join(input_dir, filename)) as im:
            # create a new filename for the converted image
            new_filename = os.path.splitext(filename)[0] + ".png"
            # convert the image and save it to the output directory with the new filename
            im.convert("RGBA").save(os.path.join(output_dir, new_filename), "PNG")
