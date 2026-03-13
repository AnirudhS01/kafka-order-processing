from fastapi import FastAPI
from fastapi.responses import JSONResponse
import app.routes as order_routes


app = FastAPI()
app.include_router(order_routes.router)


@app.get("/health")
def health_check():
    return JSONResponse(
        content = {"message":"Backend working"},
         status_code=200)