from PIL import Image

# Image dimensions and the portion of the complex plane to display
width, height = 800, 800
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
max_iter = 100

# Create a new RGB image
image = Image.new("RGB", (width, height))

# Iterate over each pixel
for x in range(width):
    for y in range(height):
        # Map pixel position to a point in the complex plane
        real = xmin + (x / width) * (xmax - xmin)
        imag = ymin + (y / height) * (ymax - ymin)
        c = complex(real, imag)
        z = 0 + 0j

        # Mandelbrot iteration
        color = (0, 0, 0)  # Default to black
        for i in range(max_iter):
            if abs(z) > 2.0:
                # Calculate color based on the iteration count
                color = (i % 4 * 64, i % 8 * 32, i % 16 * 16)
                break
            z = z * z + c
        
        # Set pixel color
        image.putpixel((x, y), color)

# Save the image
image.save("mandelbrot_set.png", "PNG")
