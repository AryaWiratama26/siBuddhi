from groq import Groq
from database import add_questions
import os
from dotenv import load_dotenv

load_dotenv()
AI_API_KEY = os.getenv("AI_API_KEY")

def ask_bot(question):
    client = Groq(api_key=AI_API_KEY)

    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a buddhist psychologist."
            },
            {
                "role": "user",
                "content": "Berikan nasihat psikologi berdasarkan kita suci agama buddha (Dhammapada) tentang: {question}",
            }
        ],

        model="llama-3.3-70b-versatile",

        temperature=0.5,
        stop=None,
        stream=False,
    )

    answer = chat_completion.choices[0].message.content
    
    add_questions(question, answer)
    
    return answer

