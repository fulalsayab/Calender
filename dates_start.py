#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("today date is ", today)

  # print out the date's individual components
  print("Date comonents: ",today.day, today.month,today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Todys wake day # is ",today.weekday())
  days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  print("Which is a: ", days[today.weekday()])


  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print(today)


  # Get the current time
  today = datetime.time(datetime.now())
  print(today)


  
if __name__ == "__main__":
  main();
  