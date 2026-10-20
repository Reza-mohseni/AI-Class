# گرفتن ورودی سن و روز هفته
a = int(input("سن: "))
b = input("روز: ")

# تعیین قیمت بر اساس سن
if a < 5:
    price = 0
elif 5 <= a <= 12:
    price = 50000
elif a >= 60:
    price = 60000
else:
    price = 100000

# محاسبه تخفیف و چاپ خروجی
if price == 0:
    print("ورود رایگان")
else:
    # اگر روز سه‌شنبه باشد ۲۰ درصد تخفیف اعمال می‌شود
    if "سه شنبه" in b or "سه‌شنبه" in b:
        price = price * 0.8
    print(f"قیمت بلیط : {int(price)} تومان")
