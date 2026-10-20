
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

a = len(playlist)
print("تعداد آهنگ‌ها:", a)

b = playlist[0]
c = playlist[-1]
print("اولین آهنگ:", b)
print("آخرین آهنگ:", c)


playlist.append("Dynamite")


playlist.remove("Believer")


playlist.sort()
print("لیست مرتب شده:", playlist)

i = 1
for a in playlist:
    print(f"{i}. {a}")
    i = i + 1
