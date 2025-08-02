from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging
from src.endpoint1FileName import endpoint1FunctionName

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Check if the logger already has handlers to avoid duplicate logs
if not logger.handlers:
    # Create a console handler
    console_handler = logging.StreamHandler()
    # Set the logging level for the handler
    console_handler.setLevel(logging.INFO)


class LogEndpointMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        logger.info(f"Endpoint called: {path}")
        response = await call_next(request)
        return response


app = FastAPI(
    title="uvFastAPITemplate",
    description="fast API Template Endpoints",
    version="1.0.0",
)

app.add_middleware(LogEndpointMiddleware)


@app.post("/endpoint1")
def endpoint1():
    try:
        endpoint1FunctionName()

        return {"message": "Success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
