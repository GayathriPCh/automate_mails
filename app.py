import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Set up your email and password for the SMTP server
EMAIL_ADDRESS = 'EMAIL'
EMAIL_PASSWORD = 'PASSWORD'

# Set up the SMTP server (e.g., for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Read the data from your Excel or CSV file
file_path = 'Test.xlsx'  # or 'certificates_data.csv'
df = pd.read_excel(file_path)  # or pd.read_csv(file_path)

# Customize the email content
def create_email_body(name, nft_code, certificate_link):
    return f"""
    Dear {name},

    Congratulations on earning your certificate! You can download your certificate from the following link:
    {certificate_link}

    As an extra reward, here is your unique code to claim an NFT: {nft_code}

    Please visit our website and redeem this code to mint your NFT.

    Best regards,
    Your Team
    """

# Function to send emails
def send_certificate_email(recipient_email, recipient_name, certificate_link, nft_code):
    try:
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = 'Your Certificate of Completion & NFT Code'

        # Add the email body with the Google Drive link
        body = create_email_body(recipient_name, nft_code, certificate_link)
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient_email, text)

        # Close the server
        server.quit()

        print(f'Email successfully sent to {recipient_name} ({recipient_email})')

    except Exception as e:
        print(f'Failed to send email to {recipient_name} ({recipient_email}): {str(e)}')

# Iterate through the list and send emails
for index, row in df.iterrows():
    name = row['Name']
    email = row['Email']
    certificate_link = row['Certificate_File']  # Use the Google Drive link
    nft_code = row['NFT_Code']
    send_certificate_email(email, name, certificate_link, nft_code)
