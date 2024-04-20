from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

project_id = "nstnocode-ejdvshjzvz"
location = "us-central1"
vertexai.init(project=project_id, location=location)
model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()


def home(requests):
    return render(requests, "index.html")


def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

# print(get_chat_response(chat, "hi"))

def texting(request):
    if request.method == "POST":
        our_prompt = request.POST.get("prompt")  # Use get method to avoid KeyError
        response = get_chat_response(chat, our_prompt)
        return JsonResponse({"response": response})  # Return a dictionary with the response
    return JsonResponse({"error": "Bad Request"}, status=400)  # Return error response if method is not POST}