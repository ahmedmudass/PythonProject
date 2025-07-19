import pandas as pd
data = {
    'Food Name': ['Biryani', 'Pizza', 'Burger', 'Pasta', 'Kebab', 'Chowmein'],
    'Price': [1200, 800, 450, 700, 500, 1800],
    'Category': ['Main Course', 'Fast Food', 'Fast Food', 'Fast Food', 'Main Course', 'Fast Food'],
    'Main Ingredient': ['Rice', 'Cheese', 'Beef', 'Pasta', 'Meat', 'Noodles'],
    'Quantity': [1, 1, 1, 1, 2, 1],
    'Status': ['Available', 'Available', 'Unavailable', 'Available', 'Available', 'Unavailable']
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df['Country'] = 'Pakistan'

df['Sale Price'] = df['Price'] * 0.9

print("\nFood items with price > 500:")
print(df[df['Price'] > 500])

print("\nAvailable food items:")
print(df[df['Status'] == 'Available'])

print("\nAvailable fast food items:")
print(df[(df['Status'] == 'Available') & (df['Category'] == 'Fast Food')])

print("\nBiryani item:")
print(df[df['Food Name'] == 'Biryani'])

print("\nFood items with price > 1500:")
print(df[df['Price'] > 1500])

conversion = input("\nIn which format you want to convert data? (csv/json/excel): ").lower()

if conversion == 'csv':
    df.to_csv('food_item.csv', index=False)
    print("Data saved as food_item.csv")
elif conversion == 'json':
    df.to_json('food_item.json', orient='records', indent=2)
    print("Data saved as food_item.json")
elif conversion == 'excel':
    df.to_excel('food_item.xlsx', index=False)
    print("Data saved as food_item.xlsx")
else:
    print("Invalid format selected.")