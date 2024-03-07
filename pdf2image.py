import fitz
from PIL import Image
import os

pdf_path = "C:/Users/raghul/Desktop/task0/Mark-img.pdf"
output_folder = "C:/Users/raghul/Desktop/task0/output_images"
counter = 1
dpi = 1000  # Set the desired DPI value

# Open the PDF file
pdf = fitz.open(pdf_path)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each page
for i in range(len(pdf)):
    # Get the page
    page = pdf[i]

    # Render the page as an image with specified DPI
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

    # Convert the image data to a PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the image
    output_image_path = os.path.join(output_folder, f"image{counter}.jpg")
    img.save(output_image_path, dpi=(dpi, dpi))
    print(f"Saved high-quality image {output_image_path}")
    counter += 1

# Close the PDF file
pdf.close()
