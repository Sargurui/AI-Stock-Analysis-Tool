from google.generativeai import GenerativeModel
from config import GEMINI_API_KEY
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat_session = gemini_model.start_chat(history=[])

def generate_response(query, retrieved_docs, chat_history):
    context = "\n".join(f"{k}: {v}" for k, v in retrieved_docs.items())
    prompt = f"""
    You are an intelligent financial analyst tasked with checking and analyzing a company's financial data and technical indicators.
    Based on the following data, evaluate the financial health, growth potential, and technical trend of the stock. 
    Provide a clear recommendation: Should I invest in this stock or not? Justify your answer.

    Data:
    {context}

    Previous Discussion History (if any):
    {chat_history}

    Question:
    {query}
    """
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        print("Error generating response:", e)
        return "Could not generate a response."
