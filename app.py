import streamlit as st
import pickle
import requests

def fetch_poster(movie_id,index):
    # key = "446176bf48f29bacbc6f0f46f067c5bf"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=446176bf48f29bacbc6f0f46f067c5bf&language=en-US"  # Correct URL format
    data = requests.get(url,stream=True,verify=False,headers={'content-type': 'application/json'})
    data = data.json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"  # Use f-string for poster URL
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")





# imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    print(len(distance))
    for i in distance[1:len(distance)]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id,index))
    return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)

    # First row of 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

    # Second row of 5 columns
    # col6, col7, col8, col9, col10 = st.columns(5)
    # with col6:
    #     st.text(movie_name[5])
    #     st.image(movie_poster[5])
    # with col7:
    #     st.text(movie_name[6])
    #     st.image(movie_poster[6])
    # with col8:
    #     st.text(movie_name[7])
    #     st.image(movie_poster[7])
    # with col9:
    #     st.text(movie_name[8])
    #     st.image(movie_poster[8])
    # with col10:
    #     st.text(movie_name[9])
    #     st.image(movie_poster[9])