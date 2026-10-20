
a = int(input("سن: "))
b = input("روز: ")


if a < 5:
    price = 0
elif 5 <= a <= 12:
    price = 50000
elif a >= 60:
    price = 60000
else:
    price = 100000


if price == 0:
    print("ورود رایگان")
else:
    
    if "سه شنبه" in b or "سه‌شنبه" in b:
        price = price * 0.8
    print(f"قیمت بلیط : {int(price)} تومان")
