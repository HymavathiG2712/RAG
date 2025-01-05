from PIL import Image
import pytesseract

# # Load the image
# image_path = '/Users/hymavathigummudala/vs1/drive/types-of-amino-acids.png'
# img = Image.open(image_path)

# # Extract text from the image using pytesseract
# text = pytesseract.image_to_string(img)

# # Print the extracted text
# print(text)

import os
from PIL import Image
import pytesseract

# Path to the folder containing PNG images
folder_path = '/Users/hymavathigummudala/vs1/drive/'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PNG image
    if filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        
        # Load the image
        img = Image.open(image_path)
        
        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(img)
        
        # Print the extracted text
        print(f"Extracted text from {filename}:")
        print(text)
        print("\n" + "-"*50 + "\n")

# Save the extracted text to a file
output_file = 'extracted_text_images.txt'
with open(output_file, 'w') as f:
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            
            f.write(f"Extracted text from {filename}:\n{text}\n\n{'-'*50}\n\n")
            
print(f"Extracted text saved to {output_file}")
