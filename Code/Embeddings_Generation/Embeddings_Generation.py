from sentence_transformers import SentenceTransformer
import csv

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_chunks(file_path):
    chunks = []
    current_chunk = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Chunk") and line.endswith(":"):  # Detect the start of a new chunk
                if current_chunk:  # Add the previous chunk if it exists
                    chunks.append("\n".join(current_chunk).strip())
                    current_chunk = []
            current_chunk.append(line)  # Collect lines of the current chunk
        if current_chunk:  # Add the last chunk if it exists
            chunks.append("\n".join(current_chunk).strip())
    return chunks

# Path to the text file containing chunks
file_path = "/Users/hymavathigummudala/Embedding/chunked_sinatra_stephen_t_houston_mark_c_eds_nutritional_and_integra.txt"

chunks = extract_chunks(file_path)
# Generate embeddings
embeddings = model.encode(chunks)

# Verify that the number of embeddings matches the number of chunks
assert len(embeddings) == len(chunks), "The number of embeddings does not match the number of chunks."

# # Print results
# print(f"Number of chunks: {len(chunks)}")

# print(f"Number of embeddings: {len(embeddings)}")
# # print(f"Embedding size (vector dimensions): {len(embeddings[0])}")
# # print("Sample embedding for Chunk 1:", embeddings[0])


# Path to save the embeddings CSV
output_csv_path = "/Users/hymavathigummudala/Embedding/Marina/chunk_embeddings_sinatra.csv"

# Save embeddings to CSV
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(["Chunk Number", "Chunk Text", "Embedding Vector"])
    # Write each chunk and its embedding
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):
        writer.writerow([i, chunk, list(embedding)])

print(f"Embeddings saved to {output_csv_path}")