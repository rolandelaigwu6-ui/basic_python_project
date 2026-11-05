import os

from google import genai

client = genai.Client()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

response = client.models.generate_content(
    model=MODEL,
    contents="""
    explain what every code here does 
    """,
)

# print(response.text)
with open("api.txt", "a") as file:
    content = file.write(response.text)
    print("write to api file sucessfully")
