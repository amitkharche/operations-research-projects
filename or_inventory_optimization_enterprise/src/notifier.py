import requests
import os

def send_slack_notification(product_id, eoq, webhook_url=None):
    webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return "Slack webhook not configured."

    message = f"*📦 Reorder Alert:* Product `{product_id}` should be reordered. EOQ: `{eoq:.2f}` units."
    payload = {"text": message}
    return requests.post(webhook_url, json=payload).status_code
