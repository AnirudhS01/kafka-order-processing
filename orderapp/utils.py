

def delivery_report(err , msg):
    if err:
        print(f"Delivery failed due to \n {err}")
    else:
        print(f"Delivery successful \n {msg.value().decode("utf-8")}")