# Fontique — Your Fonts Boutique

Fontique is a font discovery and recommendation web application built with **Python and Streamlit**. It helps users explore fonts and discover font combinations based on contrast, compatibility, readability, and design mood.

The application also provides **Firebase Authentication** for user registration and login, along with **Cloud Firestore** for backend data storage.

## Features

* Explore and discover fonts
* Find complementary font combinations
* Analyze font contrast and compatibility
* Font recommendations based on visual characteristics
* Font categories based on design moods
* Support for multiple languages and scripts
* Firebase email/password authentication
* Cloud Firestore integration
* Interactive Streamlit interface

## Tech Stack

* **Python**
* **Streamlit**
* **NumPy**
* **Pandas**
* **Pyrebase**
* **Firebase Authentication**
* **Firebase Admin SDK**
* **Cloud Firestore**
* **Git & GitHub**

## Font Recommendation

Fontique evaluates font combinations using three main criteria:

### Contrast

Font pairs are categorized according to their visual contrast:

* Very Similar
* Similar
* Balanced Contrast
* Moderate Contrast
* High Contrast

### Compatibility

The application evaluates how well two fonts work together as a combination rather than simply selecting fonts that look different.

### Readability

Recommendations consider whether the selected font combination remains readable and practical for real-world design applications.

## Font Moods

Fontique supports different visual moods, including:

* Casual
* Elegant
* Modern
* Playful
* Formal
* Retro
* Tech
* Creative
* Vintage
* Futuristic
* Neutral

## Authentication

Fontique uses Firebase Authentication to provide:

* User registration
* User login
* User logout
* Authentication session management

Cloud Firestore is used for application data storage.

## Dataset

The application uses font-related datasets for its recommendation system.

Example datasets include:

```text
font_pairs_contrast_levels.csv
google-fonts.csv
```

The font-pair dataset contains font combinations and their corresponding contrast categories.

## Project Structure

```text
Fontique/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── data/
    ├── font_pairs_contrast_levels.csv
    └── google-fonts.csv
```

The exact structure may vary depending on the current version of the project.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pratima-b/Fontique-Your-Fonts-Boutique.git
```

### 2. Open the project

```bash
cd Fontique-Your-Fonts-Boutique
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## Firebase Configuration

Fontique uses Firebase for authentication and backend services.

Firebase configuration should be stored using Streamlit secrets:

```text
.streamlit/secrets.toml
```

**Do not commit this file to GitHub.**

Firebase Admin SDK service-account JSON files should also never be uploaded to the repository.

## Run the Application

Start Fontique using:

```powershell
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## Security

The following files should never be committed to GitHub:

```text
.streamlit/secrets.toml
.env
*-firebase-adminsdk-*.json
```

These files may contain sensitive credentials.

## Future Development

Potential improvements include:

* Improved font recommendation algorithms
* More multilingual font support
* Advanced font similarity analysis
* Personalized font recommendations
* Additional typography categories
* Improved UI/UX
* More font datasets
* Deployment improvements

## Author

**Pratima Bombe**

GitHub: https://github.com/pratima-b

## License

This project is intended for educational and development purposes.
