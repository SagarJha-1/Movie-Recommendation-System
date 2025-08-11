import pandas as pd

try:
    print("Loading CSV...")
    df = pd.read_csv("imdb_top_1000.csv") 

    print("Dropping rows with missing essential data...")
    df = df.dropna(subset=['Series_Title', 'Poster_Link', 'Overview', 'Genre', 'Director'])

    print("Combining cast columns...")
    df['cast'] = df[['Star1', 'Star2', 'Star3', 'Star4']].fillna('').agg(', '.join, axis=1)

    print("Cleaning columns...")
    df['title'] = df['Series_Title'].str.strip()
    df['genres'] = df['Genre'].str.lower().str.replace(' ', '')
    df['overview'] = df['Overview'].str.strip().str.lower()
    df['director'] = df['Director'].str.strip().str.lower()
    df['year'] = df['Released_Year'].astype(str).str.strip() 


    print("Assigning numeric movie_id...")
    df = df.reset_index(drop=True)
    df['movie_id'] = df.index + 1

    print("First 5 movie_ids:")
    print(df['movie_id'].head())

    print("Saving movies.csv ...")
    movies_cols = ['movie_id', 'title', 'genres', 'overview', 'cast', 'director', 'year']
    df[movies_cols].to_csv("movies.csv", index=False)

    # Prepare poster dataset with movie_id
    posters_df = df[['movie_id', 'Series_Title', 'Poster_Link']].rename(columns={
        'Series_Title': 'title',
        'Poster_Link': 'image_url'
    })

    print("Saving movie_images.csv ...")
    posters_df.to_csv("movie_images.csv", index=False)

    print("✅ Cleaning and movie_id addition completed successfully!")

except FileNotFoundError:
    print("File not found: Please ensure 'imdb_top_1000.csv' is in the same folder as this script.")
except Exception as e:
    print(f"An error occurred: {e}")
