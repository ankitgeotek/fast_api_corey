from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)
def home():
    # return {"message": "Hello World"}
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/test")
def test_home():
    return {'message': 'Testing the home route'}

posts: list[dict] = [
    {
        "id" : 1,
        "author": "corey scocher",
        "title": "FastApi is Awesone",
        "content" : "This is a framework that help us to build application easily",
        "date_posted": "April 20 2025"
    },
    {
        "id" : 2,
        "author": "Ankit",
        "title": "FastApi is Awesone",
        "content" : "This is a framework that help us to build application easily",
        "date_posted": "April 20 2025"
    },
 
]

@app.get("/api/posts")
def get_posts():
    return posts