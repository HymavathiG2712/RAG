import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Function to load embeddings from CSV file
def load_embeddings_from_csv(file_path):
    chunks = []
    embeddings = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            chunk_text = row[1]  # Get chunk text
            embedding = np.array(eval(row[2]))  # Convert the string representation of the list back to a list
            chunks.append(chunk_text)
            embeddings.append(embedding)
    return chunks, np.array(embeddings)

# Path to the embeddings CSV file
csv_file_path = "/Users/hymavathigummudala/Embedding/Practice/chunk_embeddings_sinatra.csv"

# Load the chunks and embeddings
chunks, embeddings = load_embeddings_from_csv(csv_file_path)

# Compute cosine similarity between all embeddings
similarities = cosine_similarity(embeddings)

# Print the cosine similarity matrix
print("Cosine Similarity Matrix:")
print(similarities)

# Find the most similar pair of chunks
np.fill_diagonal(similarities, 0)  # Ignore self-similarity
most_similar_pair = np.unravel_index(np.argmax(similarities), similarities.shape)

print(f"Most similar chunks: Chunk {most_similar_pair[0]+1} and Chunk {most_similar_pair[1]+1}")
print(f"Similarity score: {similarities[most_similar_pair]:.4f}")

# Optionally, print similarity of the first few chunk pairs
print("\nTop Similarities:")
for i in range(5):  # Print first 5 similarity pairs
    for j in range(i+1, len(chunks)):
        print(f"Chunk {i+1} vs Chunk {j+1}: {similarities[i][j]:.4f}")
