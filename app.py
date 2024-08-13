import streamlit as st
import pickle
import pandas as pd

import requests
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=377ad90b16489a876f00c84b1e727e8b&language=en-Us".format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']





def recommend(movie):
    # Example implementation (replace with your actual logic)
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  # Skip the first as it is the selected movie itself
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters  # Ensure only two values are returned






movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'how would you like to be contacted',
    movies['title'].values
)

if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])