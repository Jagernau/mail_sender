import config
from jinja2 import Environment, FileSystemLoader
import classes
import funcs

smtp_server = config.SMTP_SERVER
email_sender = config.EMAIL_SENDER
email_password = config.EMAIL_PASSWORD

dict_clients = funcs.clients_to_dict(filename="./Детализация_для_рассылки.csv")

#print(dict_clients)

for key, value in dict_clients.items():
    email_receiver = str(key)
    email_subject = 'Детализация'
    filename = 'detalisation.xlsx'

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("test.html")
    content = template.render(key=key, value=value)
    funcs.create_excel_from_list(value)
    email_body = content
    email = classes.EmailSender(email_sender, email_password, smtp_server)
    email.create_message(email_receiver, email_subject, email_body)
    email.attach_file(filename)
    email.send_email()

