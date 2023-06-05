import csv
import pandas as pd
from styleframe import StyleFrame
import datetime
import locale


def clients_to_dict(filename):
    data_dict = {}

    with open(filename, newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок файла
        for row in reader:
            email = row[1]
            values = [row[0], row[5], row[6], row[7], row[8]]
            if email in data_dict:
                data_dict[email].append(values)
            else:
                data_dict[email] = [values]

    return data_dict

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
