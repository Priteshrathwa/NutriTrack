# NutriTrack - Food Nutrition Tracker

A Django web application that provides nutritional information for food items using Google's Gemini AI API.

## Features

- **Food Nutrition Lookup**: Get detailed nutritional information per 100g for any food item
- **AI-Powered Chatbot**: Ask nutrition-related questions and get expert advice
- **BMI Calculator**: Calculate and track Body Mass Index
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Django 5.2.7
- **AI Integration**: Google Gemini AI API
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Not required (uses Django's default setup for sessions only)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Priteshrathwa/NutriTrack
   cd NutriTrack
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   # On Windows
   myenv\Scripts\activate
   # On macOS/Linux
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-django-secret-key
   GEMINI_API_KEY=your-gemini-api-key
   DEBUG=True
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## API Keys

- Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Generate Django secret key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

## Project Structure

```
NutriTrack/
├── manage.py
├── requirements.txt
├── .env (create this)
├── NutriTrack/          # Main project settings
├── counter/             # Main app
│   ├── views.py         # Main views and nutrition lookup
│   ├── chatbot_views.py # AI chatbot functionality
│   ├── templates/       # HTML templates
│   └── ...
└── static/             # CSS, images, JS files
```

## Usage

1. **Nutrition Lookup**: Enter a food item to get detailed nutritional information
2. **AI Chatbot**: Ask questions about food, nutrition, and health
3. **BMI Calculator**: Calculate your Body Mass Index

## Contributing

This is a portfolio project. Feel free to fork and modify for your own use.

## License

This project is for educational and portfolio purposes.
