import pymongo
import os
import sys

# Retrieve MongoDB Connection string from .env file
mongo_connection = os.getenv("MONGO_CONNECTION")

# Connect to MongoDB Atlas
client = pymongo.MongoClient(mongo_connection)

# Set Variables for Database and Collection
db = client['Portfolio']

def main():

    while(1):
    # CRUD Option Selections
        selection = input('\nPlease make a selection from the following choices: \n 1: Create a new document\n 2: Select a document to view \n 3: Update a document\n 4: Delete a document \n 5: Quit \n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            read()
        elif selection == '3':
            update()
        elif selection == '4':
            delete()
        elif selection == '5':
            quit()
        else:
            print ('INVALID SELECTION \n')

# Function to insert data into MongoDB
def insert():
    try:
        Ticker = input('Enter Ticker Code :')
        Profit_Margin = input('Enter Profit Margin :')
        Institutional_Ownership = input('Enter Institutional Ownership :')
        EPS_growth = input('Enter EPS growth past 5 yearsCountry :')
        Total_Debt_Equity = input('Enter Total Debt/Equity :')
        Current_Ratio = input('Enter Current Ratio :')

        db.Stocks.insert_one(
            {
                "Ticker":Ticker,
                "Profit Margin":Profit_Margin,
                "Institutional Ownership":Institutional_Ownership,
                "EPS growth past 5 years":EPS_growth,
                "Total Debt/Equity":Total_Debt_Equity,
                "Current Ratio":Current_Ratio
        })
        print ('Inserted data successfully\n')
    
    except Exception as e:
        print (e)

#Function to read data from MongoDB
def read():
  ticker_selection = input('Enter the Ticker of the stock you would like to view: \n')
  ticker_find = ({"Ticker": ticker_selection})
  try:
    stockColl = db.Stocks.find(ticker_find)
    print ('Stocks')
    for stock in stockColl:
      print (stock)

  except Exception as e:
    print (e)

#Function to update data in MongoDB
def update():
  try:
    update_criteria = input('Enter Ticker of the Record you would like to update:\n')
    update_profit = input('Enter New Profit Margin\n')

    db.Stocks.update_one(
      {"ticker": update_criteria},
      {"$set": {
        "Profit_Margin": update_profit
       }
      }
    )

    print ('Record updated successfully\n')

  except Exception as e:
    print (e)

#Function to delete a record from MongoDB
def delete():
  try:
    delete_criteria = input('Enter Ticker Name to delete: \n')
    db.Stocks.delete_one({"Ticker":delete_criteria})
    print ('Document Deleted')
  except Exception as e:
    print (e)

#Function to quit program
def quit():
  try:
    endProgram = input('Are you sure you want to quit? (Yes/No) ')
    if endProgram == "Yes" or "yes":
      sys.exit()
    else: 
      main()
  except Exception as e:
    print(e)
 
main()