import streamlit as st
import pandas as pd
import random

# Load CSV files in chunks
@st.cache_data
def load_font_pairs(filepath='shuffled_pairs.csv', chunksize=10000):
    chunks = []
    for chunk in pd.read_csv(filepath, chunksize=chunksize, usecols=['Font1', 'Font2', 'Cosine Distance', 'Contrast Level']):
        chunks.append(chunk)
    return pd.concat(chunks, ignore_index=True)

@st.cache_data
def load_google_fonts(filepath='google-fonts.csv'):
    return pd.read_csv(filepath)

# Function to get Google Fonts URL
def get_google_fonts_url(font_name):
    base_url = "https://fonts.googleapis.com/css2?family="
    formatted_name = font_name.replace(' ', '+')
    return f"{base_url}{formatted_name}:wght@400;700&display=swap"

def set_google_fonts_url(font_name):
    base_url = "https://fonts.google.com/specimen/"
    return f"{base_url}{font_name.replace(' ', '+')}"

# Load data
font_pairs_data = load_font_pairs()
google_fonts_data = load_google_fonts()

default_contrast_level = 'Balanced Contrast'

if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to explore multilingual fonts
def explore_multilingual_fusion():
    st.title("Explore Multilingual Fusion 🔀")

    # Sidebar for selecting subset and contrast level
    st.sidebar.title("Font and Subset Selection")

    # List of Indian subsets and their respective texts
    indian_subsets = {
        'bengali': 'বাংলা',
        'devanagari': 'देवनागरी',
        'gujarati': 'ગુજરાતી',
        'gurmukhi': 'ਗੁਰਮੁਖੀ',
        'kannada': 'ಕನ್ನಡ',
        'malayalam': 'മലയാളം',
        'oriya': 'ଓଡ଼ିଆ',
        'tamil': 'தமிழ்',
        'telugu': 'తెలుగు'
    }

    # Filter subsets to only Indian subsets
    available_indian_subsets = [subset for subset in indian_subsets.keys() if f'subsets_{subset}' in google_fonts_data.columns]

    # Dynamic key for subset selection
    selected_subset = st.sidebar.selectbox("Select Language", available_indian_subsets, key="language_select")

    # Map selected subset to the column name
    subset_column = f'subsets_{selected_subset}'

    # Filter fonts based on selected subset
    subset_fonts = google_fonts_data[google_fonts_data[subset_column] == 1]['family'].tolist()

    # Sidebar for selecting contrast level
    st.sidebar.title("Select Contrast Level")
    contrast_levels = font_pairs_data['Contrast Level'].unique()
    selected_level = st.sidebar.selectbox("Select Contrast Level", contrast_levels, index=contrast_levels.tolist().index(default_contrast_level), key='contrast_level')

    # Filter font pairs based on selected contrast level
    filtered_data = font_pairs_data[font_pairs_data['Contrast Level'] == selected_level]

    def get_font_pair_supporting_subset():
        """Get a font pair where at least one font supports the selected subset."""
        available_pairs = filtered_data[
            (filtered_data['Font1'].isin(subset_fonts)) | (filtered_data['Font2'].isin(subset_fonts))
        ]
        if available_pairs.empty:
            return None
        return available_pairs.sample().iloc[0]

    if subset_fonts and not filtered_data.empty:
        if st.sidebar.button("Next Font Pair ⏭️", key='next_font_pair'):
            current_pair = get_font_pair_supporting_subset()
            if current_pair is not None:
                st.session_state.index = current_pair.name

        current_pair = get_font_pair_supporting_subset()

        if current_pair is not None:
            font1_name = current_pair['Font1']
            font2_name = current_pair['Font2']

            # Determine which font supports the selected subset
            if font1_name in subset_fonts and font2_name in subset_fonts:
                # Both fonts support the subset, randomly choose
                if random.choice([True, False]):
                    subset_font_name = font1_name
                    english_font_name = font2_name
                else:
                    subset_font_name = font2_name
                    english_font_name = font1_name
            elif font1_name in subset_fonts:
                subset_font_name = font1_name
                english_font_name = font2_name
            else:
                subset_font_name = font2_name
                english_font_name = font1_name

            # Editable text areas for user input
            font1_user_text = st.text_area("Edit Font 1 Text", indian_subsets[selected_subset], key="font1_text")

            font2_user_text = st.text_area("Edit Font 2 Text", "English", key="font2_text")

            # Display font names and links
            font1_url = get_google_fonts_url(font1_name)
            font2_url = get_google_fonts_url(font2_name)
            font1_specimen_url = set_google_fonts_url(font1_name)
            font2_specimen_url = set_google_fonts_url(font2_name)

            st.markdown(f"Font 1: [{font1_name}]({font1_specimen_url})")
            st.markdown(f"Font 2: [{font2_name}]({font2_specimen_url})")

            # Display sample text in the selected fonts
            html_head = f"""
            <link href="{font1_url}" rel="stylesheet">
            <link href="{font2_url}" rel="stylesheet">
            <style>
                .font1 {{ font-family: '{font1_name}', sans-serif; }}
                .font2 {{ font-family: '{font2_name}', sans-serif; }}
                .text-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: #0E1117;
                    padding: 10px;
                    color: #ffffff;
                    word-wrap: break-word;
                }}
                .font1, .font2 {{
                    font-size: 40px;
                }}
            </style>
            """

            html_content = f"""
            <div class="text-container">
                <span class="font1">{font1_user_text}</span>
                <span class="font2">{font2_user_text}</span>
            </div>
            """

            # Combine the head and content and display it
            st.markdown(html_head + html_content, unsafe_allow_html=True)
        else:
            st.write("No font pairs available for the selected contrast level or subset.")
    else:
        st.write("No font pairs available for the selected contrast level or subset.")



