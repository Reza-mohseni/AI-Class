
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


a = sentence.split()


b = []
c1 = 0  
c2 = 0  

for w in a:
    k = w.lower()
    if k in words:
        b.append(words[k])
        c1 = c1 + 1
    else:
        b.append("[" + k + "]")
        c2 = c2 + 1

ans = " ".join(b)
print(ans)


print("ترجمه شده:", c1)
print("ترجمه نشده:", c2)
