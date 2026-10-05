import streamlit as st
import time

# Inject custom CSS to modify the width of the default container, background color, and height
st.markdown('''
    <style>
    .block-container {
        max-width: 100%; /* Set to 100% or any desired width */
        padding-left: 10px;
        padding-right: 10px;
    }
    .pink-div {
    background-image: linear-gradient(to bottom right, pink, lightcoral);
    padding: 20px;
    border-radius: 5px;
    margin-bottom: 20px;
    height: 700px; /* Set to any desired height */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
}

    .pink-content {
        text-align: center;
        color: white;
        font-size: 80px;
        position: relative;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .pink-button {
        background-color: #ff007f;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        bottom: 100px;
    }
    </style>
''', unsafe_allow_html=True)

# Create the pink div and include a placeholder inside it
placeholder = st.empty()

def render_div():
    placeholder.markdown('''
        <div class="pink-div">
            <div class="pink-content" id="content-placeholder">
                <!-- Dynamic content will be placed here -->
            </div>
            <button class="pink-button">Get Started !</button>
        </div>
    ''', unsafe_allow_html=True)

# Render the initial div
render_div()

# Define the words and their colors
words = [("Designer", "red"), ("Developer", "green"), ("App", "blue"), ("Web Design", "orange")]

# Loop to display each word with a delay
while True:
    for word, color in words:
        # Update the dynamic content within the div
        content_html = f'''
        <div class="pink-div">
            <div class="pink-content" id="content-placeholder" style="color: {color};">
                {word}
            </div>
            <button class="pink-button">Click me</button>
        </div>
        '''
        placeholder.markdown(content_html, unsafe_allow_html=True)
        time.sleep(2)
