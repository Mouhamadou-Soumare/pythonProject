from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(name: str = "World"):
    """
    Root endpoint that returns an HTML document with a greeting message.
    
    Args:
        name (str): The name to include in the greeting. Defaults to "World".
        
    Returns:
        HTMLResponse: An HTML document with the greeting message.
    """
    html_content = f"""
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <h1>Hello <span>{name}</span></h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
