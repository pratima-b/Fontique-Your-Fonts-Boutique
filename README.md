# Fontique - Your Fonts Boutique 🎨🔤

**"Discover the Perfect Font Pairings for Every Design!"**

Welcome to **Fontique**, an interactive font discovery and recommendation platform built with **Python and Streamlit**. Fontique helps designers, developers, and creators discover visually compatible font combinations based on **contrast, compatibility, readability, and design mood**.

Whether you're designing a website, mobile application, presentation, poster, or branding material, Fontique makes finding the right font combination easier and faster. ✨

## Features 🎉

### 🔤 Font Discovery

* **Explore Fonts:** Browse and discover a wide variety of fonts.
* **Font Pairing:** Find complementary font combinations suitable for different design requirements.
* **Visual Recommendations:** Get font suggestions based on compatibility and contrast.
* **Easy Exploration:** Interact with fonts through a simple and intuitive Streamlit interface.

### 🎨 Font Compatibility

Fontique evaluates font combinations using three important design criteria:

* **Contrast:** Helps create visual distinction between paired fonts.
* **Compatibility:** Identifies fonts that work well together.
* **Readability:** Ensures that font combinations remain easy to read and visually balanced.

### 🎭 Mood-Based Font Recommendations

Choose a design mood and discover fonts that match your desired visual style.

Available moods include:

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

### 🌐 Multilingual Font Support

Fontique also explores fonts suitable for different writing systems and multilingual design requirements, including **Indian scripts**.

This makes the platform useful for creating designs that require both aesthetic consistency and multilingual typography.

### 📊 Data-Driven Recommendations

Fontique uses font-pair data and similarity analysis to categorize font combinations into different contrast levels:

* **Very Similar**
* **Similar**
* **Balanced Contrast**
* **Moderate Contrast**
* **High Contrast**

The recommendation system is based on data-driven comparison of font characteristics.

### 🔐 Firebase Authentication

Fontique uses **Firebase Authentication** to provide user authentication and account management.

* User registration
* User login
* Email/password authentication
* Secure Firebase-based authentication

### ☁️ Cloud Firestore

Fontique uses **Cloud Firestore** for storing and managing application data.

This allows the application to maintain user-related information and provide a cloud-connected experience.

### 💻 Interactive Streamlit Interface

The application is built using **Streamlit**, providing an interactive web interface without requiring a separate frontend framework.

---

### Demo Video 🎥

[*Demo Video*](https://drive.google.com/file/d/1JZrqOGZBXSYmbWFH9_sKfaAbUzKnIk28/view?usp=drivesdk)

---

## Getting Started 🚀

### Prerequisites

Before running Fontique, make sure you have:

* **Python 3.10 or later**
* **pip**
* **Git**
* A **Firebase project**
* **Streamlit**

### Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   ```

2. **Navigate to the project directory:**

   ```bash
   cd fontique-master
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

4. **Activate the virtual environment:**

   **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Configure Firebase credentials** using Streamlit secrets.

7. **Run the application:**

   ```bash
   streamlit run app.py
   ```

The application will then open in your browser. 🌐

---

## Architecture 🏗️

Fontique follows a data-driven application architecture combining a **Streamlit frontend**, **Python-based recommendation logic**, and **Firebase backend services**.

### Application Flow

```text
User
  ↓
Streamlit Interface
  ↓
Font Selection / Preferences
  ↓
Font Recommendation Logic
  ↓
Font Pairing & Compatibility Analysis
  ↓
Recommended Font Combinations
  ↓
Firebase / Firestore
```

### Core Components

* **Streamlit:** User interface and application framework
* **Python:** Core application and recommendation logic
* **Pandas:** Dataset processing and analysis
* **NumPy:** Numerical and similarity calculations
* **Firebase Authentication:** User authentication
* **Cloud Firestore:** Cloud database
* **Font Dataset:** Font pairing and compatibility information

---

## Dataset 📊

Fontique uses font datasets to support its recommendation system.

### Font Pair Dataset

`font_pairs_contrast_levels.csv`

This dataset contains font-pair information along with their corresponding contrast categories.

Contrast categories include:

* Very Similar
* Similar
* Balanced Contrast
* Moderate Contrast
* High Contrast

### Google Fonts Dataset

`google-fonts.csv`

This dataset contains information related to available Google Fonts used by the application.

---

## Recommendation Criteria 🎯

Fontique focuses on three major principles when recommending font combinations:

| Criteria          | Purpose                                      |
| ----------------- | -------------------------------------------- |
| **Contrast**      | Creates visual distinction between fonts     |
| **Compatibility** | Determines whether fonts work well together  |
| **Readability**   | Ensures the combination remains easy to read |

These criteria help create font combinations that are both visually appealing and practical for real-world design.

---

## Technologies & Tools 🛠️

* **Python** - Core programming language
* **Streamlit** - Interactive web application framework
* **Pandas** - Data manipulation and analysis
* **NumPy** - Numerical computing
* **Pyrebase** - Firebase integration
* **Firebase Authentication** - User authentication
* **Cloud Firestore** - Database
* **Git & GitHub** - Version control and project collaboration

---

## Project Structure 📁

```text
Fontique/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── font_pairs_contrast_levels.csv
├── google-fonts.csv
│
└── .streamlit/
    └── secrets.toml
```

> **Note:** `secrets.toml` contains private Firebase credentials and should never be committed to GitHub.

---

## Security 🔐

Fontique uses Firebase services for authentication and database functionality.

Sensitive credentials should be stored using **Streamlit Secrets** instead of being hard-coded in the source code.

The following files should **never be uploaded to GitHub**:

```text
.streamlit/secrets.toml
*-firebase-adminsdk-*.json
.env
```

---

## Contributing 🤝

Contributions and improvements are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application.
5. Commit your changes.
6. Create a Pull Request.

---

## Future Improvements 🚀

Some potential future improvements for Fontique include:

* 🤖 AI-powered font recommendations
* 📈 Advanced font similarity visualization
* 🧠 Machine-learning-based font pairing
* 🔎 More advanced search and filtering
* 🌍 Expanded multilingual font support
* 🎨 Live font preview and comparison
* 📱 Improved responsive design
* ☁️ Enhanced cloud-based user preferences

---

## License 📄

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## Contact 📬

For questions, feedback, or collaboration opportunities, feel free to connect with the project contributors through GitHub.

---

**Fontique - Your Fonts Boutique** 🎨✨

*Discover. Pair. Design.*
