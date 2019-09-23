import datetime
import re

today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
# не знаю, что имеется в виду под месяцем. Календарный месяц или просто 30 дней.
month_ago = datetime.date.today() - datetime.timedelta(days=30)

print(today)
print(yesterday)
print(month_ago)

date_str = '01/01/17 12:10:03.234567'
# я не знаю, как нормально убрать милисекунды. strptime с ними падает
pattern = '\d{1,2}\/\d{1,2}\/(\d{,4})\s.*?(\..*)'


# и я не уверена, что нормльно использую регулярки
def fix_date(m):
        return m.group(0).replace(m.group(2), '')


date_from_str = re.sub(pattern, fix_date, date_str)
date_from_str = datetime.datetime.strptime(date_from_str, '%d/%m/%y %H:%M:%S')
print(date_from_str)
