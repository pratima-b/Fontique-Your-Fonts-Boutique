import streamlit as st
import pandas as pd
from font_similarity import get_font_path
import base64
import os

@st.cache_data
def load_data():
    return pd.read_csv('font_pairs_with_moods.csv')  # Assuming the CSV file name

def embed_font(font_path, font_name):
    with open(font_path, "rb") as font_file:
        encoded_font = base64.b64encode(font_file.read()).decode("utf-8")
    return f"@font-face {{ font-family: '{font_name}'; src: url(data:font/ttf;base64,{encoded_font}) format('truetype'); }}"

def get_google_font_url(font_name):
    return f"https://fonts.google.com/specimen/{font_name.replace(' ', '+')}"

def font_gallery():
    # Load data
    font_data = load_data()

    # Moods dictionary
    moods = {
        'All': 'All',
        0: 'Casual',
        1: 'Elegant',
        2: 'Modern',
        3: 'Playful',
        4: 'Formal',
        5: 'Retro',
        6: 'Tech',
        7: 'Creative',
        8: 'Vintage',
        9: 'Futuristic',
        10: 'Neutral',
        11: 'Dynamic',
        12: 'Sophisticated',
        13: 'Artistic'
    }

    # Initialize session state for pagination and mood
    if 'start_index' not in st.session_state:
        st.session_state.start_index = 0
    if 'selected_mood' not in st.session_state:
        st.session_state.selected_mood = 'All'  # Default to 'All' moods

    # User interface for Font Gallery
    st.title("Mood Based Pairs 🔍")

    # Select mood
    selected_mood = st.selectbox("", list(moods.values()), key='mood_select')

    # Check if the mood has changed
    if st.session_state.selected_mood != selected_mood:
        st.session_state.selected_mood = selected_mood
        st.session_state.start_index = 0  # Reset pagination

    # Filter data based on selected mood
    if st.session_state.selected_mood == 'All':
        filtered_data = font_data
    else:
        filtered_data = font_data[font_data['mood'] == st.session_state.selected_mood]

    # Shuffle the filtered data
    shuffled_data = filtered_data.sample(frac=1, random_state=42).reset_index(drop=True)

    # Pagination settings
    fonts_per_page = 3
    total_fonts = len(shuffled_data)
    valid_fonts = []

    while len(valid_fonts) < fonts_per_page * 3 and st.session_state.start_index < total_fonts:
        current_batch = shuffled_data.iloc[st.session_state.start_index:st.session_state.start_index + fonts_per_page * 6]
        for index, row in current_batch.iterrows():
            font1_name = row['Font1']
            font2_name = row['Font2']

            try:
                font1_path = get_font_path(font1_name)
                font2_path = get_font_path(font2_name)

                # Check if both font files exist
                if os.path.exists(font1_path) and os.path.exists(font2_path):
                    valid_fonts.append((font1_name, font1_path, font2_name, font2_path))
                    if len(valid_fonts) >= fonts_per_page * 3:
                        break
            except (FileNotFoundError, OSError):
                continue  # Skip this font pair silently

        st.session_state.start_index += len(current_batch)

    # Display font pairs
    if valid_fonts:
        #st.write(f"Displaying random font pairs for mood: {selected_mood}")

        # Create rows of 3 font pairs each
        for i in range(0, len(valid_fonts), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(valid_fonts):
                    font1_name, font1_path, font2_name, font2_path = valid_fonts[i + j]

                    # Load the fonts in the HTML
                    html_head = f"""
                    <style>
                        {embed_font(font1_path, font1_name)}
                        {embed_font(font2_path, font2_name)}
                        .font-box {{
                            width: 100%;
                            height: 200px;  /* Fixed height */
                            border: 1px solid #ccc;
                            padding: 10px;
                            margin: 5px;
                            text-align: center;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            flex-direction: column;
                            background: #0E1117;
                        }}
                        .font-box p {{
                            margin: 0;
                        }}
                    </style>
                    """

                    # Define HTML content for display
                    html_content = f"""
                    <div class="font-box">
                        <a href="{get_google_font_url(font1_name)}" target="_blank" style="text-decoration: none;" title="Click to go to {font1_name} on Google Fonts">
                            <p style="font-family: '{font1_name}'; font-size: 22px; color: #fff;">
                                {font1_name}
                            </p>
                        </a>
                        <a href="{get_google_font_url(font2_name)}" target="_blank" style="text-decoration: none;" title="Click to go to {font2_name} on Google Fonts">
                            <p style="font-family: '{font2_name}'; font-size: 22px; color: #fff;">
                                {font2_name}
                            </p>
                        </a>
                    </div>
                    """

                    # Combine the head and content and display it in the column
                    col.markdown(html_head + html_content, unsafe_allow_html=True)

        # Pagination controls
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button('Previous') and st.session_state.start_index - fonts_per_page * 6 >= 0:
                st.session_state.start_index -= fonts_per_page * 6
        with col3:
            if st.button('Next') and st.session_state.start_index < total_fonts:
                st.session_state.start_index += fonts_per_page * 6
    else:
        st.write(f"No valid font pairs available for the selected mood: {selected_mood}")

# Assuming that Streamlit runs this as the main script
if __name__ == "__main__":
    font_gallery()
