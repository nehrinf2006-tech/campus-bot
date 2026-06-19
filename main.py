from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Request model
class Prompt(BaseModel):
    message: str

# Test route
@app.get("/")
def home():
    return {"message": "Campus Bot API is running!"}


# Chat route
@app.post("/chat")
def chat(data: Prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are a helpful college assistant for
                Sree Narayana College of Engineering.

                College Details:
                - Name: Sree Narayana College of Engineering
                - Location: Kerala, India
                - Engineering and Technology courses
                - Admissions support
                - Placement support
                - Campus information

                Answer politely and clearly.
                """
            },
            {
                "role": "user",
                "content": data.message
            }
        ]
    )

    return {
       "reply": response.choices[0].message.content
    }