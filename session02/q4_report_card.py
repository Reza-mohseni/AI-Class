
scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

passed = []
total = 0


for a in scores:
    b = scores[a]
    total = total + b
    

    if b >= 17:
        status = "عالی"
    elif b >= 14:
        status = "خوب"
    elif b >= 10:
        status = "قبول"
    else:
        status = "مردود"
        
    print(f"{a}: {b} - {status}")
    
    
    if b >= 10:
        passed.append(a)

print("قبول شده ها:", passed)

avg = total / len(scores)
print(f"میانگین کلاس: {avg}")


max_score = -1
top_student = ""
for a in scores:
    if scores[a] > max_score:
        max_score = scores[a]
        top_student = a

print(f"نفر اول : {top_student}")
