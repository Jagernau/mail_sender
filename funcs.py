import csv
import pandas as pd

def clients_to_dict(filename):
    data_dict = {}

    with open(filename, newline='') as csvfile:
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
    df = pd.DataFrame(value, columns=['Клиет','Система мониторинга', 'Имя объекта', 'Количество дней', 'Цена'])
    df.to_excel('detalisacion.xlsx', index=False)
#    workbook = Workbook('output.xlsx')
#    pdf_options = PdfSaveOptions()
#    workbook.save('output.pdf', pdf_options)
    


