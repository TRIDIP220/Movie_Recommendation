'''import streamlit as st
import pickle
import pandas as pd
import requests

st.title("Movie Recommendation System")
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch(movie_id):
    url ="https://api.themoviedb.org/3/movie/{}?api_key=1f8bbddd683318099177cd28613434ea&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path





def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    print(index)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    store =[]
    store_poster=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        store.append(movies.iloc[i[0]].title)
        store_poster.append(fetch(movie_id))
    return store,store_poster



Selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])'''

import streamlit as st
import pickle
import pandas as pd
import requests

st.title("Movie Recommendation System")
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch(movie_id):
    try:
        api_key = "1f8bbddd683318099177cd28613434ea"  # Replace with your actual TMDb API key
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            st.warning("Poster path not available for this movie.")
            return None  # Handle the case where the poster path is not available

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None  # Handle the error gracefully

# Rest of your code remains the same...


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    st.write(f"Selected Movie Index: {index}")
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    store = []
    store_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        store.append(movies.iloc[i[0]].title)
        poster_url = fetch(movie_id)
        store_poster.append(poster_url)
    return store, store_poster

Selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        if recommended_movie_posters[0]:
            st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        if recommended_movie_posters[1]:
            st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        if recommended_movie_posters[2]:
            st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        if recommended_movie_posters[3]:
            st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        if recommended_movie_posters[4]:
            st.image(recommended_movie_posters[4])
