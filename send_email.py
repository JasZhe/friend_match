import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    email,
    student
):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "MSCFriendMatch@gmail.com"  # Enter your address
    receiver_email = "kcforever101@hotmail.com"  # Enter receiver address
    password = "JasonCodedThis"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Friend Match"
    message["From"] = sender_email
    message["To"] = receiver_email

    plainText = """
    Hi {student},

    Thank you for participating in our FriendMatch Event! The data has been analyzed and your top 5 matches are: 

    1. {first_match} Ice breaker: {first_match_ice_breaker} Contact information: {first_match_contact}
    2. {second_match} Ice breaker: {second_match_ice_breaker} Contact information: {second_match_contact}
    3. {third_match} Ice breaker: {third_match_ice_breaker} Contact information: {third_match_contact}
    4. {fourth_match} Ice breaker: {fourth_match_ice_breaker} Contact information:{fourth_match_contact}
    5. {fifth_match} Ice breaker: {fifth_match_ice_breaker} Contact information: {fifth_match_contact}

    Feel free to contact your matches and to join us for our first Games Night of the year, which takes place on Oct 1st at 7 PM on our Discord server! 

    If you have any feedback for us, feel free to drop a comment here: https://forms.gle/MFmcVCsuJbasjVvo9 or send us an email at studentcouncil@michener.ca

    Sincerely, 
    Your Student Council Team
    """

    htmlText = """
    <html>
        <head></head>
        <body>
            <p>
            Hi {student}, <br>
            <br>
            Thank you for participating in our FriendMatch Event! The data has been analyzed and your top 5 matches are: <br>
            <br>
            1. {first_match} <b>Ice breaker:</b> {first_match_ice_breaker} <b>Contact information:</b> {first_match_contact} <br>
            2. {second_match} <b>Ice breaker:</b> {second_match_ice_breaker} <b>Contact information:</b> {second_match_contact} <br>
            3. {third_match} <b>Ice breaker:</b> {third_match_ice_breaker} <b>Contact information:</b> {third_match_contact} <br>
            4. {fourth_match} <b>Ice breaker:</b> {fourth_match_ice_breaker} <b>Contact information:</b>{fourth_match_contact} <br>
            5. {fifth_match} <b>Ice breaker:</b> {fifth_match_ice_breaker} <b>Contact information:</b> {fifth_match_contact} <br>
            <br>
            Feel free to contact your matches and to join us for our first Games Night of the year, which takes place on Oct 1st at 7 PM on our Discord server! <br>
            </br>
            If you have any feedback for us, feel free to drop a comment here: https://forms.gle/MFmcVCsuJbasjVvo9 or send us an email at studentcouncil@michener.ca <br>
            <br>
            Sincerely,<br> 
            Your Student Council Team<br>
            </p>
        </body>
    </html>
    """

    textPart = \
        MIMEText(plainText.format(student="kayli",
                                  first_match="johnson", first_match_ice_breaker="asdaf", first_match_contact="asd",
                                  second_match="jacky", second_match_ice_breaker="asdsdsd",
                                  second_match_contact="asdjhkalfj",
                                  third_match="tommy", third_match_ice_breaker="askdjald",
                                  third_match_contact="asda",
                                  fourth_match="kyle", fourth_match_ice_breaker="adshjalds",
                                  fourth_match_contact="adhal",
                                  fifth_match="some other dude i dunno colin or some shit",
                                  fifth_match_ice_breaker="dajs", fifth_match_contact="aisdja"
                                  ), "plain"
                 )
    htmlPart = \
        MIMEText(htmlText.format(student="kayli",
                                 first_match="johnson", first_match_ice_breaker="asdaf", first_match_contact="asd",
                                 second_match="jacky", second_match_ice_breaker="asdsdsd",
                                 second_match_contact="asdjhkalfj",
                                 third_match="tommy", third_match_ice_breaker="askdjald", third_match_contact="asda",
                                 fourth_match="kyle", fourth_match_ice_breaker="adshjalds",
                                 fourth_match_contact="adhal",
                                 fifth_match="some other dude i dunno colin or some shit",
                                 fifth_match_ice_breaker="dajs", fifth_match_contact="aisdja"
                                 ), "html"
                 )

    message.attach(textPart)
    message.attach(htmlPart)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )
