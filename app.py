import csv
import datetime 


csv_date = datetime.datetime.today().strftime("%Y%m%d")

csv_file_name = 'bloomberg_' + csv_date + '.csv'
f = open(csv_file_name, 'w', encoding='cp932')

writer = csv.writer(f, lineterminator='\n') 
csv_header = ["記事番号","URL","サマリー"]
writer.writerow(csv_header)