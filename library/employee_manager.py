''' Import standard library package. '''
from datetime import datetime as dt

class Employee_Manager():
    '''
        This class is used to manage the employee information about the hours worked and the salary the company
        has to pay them based on the salary table described next:
            Monday - Friday
            00:01 - 09:00 25 USD
            09:01 - 18:00 15 USD
            18:01 - 00:00 20 USD

            Saturday and Sunday
            00:01 - 09:00 30 USD
            09:01 - 18:00 20 USD
            18:01 - 00:00 25 USD
        The salary is calculated based on the minutes worked; because the "timedelta" object, resulting from the
        substract of two datetime.datetime, doesn't have a ".minutes" attribute but ".seconds" one, the wages are
        calculated per secodns (divided by 3600).

        The start and end turn are the middle turn described on the previous table (09:00 - 18:00), the date was set
        to 1900/1/1 because the method ".strptime" of datetime.datetime uses this date when only time information
        is passed to it, so this was set in order to match the dates between the turns and the worked hours by 
        the employees.
    '''
    name = None
    salary = None
    days = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}
    wages = [25 / 3600, 15 / 3600, 20 / 3600, 30 / 3600, 20 / 3600, 25 / 3600]
    start_turn = dt(year = 1900, month = 1, day = 1, hour = 9, minute = 0)
    end_turn = dt(year = 1900, month = 1, day = 1, hour = 18, minute = 0)

    def __init__(cls, name, schedule):
        cls.name = name
        cls.schedule = schedule
        cls.salary = cls.calculate_salary()

    def calculate_salary(cls):
        format_ = "%H:%M"
        aux_salary = 0

        for day in cls.schedule:
            start = dt.strptime(day['Start'], format_)
            end = dt.strptime(day['End'], format_)

            if cls.days[day['Day']] < 5:
                wage_1, wage_2, wage_3 = cls.wages[:3]
            else:
                wage_1, wage_2, wage_3 = cls.wages[3:]

            if start < cls.start_turn:
                if end < cls.start_turn:
                    aux_salary += (end - start).seconds * wage_1
                elif end < cls.end_turn:
                    aux_salary += (cls.start_turn - start).seconds * wage_1
                    aux_salary += (end - cls.start_turn).seconds * wage_2
                else:
                    aux_salary += (cls.start_turn - start).seconds * wage_1
                    aux_salary += (cls.end_turn - cls.start_turn).seconds * wage_2
                    aux_salary += (end - cls.end_turn).seconds * wage_3
            elif start < cls.end_turn:
                if end < cls.end_turn:
                    aux_salary += (end - start).seconds * wage_2
                else:
                    aux_salary += (cls.end_turn - start).seconds * wage_2
                    aux_salary += (end - cls.end_turn).seconds * wage_3
            else:
                aux_salary += (end - start).seconds * wage_3

        return aux_salary
            

            

            


