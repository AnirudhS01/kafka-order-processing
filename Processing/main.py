from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from confluent_kafka import Consumer



app = FastAPI()

