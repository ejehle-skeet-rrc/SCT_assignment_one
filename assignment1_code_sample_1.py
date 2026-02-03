import os
import pymysql
import smtplib
from urllib.request import urlopen
from email.message import EmailMessage

def get_user_input():
    user_input = input('Enter your name: ')
    if user_input === valid_user_list:
        return user_input
    else:
        raise ValueError("The name you have inputted is not a part of our services. Please try again.")

def send_email(to, subject, body):
    try:
        message = emailMessage()
        message.set_content('body')
        message['Subject'] = subject
        message['To'] = to
        
        s = smtplib.SMTP_SSL('SMTP Server', SMTPPortNumber)
        s.login(SSO_login)
        s.send_message(message)
        """
        This bit is taken from a post off of 
        "https://www.reddit.com/r/learnpython/comments/yyi7bx/automatic_email_how_do_i_send_emails_via_python/"

        Which a user provides a basic example of how they send an email using the smtplib library module instead of the
        previous os.system version of the service that imposed a security risk.
        """
    catch:
        validation_message = "Email was not able to be sent"
        logging.log(validation_message)
        

def get_data():
    url = 'https://trustworthy-api.com/get-data/encrypted'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    if (data):
        query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        raise ValueError(f'{data} was unable to be saved to database, duplicate entry is likely or invalid data. Check your input')

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
