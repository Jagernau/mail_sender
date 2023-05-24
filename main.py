import config
from jinja2 import Environment, FileSystemLoader
import classes
import funcs

smtp_server = config.SMTP_SERVER
email_sender = config.EMAIL_SENDER
email_password = config.EMAIL_PASSWORD

dict_clients = funcs.clients_to_dict(filename="/storage/emulated/0/Download/Детализация_для_рассылки.csv")

print(dict_clients)

for i in dict_clients:
    email_receiver = str(i)
    email_subject = 'Детализация'
    filename = '/storage/emulated/0/Download/mydata.csv'

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("sample.html")
    content = template.render(name = i, count = len(dict_clients[i]))

    email_body = content
    email = classes.EmailSender(email_sender, email_password, smtp_server)
    email.create_message(email_receiver, email_subject, email_body)
    email.attach_file(filename)
    email.send_email()

