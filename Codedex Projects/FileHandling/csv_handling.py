import csv

max_sales = 0
best_selling_book = None

with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    file.readline()
    reader_object = csv.reader(file)

    for row in reader_object:
        sales = float(row[4]) # 5th element of a row

        if sales > max_sales:
            max_sales = sales
            best_selling_book = row

with open('best_seller_info.csv', 'w',newline='', encoding='utf-8') as newfile:
    new_writer = csv.writer(newfile)
    new_writer.writerow(['Book','Author','Original language','First published','sales in millions','Genre'])
    new_writer.writerow(best_selling_book)