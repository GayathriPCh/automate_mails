# Automated Email Sender

This project automates the process of sending personalized emails to a list of recipients. It reads recipient data from an Excel or CSV file and sends emails using Gmail's SMTP server.

## Features

- **Automated Email Sending**: Sends personalized emails to recipients automatically.
- **Customizable Email Content**: Easily customize the email body for different purposes.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `pandas`: For reading data from Excel or CSV files.
  - `smtplib`: For sending emails using SMTP.
  - `email.mime.multipart`, `email.mime.text`, `email.mime.base`: For formatting the email content.

## Setup

### Step 1: Prepare Your Data File

Ensure your Excel or CSV file includes the following columns:
- `Name`: The recipient's name.
- `Email`: The recipient's email address.
- Additional columns can be added as needed for custom email content.

### Step 2: Set Up Your Email and Password

Update the following variables in the script with your email and password:

```python
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'
```

For Gmail users, you may need to enable **less secure apps** or use an **App Password** if two-factor authentication is enabled.

### Step 3: Install Required Libraries

Install the required libraries by running:

```bash
pip install pandas
```

### Step 4: Run the Script

1. Place your data file (`Test.xlsx` or `certificates_data.csv`) in the same directory as the script.
2. Run the script with:

```bash
python send_emails.py
```

The script will read the data from the file and send emails to each recipient.
