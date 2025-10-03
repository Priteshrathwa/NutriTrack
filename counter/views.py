from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


# Initialize the Gemini model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "temperature": 0.55,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2000,
        "response_mime_type": "text/plain",
    },
    system_instruction = """ Give values per 100 grams for food items in format JSON  without markdown formatting or backticks:
    {"name": "item name",
    "carbohydrate": "int amount",
    "cholesterol": "int amount",
    "fiber": "int amount",
    "calorie": "int amount",
    "protein": "int amount",
    "saturated_fat":"int amount",
    "total_fats":"int amount",
    "sugar": "int amount",
    "sodium": "int amount",
    "potassium": "int amount"} end
    if input is other than any food item return none

    Example:
        Input: Rice
        Output:
        {
        "name": "Rice",
        "carbohydrate": 28.17,
        "cholesterol": 0,
        "fiber": 0.4,
        "calorie": 130,
        "protein": 2.69,
        "saturated_fat":0.57
        "total_fats": 0.28,
        "sugar": 0.05,
        "sodium": 1,
        "potassium": 35
    }
    
"""
    )




@csrf_exempt
def home(request):
    api = None  # Initialize api variable to avoid reference errors in templates

    if 'query' in request.POST:
        user_input = request.POST['query']
        
        try:
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(user_input)
            api = response.text if hasattr(response, "text") else "Sorry, I couldn't understand."
            print(api)
            # Convert JSON string to dictionary if the response is valid JSON
            try:
                api = json.loads(api)
                print(api)
                
            except json.JSONDecodeError:
                print("Response is not a valid JSON string")
                api = "enter valid item"

        except Exception as e:
            api = f"oops! There was an error {str(e)}"
            print(f"Gemini API Error: {e}")

    return render(request, 'home.html', {'api': api})
