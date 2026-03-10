from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from orderapp.models import Order
import json

router = APIRouter()

@router.post("/postorder")
def post_order(order: Order):
    try:
        result = order.model_dump()
        return JSONResponse(
            status_code=201,
            content={
                "message":"Order placed successfully",
                "details":result
            }
            
        ) # here we add the order to kafka queue
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )