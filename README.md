# 🧠 Reddit User Persona Generator

An AI-powered tool that analyzes Reddit user activity and generates detailed personality profiles using Google's Gemini AI.

## 🌟 Features

- **Reddit Data Scraping**: Extracts posts and comments from any Reddit user
- **AI Analysis**: Uses Google Gemini to analyze user behavior and generate personas
- **Web Interface**: Clean Streamlit web app for easy interaction
- **Detailed Profiles**: Generates comprehensive personas including personality traits, interests, and communication style
- **Evidence-Based**: All traits are backed by specific Reddit posts/comments with links
- **Export Options**: Download generated personas as formatted text files

## 🚀 Demo

The tool generates detailed user personas like this example:

**"The Disillusioned Urbanite"**
- Age: 30-35 (estimated)
- Interests: Tech, Finance, NYC Culture, Plants
- Personality: Reflective, analytical, tech-savvy
- Communication: Thoughtful and introspective writing style

## 📋 Prerequisites

- Python 3.8+
- Reddit API credentials
- Google Gemini API key

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/reddit-persona-generator.git
   cd reddit-persona-generator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API credentials**
   Create a `.env` file in the project root:
   ```env
   CLIENT_ID="your_reddit_client_id"
   CLIENT_SECRET="your_reddit_client_secret"
   USER_AGENT="your_app_name by u/yourusername"
   GEMINI_API_KEY="your_gemini_api_key"
   ```

## 🔑 API Setup

### Reddit API
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create a new "script" application
3. Note the client ID and secret

### Google Gemini API
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create an API key
3. Add it to your `.env` file

## 🖥️ Usage

### Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```
Then open http://localhost:8501 in your browser.

### Command Line
```bash
python generate_persona.py https://reddit.com/u/username
```

### Programmatic Usage
```python
from reddit_scraper import scrape_user_content
from generate_persona import generate_persona

# Scrape user data
data = scrape_user_content("username")

# Generate persona
persona = generate_persona(data['posts'], data['comments'])
print(persona)
```

## 📁 Project Structure

```
reddit-persona-generator/
├── streamlit_app.py          # Web interface
├── generate_persona.py       # Main persona generation script
├── reddit_scraper.py         # Reddit API integration
├── persona_generator.py      # Legacy persona generator
├── requirements.txt          # Python dependencies
├── .env                     # API credentials (create this)
├── outputs/                 # Generated persona files
│   └── username_persona.txt
└── README.md               # This file
```

## 🛠️ Core Components

- **`reddit_scraper.py`**: Handles Reddit API authentication and data extraction
- **`generate_persona.py`**: Main script with AI integration and file operations
- **`streamlit_app.py`**: Web interface for user-friendly interaction
- **`persona_generator.py`**: Contains the AI prompt formatting and analysis logic

## 📊 Sample Output

The tool generates detailed personas with sections like:

- **Demographics**: Age, location estimates
- **Interests**: Hobbies, topics of interest
- **Personality**: Communication style, traits
- **Social Views**: Political leanings, social consciousness
- **Evidence**: Specific Reddit posts supporting each conclusion

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes. Always respect user privacy and Reddit's terms of service. The generated personas are AI interpretations and may not reflect actual user characteristics.

## 🐛 Known Issues

- Rate limiting may occur with high-volume requests
- API keys need to be kept secure and not committed to version control
- Some Reddit profiles may have limited public data

## 🔮 Future Enhancements

- [ ] Support for multiple AI models
- [ ] Batch processing of multiple users
- [ ] Advanced filtering options
- [ ] Export to different formats (JSON, PDF)
- [ ] Visualization of personality traits
- [ ] Integration with other social media platforms

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/reddit-persona-generator/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**Made with ❤️ and AI**
