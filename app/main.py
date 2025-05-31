from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

with open("app/templates/index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

@app.get("/", response_class=HTMLResponse)
def root():
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
    