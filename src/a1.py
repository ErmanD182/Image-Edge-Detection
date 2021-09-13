'''
Created on Sep. 28, 2020

CP-467-A - Image Processing & Recognition

Assignment 1

@authors: Erman Dinsel ID:160364040
          Stuart Isley ID:160757220
'''

# Import Image and ImageFilter from PIL, which is a Python Imaging Library
from PIL import Image, ImageFilter

# Open the image and convert it to grayscale
original_image = Image.open("shrek.png").convert("L")
# Create a new image that will be the edge detected image
newImage = Image.new("RGBA", original_image.size)

# Create an array that will act as the 3x3 Laplacian kernel
kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
new_pixel_val = 0

print("Running Convolution Calculation for Edge Detection...")

# Starting point at (0,0) is the top left coordinate of the image
# Loop through from top to bottom from left to right going through all pixels in the image
# original_image.size[0] is the horizontal length of the image and original_image[1] is the vertical length of the image
for x in range(0, original_image.size[0]):
    for y in range(0, original_image.size[1]):
        image_matrix = []

        # The current (x,y) pixel we are dealing with is the middle pixel of the 3x3 image region
        mid_pixel = original_image.getpixel((x, y))
        # Add zero padding at the borders of the image
        left_pixel = 0
        right_pixel = 0
        bottom_pixel = 0
        top_pixel = 0
        top_left_pixel = 0
        top_right_pixel = 0
        bottom_left_pixel = 0
        bottom_right_pixel = 0

        # Check if the pixels around the middle pixel are in range, if so get the pixel.
        # If not, their value is already set to zero

        # Check left pixel
        if x - 1 >= 0:
            left_pixel = original_image.getpixel((x - 1, y))
        # Check right pixel
        if (x + 1 < original_image.size[0]):
            right_pixel = original_image.getpixel((x + 1, y))
        # Check bottom pixel
        if (y + 1 < original_image.size[1]):
            bottom_pixel = original_image.getpixel((x, y + 1))
        # Check top pixel
        if (y - 1 >= 0):
            top_pixel = original_image.getpixel((x, y - 1))
        # Check top left pixel
        if (x - 1 >= 0 and y - 1 >= 0):
            top_left_pixel = original_image.getpixel((x - 1, y - 1))
        # Check top right pixel
        if (x + 1 < original_image.size[0] and y - 1 >= 0):
            top_right_pixel = original_image.getpixel((x + 1, y - 1))
        # Check bottom left pixel
        if (x - 1 >= 0 and y + 1 < original_image.size[1]):
            bottom_left_pixel = original_image.getpixel((x - 1, y + 1))
        # Check bottom right pixel
        if (x + 1 < original_image.size[0] and y + 1 < original_image.size[1]):
            bottom_right_pixel = original_image.getpixel((x + 1, y - 1))

        # Add the pixel values from the current 3x3 region in the image to an array that will act as the 3x3 image
        # matrix
        image_matrix.append(top_left_pixel)
        image_matrix.append(top_pixel)
        image_matrix.append(top_right_pixel)
        image_matrix.append(left_pixel)
        image_matrix.append(mid_pixel)
        image_matrix.append(right_pixel)
        image_matrix.append(bottom_left_pixel)
        image_matrix.append(bottom_pixel)
        image_matrix.append(bottom_right_pixel)

        # Convolution of the 3x3 region of the image with the 3x3 kernel
        # The elements at the same position are multiplied with each other.
        # The sum of these multiplications is the new pixel value
        for i in range(0, len(kernel)):
            new_pixel_val = new_pixel_val + kernel[i] * image_matrix[i]

        # Place the new pixel value into the current (x,y) position (the middle pixel position)
        newImage.putpixel((x, y), (0, 0, 0, new_pixel_val))
        # Reset the new pixel value to 0
        new_pixel_val = 0

print("Completed. New edge detected image saved!")

# Display the new edge detected image
newImage.show()

# Save the new edge detected image
newImage.save('edgeDetectedImage.png')

# ---------------------EDGE DETECTION USING IMAGE FILTER FROM PIL LIBRARY---------------------------------------------

# imagePILedges = original_image.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0))

# Display the new image with edge detection
# imagePILedges.show()
