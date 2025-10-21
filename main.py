import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

client = InferenceClient(
    provider="novita",      # HF Inference API provider
    api_key=os.environ["HF_TOKEN"],
)

@app.get("/", response_class=HTMLResponse)
def instant2():
    # Dummy user message
    message = "What is happiness?"

    # Call the model
    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2-Exp",
        messages=[{"role": "user", "content": message}],
    )

    # Extract the model reply
    reply = completion.choices[0].message["content"].replace("\n", "<br/>")

    # Return HTML page
    html = f"""
    <html>
        <head><title>Live in an Instant!</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>{reply}</h2>
        </body>
    </html>
    """
    return html
