from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
import logging


app = FastAPI()
logger = logging.getLogger("uvicorn")

@app.get("/", response_class=HTMLResponse)
# def instant2():
#     client = OpenAI()
#     message = """
# You are on a website that has just been deployed to production for the first time!
# Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
# """
#     messages = [{"role": "user", "content": message}]
#     response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
#     reply = response.choices[0].message.content.replace("\n", "<br/>")
#     html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
#     return html

def instant():
    logger.info("Instant2 is working")

    # Dummy message instead of calling OpenAI
    dummy_reply = (
        "🎉 Welcome to our brand new website!<br/>"
        "We’re thrilled to announce that it’s live in production for the very first time.<br/>"
        "Explore, enjoy, and share your feedback with us!"
    )

    html = f"""
    <html>
        <head><title>Live in an Instant!</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>{dummy_reply}</h2>
        </body>
    </html>
    """

    return html