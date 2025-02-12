from datetime import datetime
def convdate(date_str):
    iformat = "%m/%d/%Y"
    oformat = "%B %d, %Y"
    try:
        date_obj = datetime.strptime(date_str, iformat)
        return date_obj.strftime(oformat)
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

if __name__ == "__main__":
    print("-------------------------------------------------")
    date = input("Enter the date (mm/dd/yyyy): ")
    hdate = convdate(date)
    print("Date Output:", hdate)
    print("-------------------------------------------------")