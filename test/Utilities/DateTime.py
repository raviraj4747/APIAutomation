import datetime


class DateTime:

    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        current_time = now.strftime("%H-%M-%S")
        return current_time

    @staticmethod
    def get_todays_date():
        now = datetime.datetime.now()
        todays_date = now.strftime("%m/%d/%Y")
        return todays_date

    @staticmethod
    def get_date_with_difference_of_x_from_today_date(number):

        if number > 0:
            date = datetime.datetime.today() + datetime.timedelta(days=number)
            formatted_date = date.strftime("%m/%d/%Y")
            return formatted_date

        else:
            date = datetime.datetime.today() - datetime.timedelta(days=abs(number))
            formatted_date = date.strftime("%m/%d/%Y")
            return formatted_date

    @staticmethod
    def get_current_date_time_stamp_in_format_MMddYYYY_hhmmss():
        curr_date = datetime.datetime.now()
        date = str(curr_date.day) + str(curr_date.month) + str(curr_date.year) + str(curr_date.hour) + str(
            curr_date.minute) + str(curr_date.second)
        return date

    @staticmethod
    def get_date_without_preceding_zero(date):
        day = date[3:5]
        month = date[0:2]
        year = date[-4:]

        if day[0] == '0':
            day = day.replace("0", "")

        if month[0] == '0':
            month = month.replace("0", "")

        new_date = month + '/' + day + '/' + year

        return new_date
