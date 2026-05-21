from pathlib import Path

from openai import AuthenticationError, OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

api_key = os.getenv("OPENROUTER_API_KEY", "").strip()

if not api_key:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set. Add it to the project .env file or your environment before running main.py."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


async def generate_response(
        prompt: str,
        model: str
):

    try:
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
    except AuthenticationError as error:
        raise RuntimeError(
            "OpenRouter rejected the API key with a 401. Verify that OPENROUTER_API_KEY is correct, active, and belongs to your OpenRouter account."
        ) from error

    return response.choices[0].message.content
