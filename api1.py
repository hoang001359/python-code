import requests
import json
import smtplib
from email.mime.text import MIMEText
 
url = "http://10.200.10.189/api/budgets/1"
 
headers = {
    "accept": "application/json",
    "authorization": "Bearer d473f67e-1b4b-4d25-9d9f-360ffe414336"
}
 
response = requests.get(url, headers=headers, verify=False)
print(response.text)
# Load JSON data from the response content
data = json.loads(response.text)
 
# Extract intervals
intervals = data['budget']['stats']['intervals']
 
# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "hoangk62tlu@gmail.com"
smtp_password = "mthb lccu uhvx bjkw"
sender_email = "hoangk62tlu@gmail.com"
recipient_email = "hoang001359@gmail.com"
 
# Create a text version of the email body
email_body = ""
for interval in intervals:
    budget = interval['budget']
    cost = interval['cost']
    interval_name = interval['month']
    
    if cost > budget:
        alert_message = f"Alert: Cost ({cost}) is greater than Budget ({budget}) for interval {interval_name}\n"
        email_body += alert_message
 
# If there are alerts, send an email
if email_body:
    msg = MIMEText(email_body)
    msg['Subject'] = "Budget Alert"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Establish a secure session with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, [recipient_email], msg.as_string())
 
# Print the JSON response content
print("JSON response:")
print(response.text)
 