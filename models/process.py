import pandas as pd
import numpy as np
import re

class main:
    def __init__(self,data) -> None:
        self.data = data.decode('utf-8')
        # f = open("models/WhatsApp Chat with Young Genius 🙉☺️.txt" , 'r' ,encoding='utf-8')
        # self.data =f.read()
        self.pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\S{2}\s-\s'
        self.messages = re.split(self.pattern,self.data)[1:]
        self.dates = re.findall(self.pattern,self. data)
        df = pd.DataFrame({'user_message': self.messages, 'message_date': self.dates})
        for columns in df['message_date']:
            df['message_date'] = df['message_date'].str.upper()
        df['message_date']= df["message_date"].str.replace("-","")
        df['message_date']= df["message_date"].str.replace(","," ")
        # Print the formatted date
        df['message_date'] = pd.to_datetime(df['message_date'])
        df['message_date'] = df['message_date'].dt.strftime('%d/%m/%Y %I:%M %p')
        df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y %I:%M %p')
        df['message_date'].dt.date
        df.rename(columns={'message_date': 'date'}, inplace=True)
        self.df=df

    def func1(self):
        return self.df

    def all_users(self):
        users = []
        for message in self.df['user_message']:
            entry = re.split('([\w\W]+?):\s', message)
            if entry[1:]:  # user name
                users.append(entry[1])
            else:
                users.append('group_notification')
        self.df['user'] = users
        return users

    def all_messages(self):
        messages = []
        for message in self.df['user_message']:
            entry = re.split('([\w\W]+?):\s', message)
            if entry[1:]:  # user name
                messages.append(" ".join(entry[2:]))
            else:
                messages.append(entry[0])
        self.df['message'] = messages
        return messages

    def dates_only(self):
        self.df['only_date'] = self.df['date'].dt.date
        dates = self.df['only_date']
        return dates
    
    def years_only(self):
        self.df['year'] = self.df['date'].dt.year
        years = self.df['year']
        return years
    
    def months_only(self):
        self.df['month_num'] = self.df['date'].dt.month
        self.df['month'] = self.df['date'].dt.month_name()
        months = self.df['month']
        return months
    
    def days_only(self):
        self.df['day'] = self.df['date'].dt.day
        self.df['day_name'] = self.df['date'].dt.day_name()
        days = self.df['day_name']
        return days
    
    def hours_only(self):
        self.df['hour'] = self.df['date'].dt.hour
        hours = self.df['hour']
        return hours
    
    def minutes_only(self):
        self.df['minute'] = self.df['date'].dt.minute
        minutes = self.df['minute']
        return minutes
    
    def period_section(self):
        period = []
        for hour in self.df[[main().days_only(), main().hours_only()]][main().hours_only]:
            if hour == 0:
                period.append('00' + "-" + str(hour + 1))
            elif hour == 23:
                period.append(f"{str(hour)}-00")
            else:
                period.append(f"{str(hour)}-{str(hour + 1)}")
        self.df['period'] = period
        return period



#main_class = main()
# print(main_class.period_section())