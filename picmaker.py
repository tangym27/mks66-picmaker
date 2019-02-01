file = open("pic.ppm", "w")

# Sets the limit of our file
ROWS = 500
COLS = 500

# Establishes a basic header for the ppm file
def header(file):
    file.write("P3\n")
    file.write(str(ROWS) + " " + str(COLS) +"\n")
    file.write("255\n")

# Produces an image
def body(file):
    # Initial location
    x = 0
    y = 0
    hue = 1
    # Repeat the same pattern for however many pixels divided by a set number of linesself.
    # If there are more numbers in a ppm file past the rows and col, it will not be in the image
    for time in range( int (ROWS*COLS/22.0 +1) ):
        # Writes 18 pixels
        while (x < 6):
            # Sets up initial colors
            r = 200  - hue
            g = hue
            b = 0 + hue
            # Uses the same color three times
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            x += 1
        # Resets the value for another pattern
        x = 0
        # Writes 20 pixels of a specific color
        while (x < 10):
            # Sets up initial colors
            r = 0 + hue
            g = hue
            b = 255 - hue
            # Uses the same color twice
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            file.write(str(r) + " " + str(g)+ " " + str(b) + "\n")
            x += 1
        # Resets the value for another loop
        x = 0
        # Updates hue for a gradient
        hue += 100
print("done")

header(file)
body(file)

file.close()
