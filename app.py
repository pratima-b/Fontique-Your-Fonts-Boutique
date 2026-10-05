import streamlit as st
import pandas as pd
from font_similarity import load_font_pairs, get_font_path
import base64
import os
from auth import sign_up, sign_in, sign_out, get_current_user, db
# from share import generate_shareable_link, load_query_params
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Fontique", page_icon="fontique.svg")

# Load query parameters if present
# load_query_params()

# Utility function to generate Google Fonts URL
def get_google_fonts_url(font_name):
    base_url = "https://fonts.google.com/specimen/"
    return f"{base_url}{font_name.replace(' ', '+')}"

# Load the font pairs data
@st.cache_data
def load_data():
    return load_font_pairs()

# Load data
font_data = load_data()

default_contrast_level = 'High Contrast'



with st.sidebar:
    page = option_menu(
        menu_title="🧭 Navigation",
        options=["🏠 Home", "🔍 Mood Based Pairs", "🖼️ Inspos", "👤 User Account", "🌐 Explore Multilingual Fonts", "🔀 Explore Multilingual Fusion", "💡 Similar Font Recommender"],
        icons=[" ", " ", " ", " ", " ", " ", " "],  # No icons needed, as emojis are in the labels
        menu_icon=" ",
        default_index=0
    )
    
# Check if the user is authenticated
current_user = get_current_user()

# Authentication UI
# if current_user:
#     st.sidebar.write(f"Hello, {current_user['email']}")
#     if st.sidebar.button("Sign Out"):
#         sign_out()
#         st.experimental_rerun()
# else:
#     st.sidebar.title("Authentication")
#     email = st.sidebar.text_input("Email")
#     password = st.sidebar.text_input("Password", type="password")
#     auth_choice = st.sidebar.radio("Action", ["Sign In", "Sign Up"])

#     if auth_choice == "Sign In" and st.sidebar.button("Submit"):
#         sign_in(email, password)
#         st.experimental_rerun()
#     elif auth_choice == "Sign Up" and st.sidebar.button("Submit"):
#         sign_up(email, password)
#         st.experimental_rerun()

# Initialize session state
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'locked_font1' not in st.session_state:
    st.session_state.locked_font1 = None
if 'locked_font2' not in st.session_state:
    st.session_state.locked_font2 = None
if 'user_text' not in st.session_state:
    st.session_state.user_text = "This is a sample text"
if 'font1_size' not in st.session_state:
    st.session_state.font1_size = 60
if 'font2_size' not in st.session_state:
    st.session_state.font2_size = 40
if 'font_color' not in st.session_state:
    st.session_state.font_color = "#ffffff"  # Default font color
if 'saved_pairs' not in st.session_state:
    st.session_state.saved_pairs = []  # List to store saved font pairs

# Define embed_font function to be used in both pages
def embed_font(font_path, font_name):
    with open(font_path, "rb") as font_file:
        encoded_font = base64.b64encode(font_file.read()).decode("utf-8")
    return f"@font-face {{ font-family: '{font_name}'; src: url(data:font/ttf;base64,{encoded_font}) format('truetype'); }}"

# Function to save the font pair to Firestore
def save_font_pair(font1_name, font2_name, project_name):
    user = get_current_user()
    if user:
        user_id = user['localId']
        pair_data = {
            'Font1': font1_name,
            'Font2': font2_name,
            'ProjectName': project_name,
            'UserId': user_id
        }
        db.collection('user').document(user_id).collection('font_pairs').add(pair_data)
        st.success(f"Font pair {font1_name} and {font2_name} saved!")
    else:
        st.warning("Please sign in to save font pairs.")

def fetch_user_font_pairs(user_id):
    try:
        font_pairs_ref = db.collection('user').document(user_id).collection('font_pairs')
        font_pairs = font_pairs_ref.stream()

        # Collect font pair data
        font_pairs_list = []
        for pair in font_pairs:
            pair_data = pair.to_dict()
            font_pairs_list.append(pair_data)

        print(f"Number of font pairs fetched: {len(font_pairs_list)}")
        return font_pairs_list
    except Exception as e:
        print(f"Error fetching font pairs: {e}")
        return []

# Function to save like and comment
def like_and_comment(font1_name, font2_name, comment):
    user = get_current_user()
    if user:
        user_id = user['localId']
        like_comment_data = {
            'Font1': font1_name,
            'Font2': font2_name,
            'Comment': comment,
            'UserId': user_id
        }
        db.collection('likes_comments').add(like_comment_data)
        st.success("Your like and comment have been saved!")
    else:
        st.warning("Please sign in to like and comment.")

# Fetch likes and comments by user
def fetch_likes_comments(user_id):
    try:
        likes_comments_ref = db.collection('likes_comments').where('UserId', '==', user_id)
        likes_comments = likes_comments_ref.stream()

        likes_comments_list = []
        for lc in likes_comments:
            lc_data = lc.to_dict()
            likes_comments_list.append(lc_data)

        return likes_comments_list
    except Exception as e:
        print(f"Error fetching likes and comments: {e}")
        return []

def display_font_matrix(font_pairs):
    # Display font pairs in a 3x3 grid
    if font_pairs:
        for i in range(0, len(font_pairs), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(font_pairs):
                    pair = font_pairs[i + j]
                    font1_name = pair['Font1']
                    font2_name = pair['Font2']
                    
                    try:
                        font1_path = get_font_path(font1_name)
                        font2_path = get_font_path(font2_name)
                        
                        html_head = f"""
                        <style>
                            {embed_font(font1_path, font1_name)}
                            {embed_font(font2_path, font2_name)}
                            .font-box {{
                                width: 100%;
                                height: 200px;
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
                        
                        html_content = f"""
                        <div class="font-box">
                            <a href="{get_google_fonts_url(font1_name)}" target="_blank" style="text-decoration: none;" title="Click to go to {font1_name} on Google Fonts">
                                <p style="font-family: '{font1_name}'; font-size: 22px; color: #fff;">
                                    {font1_name}
                                </p>
                            </a>
                            <a href="{get_google_fonts_url(font2_name)}" target="_blank" style="text-decoration: none;" title="Click to go to {font2_name} on Google Fonts">
                                <p style="font-family: '{font2_name}'; font-size: 22px; color: #fff;">
                                    {font2_name}
                                </p>
                            </a>
                        </div>
                        """
                        
                        col.markdown(html_head + html_content, unsafe_allow_html=True)
                    except FileNotFoundError:
                        col.write(f"Font files for {font1_name} or {font2_name} not found.")
    else:
        st.write("No font pairs available.")


if page == "🏠 Home":
    # Main page content
    st.title("Fontique: Your Fonts Boutique✍️")

    # Move col1 content into sidebar
    with st.sidebar:
        # Get unique contrast levels
        contrast_levels = font_data['Contrast Level'].unique()

        selected_level = st.sidebar.selectbox("Select Contrast Level", contrast_levels, index=contrast_levels.tolist().index(default_contrast_level), key='contrast_level')

        # Filter data based on selected contrast level
        filtered_data = font_data[font_data['Contrast Level'] == selected_level]

        # If Font 1 or Font 2 is locked, filter the data to only include pairs containing the locked font(s)
        if st.session_state.locked_font1:
            filtered_data = filtered_data[(filtered_data['Font1'] == st.session_state.locked_font1) | (filtered_data['Font2'] == st.session_state.locked_font1)]
        if st.session_state.locked_font2:
            filtered_data = filtered_data[(filtered_data['Font1'] == st.session_state.locked_font2) | (filtered_data['Font2'] == st.session_state.locked_font2)]

        # Ensure index is within bounds
        if len(filtered_data) == 0:
            st.session_state.index = 0
            st.write("No font pairs available for the selected contrast level and locked fonts.")
        else:
            st.session_state.index = st.session_state.index % len(filtered_data)

            # Button to move to the next font pair
            if st.button("Next Font Pair ⏭️", key='next_font_pair'):
                st.session_state.index = (st.session_state.index + 1) % len(filtered_data)

            # Button to move to the previous font pair
            if st.button("Previous Font Pair ⏮️", key='prev_font_pair'):
                st.session_state.index = (st.session_state.index - 1) % len(filtered_data)
                if st.session_state.index < 0:
                    st.session_state.index = len(filtered_data) - 1


            while True:
                current_pair = filtered_data.iloc[st.session_state.index]
                font1_name = current_pair['Font1']
                font2_name = current_pair['Font2']

                try:
                    font1_path = get_font_path(font1_name)
                    font2_path = get_font_path(font2_name)
                    break
                except FileNotFoundError:
                    st.session_state.index = (st.session_state.index + 1) % len(filtered_data)
                    if st.session_state.index == 0:
                        st.write("No valid font pairs found.")
                        break

            # Display font pair information with hyperlinks to Google Fonts
            font1_url = get_google_fonts_url(font1_name)
            font2_url = get_google_fonts_url(font2_name)

            # Lock/unlock button for Font 1
            col_font1, col_lock1 = st.columns([4, 1])
            with col_font1:
                st.markdown(f"<a href='{font1_url}' style='font-size:19px;'>{font1_name}</a>", unsafe_allow_html=True)

            with col_lock1:
                font1_locked = st.session_state.locked_font1 == font1_name
                if st.button(f"{'🔒' if font1_locked else '🔓'}", key='lock_font1'):
                    if font1_locked:
                        st.session_state.locked_font1 = None
                    else:
                        st.session_state.locked_font1 = font1_name
                    st.rerun()

            # Lock/unlock button for Font 2
            col_font2, col_lock2 = st.columns([4, 1])
            with col_font2:
                st.markdown(f"<a href='{font2_url}' style='font-size:19px;'>{font2_name}</a>", unsafe_allow_html=True)

            with col_lock2:
                font2_locked = st.session_state.locked_font2 == font2_name
                if st.button(f"{'🔒' if font2_locked else '🔓'}", key='lock_font2'):
                    if font2_locked:
                        st.session_state.locked_font2 = None
                    else:
                        st.session_state.locked_font2 = font2_name
                    st.rerun()

            # Font size inputs for each font
            font1_size = st.slider("Select font size for Font 1", 10, 100, st.session_state.font1_size, key='font1_size_slider')
            font2_size = st.slider("Select font size for Font 2", 10, 100, st.session_state.font2_size, key='font2_size_slider')

            # Update session state with the slider values
            st.session_state.font1_size = font1_size
            st.session_state.font2_size = font2_size

            # Font color input
            font_color = st.color_picker('Pick A Font Color', value=st.session_state.font_color)
            st.session_state.font_color = font_color



            st.write("### Saved Font Pairs")
            if st.session_state.saved_pairs:
                for idx, pair in enumerate(st.session_state.saved_pairs):
                    st.write(f"Pair {idx + 1}: Font 1: [{pair['Font1']}]({get_google_fonts_url(pair['Font1'])}), Font 2: [{pair['Font2']}]({get_google_fonts_url(pair['Font2'])})")

            # Button to generate the shareable link
            # if st.button("Generate and Copy Shareable Link"):
            #     if st.session_state.locked_font1 and st.session_state.locked_font2:
            #         shareable_link = generate_shareable_link()
            #         st.text("Shareable Link:")
            #         st.write(shareable_link)
            #     else:
            #         st.warning("Please lock both Font 1 and Font 2 to generate the shareable link.")

            if current_user:
                project_name = st.text_input("Project Name", key='project_name')
                project_col1, project_col2 = st.columns([3, 1])
                with project_col2:
                    if st.button("Save 🔖", key='save_project'):
                        save_font_pair(font1_name, font2_name, project_name)

                comment = st.text_input("Add a comment", key='comment_text')
                comment_col1, comment_col2, comment_col3 = st.columns([3, 1, 1])
                with comment_col2:
                    if st.button("💬", key='comment_button'):
                        like_and_comment(font1_name, font2_name, comment)
                with comment_col3:
                    if st.button("❤️", key='like_button'):
                        like_and_comment(font1_name, font2_name, "")

            else:
                st.warning("Please sign in to save, like, and comment on font pairs.") 

    # Right column for font display
    if not filtered_data.empty:
        # Load the fonts in the HTML
        html_head = f"""
        <style>
            {embed_font(font1_path, font1_name)}
            {embed_font(font2_path, font2_name)}
        </style>
        """
        # Define HTML content for display
        html_content = f"""
        <div contenteditable="true" id="editable-text" 
        style="padding: 10px; 
               margin: 10px; 
               text-align: left; 
               min-height: 100px; /* Minimum height */
               max-height: 600px; /* Maximum height */
               overflow-y: auto; /* Enable vertical scroll if needed */
               width: 800px; 
               border: 2px solid #0e1117;
               color: {font_color}; /* Text color */">
            <p style="font-family: '{font1_name}'; 
                      font-size: {st.session_state.font1_size}px; 
                      color: {font_color};
                      margin: 10px 0;">
                {st.session_state.user_text}
            </p>
            <p style="font-family: '{font2_name}'; 
                      font-size: {st.session_state.font2_size}px; 
                      color: {font_color};
                      margin: 10px 0;">
                {st.session_state.user_text}
            </p>
        </div>

        <script>
            const editableDiv = document.getElementById('editable-text');

            // Function to adjust the height of the div based on input text
            function adjustHeight() {{
                const minHeight = 100; // Minimum height of the div
                const maxHeight = 600; // Maximum height of the div
                const scrollHeight = editableDiv.scrollHeight;
                editableDiv.style.height = 'auto'; // Reset height to auto to calculate actual height
                editableDiv.style.height = Math.min(maxHeight, Math.max(minHeight, scrollHeight)) + 'px'; // Set height within min and max bounds
            }}

            window.onload = function() {{
                adjustHeight();
            }};

            editableDiv.addEventListener('input', adjustHeight);
        </script>
        """

        # Combine the head and content and display it
        st.markdown(html_head + html_content, unsafe_allow_html=True)

        # Update session state with new text from JavaScript
        if 'new_text' in st.query_params:
            st.session_state.user_text = st.query_params['new_text'][0]

elif page == "🔍 Mood Based Pairs":
    # Import and run the font gallery page
    from font_gallery import font_gallery
    font_gallery()

elif page == "🖼️ Inspos":
    from inspo import inspo
    inspo()

elif page == "👤 User Account":
    st.title("User Account 👤")
    st.write("Manage your account and view your likes and comments.")

    if current_user:
        user_id = current_user['localId']
        st.write(f"Email: {current_user['email']}")
        if st.button("Sign out"):
            sign_out()
            st.rerun()

        st.subheader("Saved Font Pairs")
        user_font_pairs = fetch_user_font_pairs(user_id)
        if user_font_pairs:
            for pair in user_font_pairs:
                st.write(f"Font1: {pair['Font1']} | Font2: {pair['Font2']} | Project Name: {pair['ProjectName']}")
        else:
            st.write("You haven't saved any font pairs yet.")

        st.subheader("Your Likes and Comments")
        likes_comments = fetch_likes_comments(user_id)
        if likes_comments:
            for lc in likes_comments:
                st.write(f"Font1: {lc['Font1']} | Font2: {lc['Font2']} | Comment: {lc['Comment']}")
        else:
            st.write("You haven't liked or commented on any font pairs yet.")
    else:
        st.warning("Please sign in to view and manage your account.")

         # Authentication form
        auth_mode = st.radio("Choose authentication mode", ["Sign In", "Sign Up"])

        if auth_mode == "Sign In":
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Sign In"):
                sign_in(email, password)
                st.rerun()

        elif auth_mode == "Sign Up":
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Sign Up"):
                sign_up(email, password)
                st.rerun()

elif page == "🌐 Explore Multilingual Fonts":
    from lang import explore_multilingual_fonts
    explore_multilingual_fonts()

elif page == "🔀 Explore Multilingual Fusion":
    from fusion import explore_multilingual_fusion
    explore_multilingual_fusion()

elif page == "💡 Similar Font Recommender":
    from suggest import *
    main()  # Ensure that the 'suggest' module handles its own data without relying on 'filtered_data'
