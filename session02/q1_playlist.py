# لیست اولیه آهنگ‌ها
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

# الف) تعداد آهنگ‌ها
a = len(playlist)
print("تعداد آهنگ‌ها:", a)

# ب) اولین و آخرین آهنگ
b = playlist[0]
c = playlist[-1]
print("اولین آهنگ:", b)
print("آخرین آهنگ:", c)

# ج) اضافه کردن آهنگ جدید به انتهای لیست
playlist.append("Dynamite")

# د) حذف آهنگ Believer
playlist.remove("Believer")

# هـ) مرتب کردن بر اساس حروف الفبا و چاپ
playlist.sort()
print("لیست مرتب شده:", playlist)

# و) چاپ شماره‌دار با حلقه for
i = 1
for a in playlist:
    print(f"{i}. {a}")
    i = i + 1
