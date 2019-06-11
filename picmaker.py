file = open("pic.ppm", "w")

# Sets the limit of our file
ROWS = 500
COLS = 500

# Establishes a basic header for the ppm file
def header(file):
    file.write("P3\n")
    file.write(str(ROWS) + " " + str(COLS) +"\n")
    file.write("255\n")

def pixels(file):
    x = 0
    y = 0
    hue = 1
    # Repeat the same pattern for however many pixels divided by a set number of linesself.
    # If there are more numbers in a ppm file past the rows and col, it will not be in the image
    for time in range( int (ROWS*COLS/400.0 +1) ):
        for r in range(ROWS/10):
            for c in range(COLS/20):
                if ( (r - 25) ** 2 + (c - 25) ** 2 <= 15 ** 2):

                    red   = int(c/10 + 200)
                    green = int((500 - r)/2)
                    blue  = int(r/100)
                else:
                    red   = int(c/10 + 200)
                    green = int((500 - r)/2)
                    blue  = int(r/100)
                    # red   = int((500 - r)/2)
                    # green = int((500 - c)/2)
                    # blue  = int(r/3)
                file.write(str(red)+" ")
                file.write(str(green)+" ")
                file.write(str(blue)+" \t")
                file.write("\n")


# Produces an image
def body(file):
    # Initial location
    x = 0
    y = 0
    hue = 1
    # Repeat the same pattern for however many pixels divided by a set number of linesself.
    # If there are more numbers in a ppm file past the rows and col, it will not be in the image
    for time in range( int (ROWS*COLS/6.0 +1) ):

        if (hue > 255):
            hue = 0
        # Writes 18 pixels
        while (x < 2):
            # hue=x
            # Sets up initial colors
            r = 0
            g = 100 + hue
            b = 155  - hue
            # Uses the same color three times
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            # file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            # file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")

            x += 1
        # Resets the value for another pattern
        x = 0
        # Writes 20 pixels of a specific color
        while (x < 3):
            # hue=x
            # Sets up initial colors
            r = 0
            g = 0 + hue
            b = r
            # Uses the same color twice
            # file.write(str(210) + " " + str(105)+ " " + str(30) + "\n")
            file.write(str(210) + " " + str(105)+ " " + str(30) + "\n")
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")

            x += 1
        # Resets the value for another loop
        x = 0
        # Updates hue for a gradient
        hue += 50

print("done")

header(file)
pixels(file)
# body(file)

file.close()
