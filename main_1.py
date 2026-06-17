# this is t0o show how human readable response can be returned

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/", response_class = HTMLResponse, include_in_schema= False) # we can make this route disappear from the docs by using include_in_schema = False
@app.get("/posts", response_class = HTMLResponse)
def home():
    return f"<h1>{posts[1]['title']}</h1>"