# دیکشنری کلمات
words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "book": "کتاب",
    "hello": "سلام",
    "student": "دانشجو",
    "code": "کد",
    "good": "خوب"
}

sentence = "I love python and AI"

# تکه تکه کردن جمله
a = sentence.split()

# لیست برای ذخیره کلمات ترجمه شده
b = []
c1 = 0  # تعداد ترجمه شده‌ها
c2 = 0  # تعداد ترجمه نشده‌ها

for w in a:
    k = w.lower()
    if k in words:
        b.append(words[k])
        c1 = c1 + 1
    else:
        b.append("[" + k + "]")
        c2 = c2 + 1

# چاپ جمله ترجمه شده در یک خط
ans = " ".join(b)
print(ans)

# بخش اضافه: تعداد کلمات
print("ترجمه شده:", c1)
print("ترجمه نشده:", c2)
