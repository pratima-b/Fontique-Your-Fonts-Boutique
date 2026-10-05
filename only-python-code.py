import pandas as pd
from font_similarity import load_font_pairs, get_font_path

# Load the font pairs data
def load_data():
    return load_font_pairs()

# Load data
font_data = load_data()

# Initialize session state (mocked for non-UI environment)
session_state = {
    'index': 0,
    'locked_font1': None,
    'locked_font2': None,
    'user_text': "This is a sample text",
    'font1_size': 60,
    'font2_size': 40,
    'text_align': 'left',
    'gradient_color': ("#101016", "#101016"),  # Default gradient colors
    'background_color': "",  # Default background color
    'saved_pairs': []  # List to store saved font pairs
}

# Mock functions to simulate user interface actions
def select_contrast_level(contrast_levels, default_level):
    return default_level

def get_next_font_pair_index(current_index, total_pairs):
    return (current_index + 1) % total_pairs

def update_session_state(key, value):
    session_state[key] = value

def lock_unlock_font(font_name, current_lock):
    return None if current_lock == font_name else font_name

def save_font_pair(font1_name, font2_name):
    saved_pair = {'Font1': font1_name, 'Font2': font2_name}
    if saved_pair not in session_state['saved_pairs']:
        session_state['saved_pairs'].append(saved_pair)
        return "Font pair saved!"
    else:
        return "Font pair already saved!"

# Simulate loading contrast levels and selecting a level
contrast_levels = font_data['Contrast Level'].unique()
selected_level = select_contrast_level(contrast_levels, contrast_levels[0])

# Filter data based on selected contrast level
filtered_data = font_data[font_data['Contrast Level'] == selected_level]

# If Font 1 or Font 2 is locked, filter the data to only include pairs containing the locked font(s)
if session_state['locked_font1']:
    filtered_data = filtered_data[(filtered_data['Font1'] == session_state['locked_font1']) | (filtered_data['Font2'] == session_state['locked_font1'])]
if session_state['locked_font2']:
    filtered_data = filtered_data[(filtered_data['Font1'] == session_state['locked_font2']) | (filtered_data['Font2'] == session_state['locked_font2'])]

# Ensure index is within bounds
if len(filtered_data) == 0:
    session_state['index'] = 0
    print("No font pairs available for the selected contrast level and locked fonts.")
else:
    session_state['index'] = session_state['index'] % len(filtered_data)

    # Simulate button press to move to the next font pair
    session_state['index'] = get_next_font_pair_index(session_state['index'], len(filtered_data))

    current_pair = filtered_data.iloc[session_state['index']]
    font1_name = current_pair['Font1']
    font2_name = current_pair['Font2']

    font1_path = get_font_path(font1_name)
    font2_path = get_font_path(font2_name)

    # Lock/unlock Font 1
    session_state['locked_font1'] = lock_unlock_font(font1_name, session_state['locked_font1'])

    # Lock/unlock Font 2
    session_state['locked_font2'] = lock_unlock_font(font2_name, session_state['locked_font2'])

    # Simulate saving font pair
    save_message = save_font_pair(font1_name, font2_name)
    print(save_message)

# Display saved font pairs
print("Saved Font Pairs:")
for idx, pair in enumerate(session_state['saved_pairs']):
    print(f"Pair {idx + 1}: Font 1: {pair['Font1']}, Font 2: {pair['Font2']}")

# Mock function to embed font in HTML
def embed_font(font_path, font_name):
    import base64
    with open(font_path, "rb") as font_file:
        encoded_font = base64.b64encode(font_file.read()).decode("utf-8")
    return f"@font-face {{ font-family: '{font_name}'; src: url(data:font/ttf;base64,{encoded_font}) format('truetype'); }}"

# Generate HTML for font display (without UI)
html_head = f"""
<style>
    {embed_font(font1_path, font1_name)}
    {embed_font(font2_path, font2_name)}
</style>
"""

html_content = f"""
<div contenteditable="true" id="editable-text" style="background: {session_state['background_color']}; 
                                                    background-image: linear-gradient(to right, {session_state['gradient_color'][0]}, {session_state['gradient_color'][1]}); 
                                                    padding: 10px; 
                                                    text-align: {session_state['text_align']}; 
                                                    min-height: 100px; 
                                                    max-height: 600px; 
                                                    overflow-y: auto; 
                                                    width: 800px; 
                                                    color: #ffffff;">
    <p style="font-family: '{font1_name}'; 
              font-size: {session_state['font1_size']}px; 
              color: #ffffff; 
              margin: 10px 0;">
        {session_state['user_text']}
    </p>
    <p style="font-family: '{font2_name}'; 
              font-size: {session_state['font2_size']}px; 
              color: #ffffff; 
              margin: 10px 0;">
        {session_state['user_text']}
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

    // Call the function to adjust height when the page loads
    window.onload = function() {{
        adjustHeight();
    }};

    // Listen for input events to adjust height dynamically
    editableDiv.addEventListener('input', adjustHeight);
</script>
"""

# Combine the head and content
html_output = html_head + html_content

# Display HTML (this would be rendered in a browser or UI)
print(html_output)
