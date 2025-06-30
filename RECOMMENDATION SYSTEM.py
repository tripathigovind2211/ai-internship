import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Sample movie dataset
movies = {
    'Title': [
        'The Matrix', 'John Wick', 'Inception',
        'The Lion King', 'Finding Nemo', 'Avengers: Endgame',
        'The Dark Knight', 'Interstellar', 'Toy Story', 'Frozen'
    ],
    'Genre': [
        'Action Sci-Fi', 'Action Thriller', 'Action Sci-Fi',
        'Animation Adventure', 'Animation Family', 'Action Superhero',
        'Action Crime', 'Sci-Fi Drama', 'Animation Comedy', 'Animation Musical'
    ]
}

df = pd.DataFrame(movies)

# Step 2: Convert genres into TF-IDF vectors
tfidf = TfidfVectorizer()
genre_matrix = tfidf.fit_transform(df['Genre'])

# Step 3: Compute cosine similarity
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Step 4: Recommend similar movies
def recommend_movies(title):
    if title not in df['Title'].values:
        print("Movie not found. Please try another.")
        return

    idx = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    print(f"\n📽️ Because you liked **{title}**, you might also enjoy:")
    for i in sim_scores[1:6]:  # top 5 excluding the input
        print("  →", df['Title'][i[0]])

# Example run
print("🎬 Movie Options:", ", ".join(df['Title']))
user_input = input("\nEnter a movie you like: ")
recommend_movies(user_input)
