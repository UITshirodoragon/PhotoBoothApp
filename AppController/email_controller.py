from email.message import EmailMessage
from email.utils import formataddr
import ssl
import imghdr
import smtplib
import sys
sys.path.insert(0, 'AppController')

def set_email_body (UserName = "bạn"):
    body = f"""\
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .email-container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #444444;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            padding: 20px 0;
        }}
        .header h1 {{
            margin: 0;
            color: #333333;
        }}
        .content {{
            padding: 20px;
            text-align: center;
        }}
        .content p {{
            margin: 0 0 20px;
            line-height: 1.6;
            color: #666666;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007BFF;
            text-decoration: none;
            border-radius: 5px;
        }}
        .footer {{
            text-align: center;
            padding: 20px 0;
            font-size: 12px;
            color: #aaaaaa;
        }}
        .footer .social-icons {{
            margin: 10px 0;
        }}
        .footer .social-icons a {{
            text-decoration: none;
            color: #333333;
            margin: 0 5px;
        }}
        .footer .social-icons a:hover {{
            color: #007BFF;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Photo Booth</h1>
        </div>
        <div class="content">
            <p>Cảm ơn {UserName} đã sử dụng Photo Booth! Chúng tôi hy vọng bạn đã có những bức ảnh tuyệt vời.</p>
            <p>Bạn có thể tải ảnh xuống bằng cách nhấn vào nút bên dưới.</p>
        </div>
        <div class="footer">
            <div class="social-icons">
                <a href="https://www.facebook.com/thinh.tranlequoc" target="_blank">
                    <i class="fab fa-facebook-f"></i>
                </a>
            </div>
            <p>&copy; 2024 Photo Booth. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""
    return body

def send_email(user_email, user_name):
    # with open("DataStorage/ImageGallery" + ".png", "rb") as f:
    #     file_data = f.read()
    #     file_type = imghdr.what(f.name)
    #     file_name = f.name

    # email_sender = 'thinhtranlequoc@gmail.com'
    # email_password = 'heyd nhhz wjvu slqr'
    # email_receiver = user_email

    # name = user_name

    # subject = 'TEST PHOTOBOOTH'

    # email = EmailMessage()
    # email['From'] = formataddr(("PHOTO BOOTH" , f"{email_sender}"))
    # email['To'] = email_receiver
    # email['subject'] = subject
    # email.add_alternative(set_email_body(name), subtype = "html")
    # email.add_attachment(file_data, maintype= "image", subtype= file_type, filename = file_name)

    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(email_sender, email_password)
    #     smtp.sendmail(email_sender, email_receiver, email.as_string())

    print(user_email,' ',user_name)