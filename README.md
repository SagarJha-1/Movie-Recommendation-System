# 🎬 Movie Recommendation System

 **Movie Recommendation System** is your personal movie buddy! Built with **Flask** and **Jinja2**, it provides **personalized movie suggestions** using **content-based filtering** and **Jaccard similarity**.
 - Utilizes flask as a backend
 - Jinja2 templating with embedded html and css for frontend
 - Mysql for Storing user and watchlist data
 - Movies data are managed through CSV file

---

## 🔥 Features
- Personalized **movie recommendations** based on user input.  
- **Watchlist management:** add or remove movies.  
- **Upload & delete movies** (user-contributed database).  
- **Detailed movie info** with posters and overviews.  
- **Secure authentication:** register, login, and profile management.  
- Responsive **UI with Jinja2 templates** for a smooth experience.  

---

## 🎬 Demo

For demo run this project in your Local Machine 

---

## 🛠 Tech Stack
- **Backend:** Python + Flask  
- **Frontend:** Jinja2 templates, HTML, CSS  
- **Database:** MySQL via SQLAlchemy  
- **Data Storage:** CSV files (`movies.csv`, `movie_images.csv`)  
- **Key Libraries:**  
  - `pandas` – CSV handling  
  - `fuzzywuzzy` – string similarity  
  - `Pillow` – image processing  
  - `Flask-WTF` – form validation  
  - `bcrypt` – password hashing  

---

## ⚙ Installation

1. **Clone the repository:**

git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

2. **Create the virtual Environment:**
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   
3. **Install dependencies:**
   pip install -r requirements.txt

4. **Set up MySQL Database:**
   Requires two tables: User and Watchlist

5. **Run the app:**
   python run.py


