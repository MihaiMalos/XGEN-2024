import tensorflow as tf
import tensorflow_hub as hub

# Load pre-trained Universal Sentence Encoder model
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


def calculate_similarity_use(text1, text2):
    # Generate embeddings for the input texts
    embeddings = model([text1, text2])

    # Calculate cosine similarity between the embeddings
    similarity = cosine_similarity([embeddings[0].numpy()], [embeddings[1].numpy()])[0][0]

    return similarity * 100  # Convert to percentage


# Example usage
text1 = "The stock market crashed on Monday."
text2 = "On Monday, the stock market experienced a significant crash."
similarity = calculate_similarity_use(text1, text2)
print(f"Similarity: {similarity:.2f}%")