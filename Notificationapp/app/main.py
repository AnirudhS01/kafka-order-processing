from confluent_kafka import Consumer
import json
import time

consumer_config = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "Order-Tracker",
    "auto.offset.reset": "earliest"
}

# Wait for Kafka to be ready
print("Waiting for Kafka to be ready...")
time.sleep(15)

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])
print("Consumer is running and subscribed to Topic: orders")

try:
    while True:
        msg = consumer.poll(5.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue
        result = msg.value().decode("utf-8")
        order = json.loads(result)
        print(f"Order Received for {order['user_id']} -- {order['email']} -- {order['total_cost']} -- {order['items']}")
except KeyboardInterrupt:
    print("Consumer stopped")
finally:
    consumer.close()