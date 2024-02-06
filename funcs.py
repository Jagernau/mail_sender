import csv
import pandas as pd
from styleframe import StyleFrame
import datetime
import locale
import logging

def clients_to_list(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def create_pdf_from_list(value):
    df = pd.DataFrame(value, columns=['Клиет', 'Система мониторинга', 'Имя объекта', 'Количество дней', 'Цена'])
    df['Цена'] = df['Цена'].astype(float)
    excel_writer = StyleFrame.ExcelWriter('detalisation.xlsx')
    sf = StyleFrame(df)
    sf.set_column_width(columns=['Имя объекта', ],
                        width=36)
    sf.set_column_width(columns=['Клиет'], width=15)
    sf.set_column_width(columns=['Количество дней'], width=15)

    sf.to_excel(excel_writer=excel_writer)
    excel_writer.save()

def get_date_last_month():
    months = {
    '1': 'январь',
    '2': 'февраль',
    '3': 'март',
    '4': 'апрель',
    '5': 'май',
    '6': 'июнь',
    '7': 'июль',
    '8': 'август',
    '9': 'сентябрь',
    '10': 'октябрь',
    '11': 'ноябрь',
    '12': 'декабрь'
}
    return months[str(int(datetime.date.today().month)-1)]
    
def get_current_year():
    return datetime.date.today().year

def my_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


    # Создание обработчика для записи в файл
    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.INFO)


    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(file_handler)
    return logger
