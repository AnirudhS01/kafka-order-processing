from confluent_kafka import Consumer
import json

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "Order-Tracker",
    "auto.offset.reset": "earliest"
}
consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])
print("Consumer  is running annd subscribed to Topic: orders")

while True:
    msg = consumer.poll(5.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error : {msg.error()}")
        continue

    result = msg.value().decode("utf-8")
    order = json.loads(result)
    print(f"""Order Recieved, Generation of confirmation mail in process for
          {order["user_id"]} -- {order["email"]} -- {order["total_cost"]} -- {order["items"]}""")


