import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from string import Template
from email.mime.application import MIMEApplication
import os
import json
with open('env.json') as file:
    env = json.load(file)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = env["email"]
SENDER_PASSWORD = env['pass']

# HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechHunt Certificates</title>
</head>
<body style="font-family: ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'; line-height: 1.5; -webkit-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; background-color: #121212; color: #e0e0e0; margin: 0; padding: 0;">
    <div style="display: flex; justify-content: center; align-items: center; min-height: 100vh; background-color: #121212;">
        <div style="max-width: 28rem; margin: 2rem auto;">
            <div style="background-color: #1e1e1e; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -2px rgba(0, 0, 0, 0.3);">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <img src="https://i.imgur.com/XDemAsx.png" alt="cc" style="height: 30px; margin-right: 10px;">
                    <h1 style="font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0;">Hack The Plot</h1>
                </div>
                <div style="background-color: #2a2a2a; padding: 1rem; border-radius: 0.5rem;">
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">Hola! ${name}👋 TechHunt here... again...</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">We are forever indebted to you for participating in TechHunt and making it so rewarding to host.</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">So, as a token of our appreciation, here’s a shiny e-certificate to flex on LinkedIn—go ahead, let the world know you’re a huuuge geek.</p>
       <p style="color: #e0e0e0; margin-top: 1rem;">And, now that the "Why" in Anaya's story is over, we'll move on to "Where"...</p>
                    <p style="color: #e0e0e0; margin-top: 1rem;">See you next time!</p>                    <p style="color: #e0e0e0; font-size: 0.8rem; margin-top: 0.5rem;">~DDS</p>
                </div>
                <p style="color: #8a8a8a; font-size: 0.875rem; margin-top: 0.8rem;">Made with 
                    <img src="https://iiitvcc.vercel.app/heart.png" alt="love" style="display: inline-block; width: 1rem; height: 1rem;">
                    by <a href="https://hacktheplot.vercel.app" style="color: #bb86fc; text-decoration: none;">Team TechHunt</a>
                </p>
                <p style="color: #8a8a8a; font-size: 0.875rem; margin-top: -0.8rem;">Questions? <a href="tel:9074755597" style="color: #bb86fc; text-decoration: none;">Contact Us</a></p>
            </div>
        </div>
    </div>
</body>
</html>"""

def send_email(recipient_email, team_id, name, is_winner):
    try:
        folder = "losers" if not is_winner else "winners"
        pdf_path = f"./certs/{folder}/pdfs/{team_id}_{name}.pdf"
        
        # Create message
        msg = MIMEMultipart('mixed')
        msg['Subject'] = "Your TechHunt E-Certificate"
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email

        # Replace template variables
        html_content = Template(HTML_TEMPLATE).safe_substitute(
            name=name,
        )

        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))
        
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
                pdf_attachment.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=os.path.basename(pdf_path)  # File name for the recipient
                )
                msg.attach(pdf_attachment)

        # Send email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"✅ Email sent successfully to {recipient_email}")
            
    except Exception as e:
        print(f"❌ Failed to send email to {recipient_email}: {str(e)}")

def process_json(filename):
    print("Starting email dispatch process...")
    sent_count = 0
    failed_count = 0
    
    try:
        with open(filename, 'r') as file:
            users = json.load(file)
            for user in users:
                email = user["email"]
                team_id = user['team_id']
                name = user['name']
                standing = user['standing']
                try:
                    time.sleep(60)
                    send_email(email, team_id, name, True if standing <= 10 else False)
                    sent_count += 1
                    # Add a small delay between emails to avoid rate limiting
                except Exception as e:
                    failed_count += 1
                    print(f"Failed to process row for team {name}: {str(e)}")
                    
    except Exception as e:
        print(f"Error reading JSON file: {str(e)}")
        return
    
    print("\nEmail dispatch summary:")
    print(f"✅ Successfully sent: {sent_count}")
    print(f"❌ Failed: {failed_count}")
    print("Process completed!")

if __name__ == "__main__":
    json_filename = "./standings.json"  # Make sure this matches your JSON file name
    process_json(json_filename)