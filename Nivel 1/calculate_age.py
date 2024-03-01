from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(present_date, birth_date):
    present = datetime.strptime(present_date, '%d/%m/%Y')
    birth = datetime.strptime(birth_date, '%d/%m/%Y')
    delta = relativedelta(present, birth)
    print(f'Present Age = Years: {delta.years}  Months: {delta.months}  Days: {delta.days}')

present_date = '07/12/2017'
birth_date = '07/09/1996'
calculate_age(present_date, birth_date)
