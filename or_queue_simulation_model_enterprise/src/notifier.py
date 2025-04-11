import os
import requests

def alert_high_wait(customers, threshold=10, webhook_url=None):
    webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return "Missing webhook"

    high_waits = customers[customers["WaitTime"] > threshold]
    if high_waits.empty:
        return "No alerts needed"

    msg = f"🚨 {len(high_waits)} customers waited over {threshold} units.
"
    for _, row in high_waits.iterrows():
        msg += f"{row['CustomerID']}: Wait {row['WaitTime']:.2f}
"

    return requests.post(webhook_url, json={"text": msg}).status_code
