import pickle
import streamlit as st

# Load the data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit code
st.header('Movie Recommender System')

movie_name = st.text_input("Enter a movie name", "Type Here ...")

if st.button("Recommender"):
    try:
        movie_index = movies.index(movie_name)
        similar_movies = sorted(list(enumerate(similarity[movie_index])), key=lambda x: x[1], reverse=True)[1:6]
        recommended_movies = [movies[i[0]] for i in similar_movies]
        st.write("Recommended movies are : ", recommended_movies)
    except:
        st.write("Movie not found. Please enter a valid movie name.")