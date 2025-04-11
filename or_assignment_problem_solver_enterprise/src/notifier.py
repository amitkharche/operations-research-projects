import requests
import os

def send_slack_notification(assignments, total_cost, webhook_url=None):
    if not webhook_url:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        return "Slack webhook not configured."

    blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": "*🚨 Assignment Completed*"}}]
    for a in assignments:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"{a['worker']} → {a['task']} (${a['cost']})"}})
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"*Total Cost:* ${total_cost}"}})
    
    response = requests.post(webhook_url, json={"blocks": blocks})
    return response.status_code
