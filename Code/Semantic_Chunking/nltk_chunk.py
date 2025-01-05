import os
import nltk
from langchain.text_splitter import NLTKTextSplitter

# Download NLTK data for tokenization (only needed once)
nltk.download('punkt')

# Step 1: Read the extracted text from the text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Step 2: Use NLTKTextSplitter to split the text into chunks
def split_text_into_chunks(text):
    text_splitter = NLTKTextSplitter()
    chunks = text_splitter.split_text(text)
    return chunks

# Step 3: Save the chunks to a new text file
def save_chunks_to_file(chunks, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for idx, chunk in enumerate(chunks):
            file.write(f"Chunk {idx+1}:\n{chunk}\n{'-'*40}\n")

# Step 4: Traverse each text file in a folder and create chunking files
def chunk_text_files_in_folder(folder_path, output_folder_path):
    # Ensure the output folder exists
    os.makedirs(output_folder_path, exist_ok=True)

    # Traverse all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):  # Process only text files
            file_path = os.path.join(folder_path, file_name)
            extracted_text = read_text_file(file_path)
            chunks = split_text_into_chunks(extracted_text)

            # Save the chunked text to a new file with the same name in the output folder
            output_file_path = os.path.join(output_folder_path, f"chunked_{file_name}")
            save_chunks_to_file(chunks, output_file_path)

            print(f"Chunks have been saved to {output_file_path}")

# Example usage
input_folder_path = "/Users/hymavathigummudala/Downloads/vis/"  # Folder with text files
output_folder_path = "/Users/hymavathigummudala/Downloads/vis/chunked_files"  # Folder for output files

chunk_text_files_in_folder(input_folder_path, output_folder_path)
