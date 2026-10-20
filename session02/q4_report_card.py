# دیکشنری نمرات
scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

passed = []
total = 0

# الف و ب: چاپ رتبه هر دانشجو و جمع‌آوری قبول شده‌ها
for a in scores:
    b = scores[a]
    total = total + b
    
    # تعیین وضعیت نمره
    if b >= 17:
        status = "عالی"
    elif b >= 14:
        status = "خوب"
    elif b >= 10:
        status = "قبول"
    else:
        status = "مردود"
        
    print(f"{a}: {b} - {status}")
    
    # نمرات ۱۰ و بالاتر
    if b >= 10:
        passed.append(a)

print("قبول شده ها:", passed)

# ج) میانگین کلاس
avg = total / len(scores)
print(f"میانگین کلاس: {avg}")

# د) پیدا کردن نفر اول
max_score = -1
top_student = ""
for a in scores:
    if scores[a] > max_score:
        max_score = scores[a]
        top_student = a

print(f"نفر اول : {top_student}")
