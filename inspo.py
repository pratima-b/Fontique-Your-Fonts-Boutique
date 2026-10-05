import streamlit as st
import pandas as pd
import base64


st.title("Inspos 🖼️")

def inspo(csv_path='shuffled_mood.csv'):
    # Load CSV data
    data = pd.read_csv(csv_path)

    # Define background images for each mood
    mood_backgrounds = {
        'Casual': r'bgs/bg_casual.jpg',
        'Elegant': r'bgs/bg_elegant.jpg',
        'Modern': r'bgs/bg_modern.jpg',
        'Playful': r'bgs/bg_playful.jpg',
        'Formal': r'bgs/bg_formal.jpg',
        'Retro': r'bgs/bg_retro.jpg',
        'Tech': r'bgs/bg_tech.jpg',
        'Creative': r'bgs/bg_creative.jpg',
        'Vintage': r'bgs/bg_vintage.jpg',
        'Futuristic': r'bgs/bg_futuristic.jpg',
        'Neutral': r'bgs/bg_neutral.jpg',
    }

    # Sample texts for each mood
    sample_texts = {
        'Casual': {
            'text1': {
                'content': "Unlock Your Style",
                'size': '100px',
                'color': 'black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "With all of the biggest names in fashion, you'll be amazed to find the best designer clothes.",
                'size': '30px',
                'color': 'black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Elegant': {
            'text1': {
                'content': "Elegant & Luxury",
                'size': '100px',
                'color': 'white',
                'alignment': 'right',
                'margin_left': '20px',
                'margin_right': '80px'
            },
            'text2': {
                'content': "Remarkable jewelery for the modern women",
                'size': '30px',
                'color': 'white',
                'alignment': 'right',
                'margin_left': '20px',
                'margin_right': '80px'
            }
        },
        'Modern': {
            'text1': {
                'content': "Empower Your Financial Future",
                'size': '60px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Discover Seamless Banking Solutions Designed for Your Digital Lifestyle",
                'size': '30px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Playful': {
            'text1': {
                'content': "Whimsy Express",
                'size': '60px',
                'color': '#915733',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Sending Smiles Worldwide with Our Playful Mailing and Courier Services",
                'size': '30px',
                'color': '#915733',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Formal': {
            'text1': {
                'content': "Elite Real Estate",
                'size': '60px',
                'color': 'black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Discover unparalleled service and exquisite properties. Our dedicated team brings a wealth of expertise and a commitment to excellence, ensuring every client receives personalized attention and seamless transactions.",
                'size': '20px',
                'color': 'black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Retro': {
            'text1': {
                'content': "RetroTicket, Relive the Nostalgia of Movie Magic",
                'size': '60px',
                'color': '#800059',
                'alignment': 'center',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Your portal to vintage cinema experiences. Book tickets for classic films in historic theaters, with a touch of old-school charm and modern convenience.",
                'size': '30px',
                'color': '#800059',
                'alignment': 'center',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Tech': {
            'text1': {
                'content': "NextGen Credit Cards",
                'size': '80px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Join the future of banking with our range of smart credit solutions, crafted to meet the needs of today's digital-savvy consumers.",
                'size': '20px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Creative': {
            'text1': {
                'content': "Sparkle: Ignite Your Creativity",
                'size': '80px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "The innovative social media app designed to inspire and connect creative minds",
                'size': '30px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Vintage': {
            'text1': {
                'content': "Echoes of Time",
                'size': '80px',
                'color': 'white',
                'alignment': 'center',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Explore the Charm and Nostalgia of Yesteryear Through Captivating Images",
                'size': '30px',
                'color': 'white',
                'alignment': 'center',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Futuristic': {
            'text1': {
                'content': "MetaVerse Nexus",
                'size': '80px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Step into a Virtual World of Infinite Possibilities and Boundless Adventure",
                'size': '20px',
                'color': 'white',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        },
        'Neutral': {
            'text1': {
                'content': "Natural Skincare",
                'size': '80px',
                'color': 'Black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            },
            'text2': {
                'content': "Discover our product line.",
                'size': '30px',
                'color': 'Black',
                'alignment': 'left',
                'margin_left': '20px',
                'margin_right': '20px'
            }
        }    
    }

    # Function to load a local image and encode it to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_bg_div(main_bg, index, sample_text1, sample_text2, current_pair, mood):
        bin_str = get_base64_of_bin_file(main_bg)
        font1_url = f"https://fonts.googleapis.com/css2?family={current_pair['Font1'].replace(' ', '+')}&display=swap"
        font2_url = f"https://fonts.googleapis.com/css2?family={current_pair['Font2'].replace(' ', '+')}&display=swap"
        text1 = sample_texts[mood]['text1']
        text2 = sample_texts[mood]['text2']
        text1_style = f"font-size: {text1['size']}; color: {text1['color']}; text-align: {text1['alignment']}; margin-left: {text1['margin_left']}; margin-right: {text1['margin_right']};"
        text2_style = f"font-size: {text2['size']}; color: {text2['color']}; text-align: {text2['alignment']}; margin-left: {text2['margin_left']}; margin-right: {text2['margin_right']};"
        text1_content = text1['content'].replace(',', ',<br>')
        text2_content = text2['content'].replace(',', ',<br>')
        page_bg_img = f'''
        <style>
        @import url('{font1_url}');
        @import url('{font2_url}');
        .bg-img-{index} {{
            position: relative;
            width: 100%;
            height: 100vh; 
            background: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-bottom: 20px;
        }}
        .mood-name-{index} {{
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 40px;
            color: white;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 10px;
        }}
        .content-{index} {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 100%;
            padding: 20px;
            z-index: 1; /* Ensure content is above buttons */
        }}
        .text1-{index} {{
            {text1_style}
            font-family: '{current_pair['Font1']}';
        }}
        .text2-{index} {{
            {text2_style}
            font-family: '{current_pair['Font2']}';
        }}
        .font-name-{index} {{
            font-size: 30px;
            color: white;
            margin: 10px 0 0 0;
            
        }}
        .button-container-{index} {{
            position: absolute;
            bottom: 20px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 20px;
            z-index: 1; /* Ensure buttons are above background */
        }}
        .button-container-{index} .custom-button {{
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }}
        .button-container-{index} .custom-button:hover {{
            background-color: #0056b3;  /* Darker shade of primary color on hover */
        }}
        </style>
    
        <div class="bg-img-{index}">
            <div class="mood-name-{index}">
                {mood}
            <p class="font-name-{index}">{current_pair['Font1']} + {current_pair['Font2']}</p>
            </div>
        <div class="content-{index}">
                <p class="text1-{index}">{text1_content}</p>
                <p class="text2-{index}">{text2_content}</p>
            </div>
        </div>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

    # Initialize session state for each mood
    if 'indices' not in st.session_state:
        st.session_state.indices = {mood: 0 for mood in mood_backgrounds.keys()}

    # Function to get the current index for a given mood
    def get_current_index(mood):
        return st.session_state.indices.get(mood, 0)

    # Function to set the current index for a given mood
    def set_current_index(mood, index):
        st.session_state.indices[mood] = index

    # Function to go to the next pair
    def next_pair(mood):
        current_index = get_current_index(mood)
        current_index += 1
        mood_data = data[data['mood'] == mood]
        if current_index >= len(mood_data):
            current_index = 0
        set_current_index(mood, current_index)

    # Function to go to the previous pair
    def previous_pair(mood):
        current_index = get_current_index(mood)
        current_index -= 1
        mood_data = data[data['mood'] == mood]
        if current_index < 0:
            current_index = len(mood_data) - 1
        set_current_index(mood, current_index)

    # Handling button clicks via query parameters
    query_params = st.query_params
    for mood in mood_backgrounds.keys():
        if f"next_{mood}" in query_params:
            next_pair(mood)
            st.experimental_set_query_params()  # Clear the query params
        elif f"previous_{mood}" in query_params:
            previous_pair(mood)
            st.experimental_set_query_params()  # Clear the query params

    # Inject custom CSS to modify the width of the default container
    st.markdown('''
        <style>
        .block-container {
            max-width: 100%; /* Set to 100% or any desired width */
            padding-left: 10px;
            padding-right: 10px;
        }
        </style>
    ''', unsafe_allow_html=True)

    # Display sections for each mood
    for index, (mood, bg_image) in enumerate(mood_backgrounds.items()):
        mood_data = data[data['mood'] == mood]
        if not mood_data.empty:
            current_index = get_current_index(mood)
            current_pair = mood_data.iloc[current_index]
            sample_text1 = sample_texts[mood]['text1']
            sample_text2 = sample_texts[mood]['text2']
            set_bg_div(bg_image, index, sample_text1, sample_text2, current_pair, mood)
            # Add Streamlit buttons for navigation
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"Previous {mood}"):
                    previous_pair(mood)
            with col2:
                if st.button(f"Next {mood}"):
                    next_pair(mood)
        else:
            st.write(f"No font pairs available for the mood: {mood}")

# Example usage
if __name__ == "__main__":
    inspo()
