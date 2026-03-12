from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from orderapp.models import Order
import json
from confluent_kafka import Producer
from orderapp.utils import delivery_report

router = APIRouter()

@router.post("/postorder")
def post_order(order: Order):
    try:
        #configuration for producer to listen to kafka broker at 9092 as mentioned in the docker compose env
        producer_config = {"bootstrap.servers":"localhost:9092"}
        producer = Producer(producer_config)

        #convert the request to json and encode into bytes as required by kafka
        encoded_order = json.dumps(order.model_dump()).encode("utf-8")

        producer.produce(topic="orders",
                         value=encoded_order,
                         callback=delivery_report)
        
        producer.flush()
        
        return JSONResponse(
            status_code=200,
            content={
                "message":"Order Placed and waiting to be processed",
                "detials": order.model_dump()
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )