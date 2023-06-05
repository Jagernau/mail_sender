import config
from jinja2 import Environment, FileSystemLoader
import classes
import funcs
import time


last_month = funcs.get_date_last_month()
current_year = funcs.get_current_year()

smtp_server = config.SMTP_SERVER
email_sender = config.EMAIL_SENDER
email_password = config.EMAIL_PASSWORD
sender_name = config.SENDER_NAME
sender_phone = config.SENDER_PHONE


time.sleep(60)
dict_clients = funcs.clients_to_dict(filename="./detalisation.csv")

#print(dict_clients)

for key, value in dict_clients.items():
    email_receiver = str(key)
    email_subject = f'Детализация за {last_month} {current_year} от Сантел Сервис'
    filename = 'detalisation.xlsx'

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("file_sender.html")

    content = template.render(
            key=key, value=value, last_month=last_month, 
            sender_name=sender_name, sender_phone=sender_phone, 
            current_year=current_year)

    funcs.create_pdf_from_list(value)
    email_body = content
    email = classes.EmailSender(email_sender, email_password, smtp_server)
    email.create_message(email_receiver, email_subject, email_body)
    email.attach_file(filename)
    email.send_email()
    time.sleep(35)
