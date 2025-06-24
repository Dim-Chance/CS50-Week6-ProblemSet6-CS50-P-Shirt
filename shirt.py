import sys
import os
from PIL import Image, ImageOps

def main():

    #sys.argv = [os.path.basename(__file__), "before1.jpg", "after1.jpg"]
    #sys.argv = ["shirt.py", "before1.jpg", "after1.jpg"]
    input = sys.argv

    try:
        if len(input) < 3: # if the user does not specify exactly two command-line arguments
            sys.exit("Too few command-line arguments")

        if len(input) > 3:
            sys.exit("Too many command-line arguments")


        read_file = sys.argv[1]
        write_file = sys.argv[2]

        read_file_format = os.path.splitext(read_file)[-1]
        write_file_format = os.path.splitext(write_file)[-1]
        if not read_file_format.endswith(("jpg", "jpeg", "png")): # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
            sys.exit("Invalid output")

        if not write_file.lower().endswith(("jpg", "jpeg", "png")): # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
            sys.exit("Invalid output")



        if read_file_format != write_file_format: # if the input’s name does not have the same extension as the output’s name
            sys.exit("Input and output have different extensions")


        file = Image.open(read_file)
        #output = Image.open(write_file)
        shirt_image = Image.open("shirt.png")


        file_size = shirt_image.size
        output = ImageOps.fit(
            file,
            file_size)

        output.paste(shirt_image,box = (0, 0),mask=shirt_image)

        output.save(write_file)
    except FileNotFoundError: #if the specified input does not exist.
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
