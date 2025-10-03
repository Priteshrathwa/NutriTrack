from django.http import JsonResponse
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import re
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@xframe_options_exempt
def chathome(request):
    return render(request, "chatbot.html")

def format_response(text):
    """Converts plain text to formatted HTML."""
    text = re.sub(r'\*(.*?)\*', r'<b>\1</b>', text)  # Bold formatting
    text = text.replace("\n", "<br>")  # New lines to <br>
    return text


# Initialize the Gemini model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0.55,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2000,
        "response_mime_type": "text/plain",
    },
    system_instruction=(
        "Act as a food and nutrition expert. Answer queries about food, health, and nutrition "
        "in a well-structured manner with headings, bullet points, and concise explanations. "
        "Ensure clarity and readability in the response. Keep responses short and to the point."
    )
)


@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()

        if not user_message:
            return JsonResponse({"message": "Please enter a valid query."})

        try:
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(user_message)

            bot_response = response.text if hasattr(response, "text") else "I'm not sure about that."
            bot_response = format_response(bot_response)  # Apply formatting

        except Exception as e:
            bot_response = "Oops! Something went wrong."
            print(f"Chatbot Error: {e}")

        return JsonResponse({"message": bot_response})

    return JsonResponse({"message": "Invalid request method."})