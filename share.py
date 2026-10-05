import streamlit as st
import urllib.parse

# Function to generate the shareable link
def generate_shareable_link():
    params = {
        'font1': st.session_state.locked_font1 or '',
        'font2': st.session_state.locked_font2 or '',
        'font1_size': st.session_state.font1_size,
        'font2_size': st.session_state.font2_size,
        'font_color': st.session_state.font_color,
        'user_text': st.session_state.user_text
    }
    query_string = urllib.parse.urlencode(params)
    shareable_link = f"{st.secrets['URL']}?{query_string}"
    return shareable_link

def load_query_params():
    params = st.query_params
    if 'font1' in params:
        st.session_state.locked_font1 = params['font1']
    if 'font2' in params:
        st.session_state.locked_font2 = params['font2']
    if 'font1_size' in params:
        st.session_state.font1_size = int(params['font1_size'])
    if 'font2_size' in params:
        st.session_state.font2_size = int(params['font2_size'])

    if 'font_color' in params:
        st.session_state.font_color = params['font_color']
    if 'user_text' in params:
        st.session_state.user_text = params['user_text']