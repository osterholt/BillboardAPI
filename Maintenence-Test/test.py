import datetime

date_string = '1963-08-02'

start_date = datetime.date(int(date_string[:4]), int(date_string[5:7]), int(date_string[9:]))

print(start_date)