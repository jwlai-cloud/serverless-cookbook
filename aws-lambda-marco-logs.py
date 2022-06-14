def lambda_handler(event, context):
    print(f"This was the raw event: {event}")
    if event["name"] == "Marco":
        print("This event was 'Marco'")
        return "Polo"
    print("This event was not 'Marco'")
    return "No!"
