# Long trying and failing in the dark i have found why the cs50 checker does not accepted my code. 

The first commit shows the baseline code (after many changes) 

## Issue was due to the transparent background

if you are having this issue just add this part of to your code
".convert("RGBA")" into the open 

```
shirt_image = Image.open("shirt.png").convert("RGBA")
```

## Previous changes: 

- Removed other defined functions and made it into a one main function to fix return issue
- Update to the code changing variable names.
- Testing it with diffrent files to see if it was a file issue
- Testing return functions to see if it was a return issue
- Testing sys.exit() options
- etc. 


### Code in mid chaos state 
Where i have tried couple of things mentioned above without the involvment of sys.argv so i could see what was going on 


```


import sys

from PIL import Image, ImageOps

"""
The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or

"""


def main():

    #sys.argv = ["shirt.py", "before1.jpg", "after1.jpg"]
    input = sys.argv

    try:
        if len(input) < 3: # if the user does not specify exactly two command-line arguments
            sys.exit("Too few command-line arguments")

        if len(input) > 3:
            sys.exit("Too many command-line arguments")


        read_file = sys.argv[1]
        write_file = sys.argv[2]

        read_file_format = read_file.split(".")[-1]
        write_file_format = write_file.split(".")[-1]
        read_file_format = read_file_format.lower()
        write_file_format = write_file_format.lower()

        if not read_file_format.endswith(("jpg", "jpeg", "png")): # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
            sys.exit("Invalid output")

        if not write_file.lower().endswith(("jpg", "jpeg", "png")): # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
            sys.exit("Invalid output")



        if read_file_format != write_file_format: # if the input’s name does not have the same extension as the output’s name
            sys.exit("Input and output have different extensions")


        file = Image.open(read_file)
        shirt_image = Image.open("/workspaces/65041095/shirt/shirt.png")


        file_size = shirt_image.size
        fitted_img = ImageOps.fit(
            file,
            file_size,
            method=Image.Resampling.BICUBIC,
            bleed=0.0,
            centering=(0.5, 0.5))

        # fitted_img.save("/workspaces/65041095/shirt/fitted.png")


        #pasted_image = fitted_img.copy()
        fitted_img.paste(shirt_image, (0, 0),mask=shirt_image)
        fitted_img.save(write_file)

        sys.exit()
        #pasted_image.show()
        #return pasted_image.save(write_file)


    except FileNotFoundError: #if the specified input does not exist.
        sys.exit("Input does not exist")


"""
def image_paste(read_file,write_file):
    file = Image.open(read_file)
    shirt_image = Image.open("/workspaces/65041095/shirt/shirt.png")


    file_size = shirt_image.size
    fitted_img = ImageOps.fit(
        file,
        file_size,
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5))

    # fitted_img.save("/workspaces/65041095/shirt/fitted.png")


    pasted_image = fitted_img.copy()
    pasted_image.paste(shirt_image, (0, 0),mask=shirt_image)
    #pasted_image.save(write_file)

    #pasted_image.show()
    return pasted_image.save(write_file)
 """

if __name__ == "__main__":
    main()
```
