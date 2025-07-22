from fastapi import FastAPI, Request
from profile.student_router import router as student_router
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Career LMS API")

# Determine paths relative to the main.py file
backend_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(backend_dir)
frontend_dir = os.path.join(root_dir, "frontend")

# Mount static files from the frontend directory
app.mount("/static", StaticFiles(directory=os.path.join(frontend_dir, "static")), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory=os.path.join(frontend_dir, "templates"))

app.include_router(student_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})