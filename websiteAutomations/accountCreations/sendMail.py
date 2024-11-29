import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from string import Template
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
    <title>IIITV Coding Club - Email Verification</title>
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
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">Hola! Team ${teamName}👋 TechHunt here...</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">The first step towards uncovering the mystery of Anaya is actually being able to login!</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">So here are your login credentials fellow hunter...</p>
                    <div style="display: inline-flex; align-items: center; justify-content: center; white-space: nowrap; font-size: 0.875rem; font-weight: 500; height: 4rem; padding-left: 1rem; padding-right: 1rem; border: 0.5px solid #bb86fc; color: #ffffff; width: fit-content; border-radius: 0.5rem; text-decoration: none;">
                        <span style="display: inline-flex; color: #ffffff; text-decoration: none; margin: auto; padding: 8px;">Email:  ${email}<br>Pass:  ${password}</span>
                    </div>
                    <p style="color: #e0e0e0; margin-top: 1rem;">For all announcements, join our <a href="https://chat.whatsapp.com/ElqeDEwzTPv6syRVmqv6B5" style="text-decoration:none;">WhatsApp Group</a></p>
                    <p style="color: #e0e0e0; margin-top: 1rem;">Happy Hacking!</p>
                    <p style="color: #e0e0e0; margin-top: 1rem;">PS: Don't forget to bring your laptops, headphones and ego.</p>
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

def send_email(recipient_email, team_name, password):
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Welcome to Hack The Plot - Your Login Credentials"
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email

        # Replace template variables
        html_content = Template(HTML_TEMPLATE).safe_substitute(
            teamName=team_name,
            email=recipient_email.replace("@", "&#8203;@").replace(".", "&#8203;."),
            password=password
        )

        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # Send email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"✅ Email sent successfully to {recipient_email} (Team {team_name})")
            
    except Exception as e:
        print(f"❌ Failed to send email to {recipient_email}: {str(e)}")

def process_csv(filename):
    print("Starting email dispatch process...")
    sent_count = 0
    failed_count = 0
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                team_name = row['Team Name']
                email = row["Candidate's Email"]
                password = row['Team ID']
                
                try:
                    send_email(email, team_name, password)
                    sent_count += 1
                    # Add a small delay between emails to avoid rate limiting
                    time.sleep(1)
                except Exception as e:
                    failed_count += 1
                    print(f"Failed to process row for team {team_name}: {str(e)}")
                    
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return
    
    print("\nEmail dispatch summary:")
    print(f"✅ Successfully sent: {sent_count}")
    print(f"❌ Failed: {failed_count}")
    print("Process completed!")

if __name__ == "__main__":
    csv_filename = "output.csv"  # Make sure this matches your CSV file name
    process_csv(csv_filename)