# Reddit User Persona Generator

An AI-powered tool that analyzes Reddit user activity and generates detailed personality profiles using Google's Gemini AI.
                                              
## Features

- **Reddit Data Scraping**: Extracts posts and comments from any Reddit user
- **AI Analysis**: Uses Google Gemini to analyze user behavior and generate personas
- **Web Interface**: Clean Streamlit web app for easy interaction
- **Detailed Profiles**: Generates comprehensive personas including personality traits, interests, and communication style
- **Evidence-Based**: All traits are backed by specific Reddit posts/comments with links

## Prerequisites

- Python 3.8+
- Reddit API credentials
- Google Gemini API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sujan22359/reddit_scraper.git
   cd reddit_scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API credentials**
   Create a `.env` file in the project root:
   ```env
   CLIENT_ID="your_reddit_client_id"
   CLIENT_SECRET="your_reddit_client_secret"
   USER_AGENT="your_app_name by u/yourusername"
   GEMINI_API_KEY="your_gemini_api_key"
   ```

## API Setup

### Reddit API
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create a new "script" application
3. Note the client ID and secret

### Google Gemini API
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create an API key
3. Add it to your `.env` file

## Usage

### Web Interface
```bash
streamlit run streamlit_app.py
```
Then open http://localhost:8501 in your browser.



### Command Line
```bash
python generate_persona.py
```

