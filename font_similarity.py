import pandas as pd
import os

# Load the CSV file containing font pairs and their contrast levels
def load_font_pairs(filepath='shuffled_pairs.csv'):
    return pd.read_csv(filepath)

# Function to get font file path
def get_font_path(font_name, base_path='ofl'):
    font_folder = os.path.join(base_path, font_name.lower().replace(' ', ''))
    for file in os.listdir(font_folder):
        if file.endswith('.ttf'):
            return os.path.join(font_folder, file)
    return None
