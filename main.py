import config
from jinja2 import Environment, FileSystemLoader
import classes
import funcs
import time
import random
import sys
from tqdm import tqdm


last_month = funcs.get_date_last_month()
current_year = funcs.get_current_year()

smtp_server = config.SMTP_SERVER
email_sender = config.EMAIL_SENDER
email_password = config.EMAIL_PASSWORD

list_clients = [["st"], ["st"]]
list_clients.extend(funcs.clients_to_list(filename="./clients.csv"))
logger = funcs.my_logger()

def job():
    for i in tqdm(list_clients, desc="Отправка писем..."):
        if i == []:
            continue
        try:
            time.sleep(random.randint(15, 30))
            i = str(i[0]).replace(" ", "")
            if i == "NULL" or i == " " or i == "":
                continue
            if "@" not in i:
                continue
            try:
                logger.info(f'Начало формирования письма для {i}')
                email_receiver = str(i)
                email_subject = f'Тест'
                environment = Environment(loader=FileSystemLoader("templates/"))
                template = environment.get_template("file_sender.html")
                content = template.render()
                email_body = content
                email = classes.EmailSender(email_sender, email_password, smtp_server)
                email.create_message(email_receiver, email_subject, email_body)
                email.attach_file("file.txt")
                email.send_email()
                logger.info(f'Письмо для {i} отправлено')
                with open("sends.txt", "a") as f:
                    f.write(f"{i}\n")
                time.sleep(random.randint(20, 47))
            except Exception as e:
                logger.error(f'Письмо для {i} не отправлено. Ошибка: {e}')
                with open("fails.txt", "a") as f:
                    f.write(f"{i}\n")
                continue
            

        except Exception as e:
            logger.error(f'Письмо для {i} не отправлено. Ошибка: {e}')
            with open("fails.txt", "a") as f:
                f.write(f"{i}\n")
            continue


if __name__ == "__main__":
    job()
    sys.exit()
