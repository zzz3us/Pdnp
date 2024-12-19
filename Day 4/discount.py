from datetime import datetime, date, timedelta

today = date.today()
# print(type(today))
#
# time = datetime.now()
# print(time)
# print(type(time))
#
tomorrow = today + timedelta(days=1)
# print(tommorow)
#
# formatted_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_data)
# print(type(formatted_data))

# formatted_hour = datetime.now().strftime("%H:%M")
# print(formatted_hour)
# print(type(formatted_hour))
#
# formatted_day = datetime.now().strftime("%A")
# print(formatted_day)
# print(type(formatted_day))
#
# fortmatted_time = datetime.now().strftime("%I:%M %p")
# print(fortmatted_time)
# print(type(fortmatted_time))

products = [
    {"sku": 1, "exp_date": today, "price": 100},
    {"sku": 2, "exp_date": today, "price": 200},
    {"sku": 3, "exp_date": tomorrow, "price": 500},
    {"sku": 4, "exp_date": today, "price": 200.00},
    {"sku": 5, "exp_date": tomorrow, "price": 99.99},
]

for p in products:
    # print(f"Product SKU: {p['sku']}, Expiration date: {p['exp_date']}, Price: {p['price']}")
    # print(p['exp_date'])
    if p['exp_date'] != today:
        continue
    # if p['exp_date'] == today:
    p['price'] *= 0.9
    print(f"Product SKU: {p['sku']}, New price: {p['price']}")

