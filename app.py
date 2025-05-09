# Import necessary libraries for web app, data handling, and serialization
import pickle                      # For loading pre-saved Python objects
import streamlit as st             # For building the web app interface
import pandas as pd                # For data manipulation

# Load the precomputed similarity matrix from a pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Define a function to recommend similar movies
def recommend(movie):
    
    # Find the index of the selected movie in the DataFrame
    index = movies[movies['name'] == movie].index[0]
    
    # Get a list of (index, similarity_score) tuples, sorted by similarity (descending)
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies = []
    
    # Loop through the top 5 similar movies (excluding the movie itself)
    for i in distances[1:6]:
        recommend_movies.append(movies['name'].iloc[i[0]])  # Add each recommended movie's name to the list
    return recommend_movies   # Return the list of recommended movie names

# Load the movie data (as a dictionary) and convert it to a DataFrame
movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

# Streamlit app title
st.title("Movie Recommendation System")

# Create a dropdown/select box for users to choose a movie
selected_movie = st.selectbox(
    "Type or select a movie",
    movies['name'].values  # List of all movie names for selection
)

# When the 'Recommend Movies' button is clicked
if st.button('Recommend Movies'):
    recommend_movies = recommend(selected_movie)  # Get recommendations for the selected movie
    for i in recommend_movies:
        st.write(i)  # Display each recommended movie name in the web app
