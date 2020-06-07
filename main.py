import pymongo
import os

# Retrieve MongoDB Connection string from .env file
mongo_connection = os.getenv("MONGO_CONNECTION")

# Connect to MongoDB Atlas
client = pymongo.MongoClient(mongo_connection)

# Set Variables for Database and Collection
db = client['Portfolio']
stocks_collection = db['Stocks']

def main():

    while(1):
    # CRUD Option Selections
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print ('\n INVALID SELECTION \n')

# Function to insert data into MongoDB
def insert():
    try:
        Ticker = raw_input('Enter Ticker Code :')
        Profit_Margin = raw_input('Enter Profit Margin :')
        Institutional_Ownership = raw_input('Enter Institutional Ownership :')
        EPS_growth = raw_input('Enter EPS growth past 5 yearsCountry :')
        Total_Debt_Equity = raw_input('Enter Total Debt/Equity :')
        Current_Ratio = raw_input('Enter Current Ratio :')

        db.Employees.insert_one(
            {
                "Ticker":Ticker,
                "Profit Margin":Profit_Margin,
                "Institutional Ownership":Institutional_Ownership,
                "EPS growth past 5 years":EPS_growth,
                "Total Debt/Equity":Total_Debt_Equity,
                "Current Ratio":Current_Ratio
        })
        print ('\nInserted data successfully\n')
    
    except Exception as e:
        print (e)