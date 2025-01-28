from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn

app = FastAPI(title="DunamisMax")

# Mount static files
app.mount(
    "/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static"
)

# Templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "services": [
                {
                    "name": "Messenger",
                    "description": "Real-time chat application using WebSocket technology",
                    "url": "https://messenger.dunamismax.com",
                    "icon": "message-square",
                }
                # Add more services here as they become available
            ],
        },
    )


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
