import streamlit as st
import requests
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

# Replace with your actual Google Fonts API key
API_KEY = 'AIzaSyDMuuhzXQ5KDhfWnwHSPrG0hA1hHXJQ-Tk'

# Fetch Google Fonts data
@st.cache_data
def fetch_google_fonts(api_key):
    url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}"
    response = requests.get(url)
    return response.json()['items']

# Precompute font features based on actual data
def compute_font_features(fonts):
    categories = [font['category'] for font in fonts]
    unique_categories = list(set(categories))
    
    category_encoder = LabelEncoder()
    category_encoder.fit(unique_categories)
    
    font_features = {}
    for font in fonts:
        name = font['family']
        category = font['category']
        variants = len(font['variants'])
        subsets = len(font['subsets'])
        
        # Encode category
        category_encoded = category_encoder.transform([category])[0]
        
        # Feature vector: [category_encoded, number of variants, number of subsets]
        features = [category_encoded, variants, subsets]
        
        font_features[name] = features
    
    return font_features, category_encoder

# Apply t-SNE
def apply_tsne(font_features, n_components=3):
    font_names = list(font_features.keys())
    features = np.array(list(font_features.values()))
    
    tsne = TSNE(n_components=n_components, random_state=42)
    tsne_results = tsne.fit_transform(features)
    
    return font_names, tsne_results

# Apply K-means clustering
def apply_kmeans(tsne_results, n_clusters=10):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(tsne_results)
    return clusters, kmeans

# Get similar fonts based on t-SNE and K-means clustering
def get_similar_fonts(input_fonts, font_names, tsne_results, clusters, top_n=5):
    similar_fonts = {}
    for font in input_fonts:
        if font in font_names:
            idx = font_names.index(font)
            cluster_label = clusters[idx]
            cluster_indices = [i for i, x in enumerate(clusters) if x == cluster_label]
            distances = euclidean_distances([tsne_results[idx]], tsne_results[cluster_indices])[0]
            sorted_indices = np.argsort(distances)[:top_n + 1]  
            similar_fonts[font] = [font_names[cluster_indices[i]] for i in sorted_indices if cluster_indices[i] != idx]
    return similar_fonts

def get_font_url(font_name):
    font_name_formatted = font_name.replace(' ', '+')
    return f"https://fonts.googleapis.com/css2?family={font_name_formatted}"

def main():
    st.title("Similar Font Recommender 💡")

    fonts = fetch_google_fonts(API_KEY)
    font_names = [font['family'] for font in fonts]
    
    input_font1 = st.selectbox("Choose the first font", font_names)
    sample_text = st.text_input("Enter sample text", value="The quick brown fox jumps over the lazy dog.")
    top_n = st.slider("Number of similar fonts to display", min_value=1, max_value=10, value=5)

    font_features, category_encoder = compute_font_features(fonts)
    font_names, tsne_results = apply_tsne(font_features)
    clusters, kmeans = apply_kmeans(tsne_results)
    similar_fonts = get_similar_fonts([input_font1], font_names, tsne_results, clusters, top_n)
    
  
    font_url = get_font_url(input_font1)
    st.markdown(f'<link href="{font_url}" rel="stylesheet">', unsafe_allow_html=True)
    st.markdown(f'<p style="font-family:{input_font1}; font-size:24px;">{input_font1}: {sample_text}</p>', unsafe_allow_html=True)
   
    for font in similar_fonts[input_font1]:
        font_url = get_font_url(font)
        st.markdown(f'<link href="{font_url}" rel="stylesheet">', unsafe_allow_html=True)
        st.markdown(f'<p style="font-family:{font}; font-size:30px;">{font}: {sample_text}</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
