import pandas as pd


class JSONAnalyzer:

    
    def __init__(self, data):
        self.df = pd.DataFrame(data)


    # Check to see if the amount field is a float
    def check_amount_fields_valid(self):
        self.df['is_float_amount'] = pd.to_numeric(self.df['Amount'], errors='coerce').notnull()
        invalid_amount_rows = self.df[~self.df['is_float_amount']]

        if len(invalid_amount_rows) == 0:
            return True
        else:
            print(invalid_amount_rows.drop(columns=['is_float_amount']))
            return False
    

    # Check if the date field has valid data in the right format
    def check_date_fields_valid(self):
        self.df['is_valid_date'] = pd.to_datetime(self.df['Date'], errors='coerce', format="%Y-%m-%dT%H:%M:%S").notnull()
        invalid_date = self.df[~self.df['is_valid_date']]

        if len(invalid_date) == 0:
            return True
        else:
            print(invalid_date.drop(columns=['is_valid_date']))
            return False


    # Works out the total that an employee still owes
    def total_amount_to_pay(self, user):
        total_amount = self.df[self.df['FromAccount'] == user]['Amount'].sum()
        return round(total_amount,2)


    # Works out the total amount owed to an employee
    def total_amount_to_recv(self, user):
        total_amount = self.df[self.df['ToAccount'] == user]['Amount'].sum()
        return round(total_amount,2)


    # Find all the names in the database
    def unique_names(self):
        unique_from_names = self.df['FromAccount'].unique()
        unique_to_names = self.df['ToAccount'].unique()
        all_unique_names = set(unique_from_names) | set(unique_to_names)

        return all_unique_names


    # List all employees and what they owe / are owed
    def list_all(self):
        users = self.unique_names()

        for user in users:
            print(f"Total amount for {user} to pay: £{self.total_amount_to_pay(user)}")
            print(f"Total amount for {user} to receive: £{self.total_amount_to_recv(user)}")
        
    def list_user_details(self, user):
        return self.df[self.df['FromAccount'].str.lower() == user.lower()]

