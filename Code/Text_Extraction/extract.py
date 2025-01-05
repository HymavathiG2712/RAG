import PyPDF2

# # Open the PDF file
pdf_file_path = '/Users/hymavathigummudala/VS/Chunking1/nutri.pdf'
with open(pdf_file_path, 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Extract text from all pages
    extracted_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        extracted_text += page.extract_text()

# Print or process the extracted text
print(extracted_text)

# You can save the extracted text to a file if needed
with open('output_chunk1.txt', 'w') as output_file:
        output_file.write(extracted_text)

print("Text extracted and saved to 'output_chunk1.txt'")
