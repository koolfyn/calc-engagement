from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


async def generate_response(
        prompt: str,
        model: str
):

    response = client.chat.completions.create(

        model=model,

        messages=[
            {
                "role":"system",
                "content":"Welcome to another Calc BC tutoring session today!"
            },

            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
