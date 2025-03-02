import csv

def exchangerates(filename):
    rates = {}
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            rates[row['code'].strip()] = float(row['rate'].strip())
    return rates

def convert_currency(usd, target_currency, rates):
    return usd * rates[target_currency] if target_currency in rates else None

def main():
    file_path = 'C:/Users/andra_vl3zf4i/andrade_IT0011/LAB-4B/currency.csv'
    rates = exchangerates(file_path)
    usd = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").upper()
    converted_amount = convert_currency(usd, target_currency, rates)

    print("-------------------------------")
    print(f"Dollar: {usd} USD")
    print(f"{target_currency}: {converted_amount}" if converted_amount else "Invalid currency.")

if __name__ == "__main__":
    main()
