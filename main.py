from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Bitelemetric</title>
        </head>
        <body>
            <h1>Bitelemetric rebranding in progress!</h1>
            <p>Check back soon!</p>
        </body>
    </html>
    """

@app.get("/api/hello")
def hello():
    return {"message": "Flow ready to go!"}
