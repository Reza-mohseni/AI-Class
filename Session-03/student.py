class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # دیکشنری نمرات

    # اضافه کردن نمره
    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
        else:
            self.grades[course] = grade

    # محاسبه میانگین
    def average(self):
        if len(self.grades) == 0:
            return 0
        
        s = 0
        for k in self.grades:
            s = s + self.grades[k]
        
        avg = s / len(self.grades)
        return avg

    # درسی با بالاترین نمره
    def best_course(self):
        max_grade = -1
        best_name = ""
        for c in self.grades:
            if self.grades[c] > max_grade:
                max_grade = self.grades[c]
                best_name = c
        return best_name

    # درس‌های افتاده (زیر ۱۰)
    def failed_courses(self):
        bad_courses = []
        for c in self.grades:
            if self.grades[c] < 10:
                bad_courses.append(c)
        return bad_courses

    # تعیین وضعیت دانشجو
    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    # چاپ کارنامه
    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        for c in self.grades:
            print(f"{c}: {self.grades[c]}")
        
        print(f"Average: {self.average():.1f}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")
        print("---------------------------------")


# --- بخش امتیازی: کلاس Classroom ---
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        best_s = None
        max_avg = -1
        for s in self.students:
            if s.average() > max_avg:
                max_avg = s.average()
                best_s = s
        return best_s

    def class_average(self):
        if len(self.students) == 0:
            return 0
        tot = 0
        for s in self.students:
            tot = tot + s.average()
        return tot / len(self.students)


# --- تست برنامه با متغیرهای a و b ---

# دانشجوی اول
a = Student("Sara Ahmadi", "40312345")
a.add_grade("Math", 18)
a.add_grade("Physics", 9)
a.add_grade("Programming", 20)
a.add_grade("English", 15)

# دانشجوی دوم
b = Student("Ali Rezaei", "40312346")
b.add_grade("Math", 11)
b.add_grade("Physics", 8)
b.add_grade("Programming", 14)
b.add_grade("English", 10)

print("--- کارنامه دانشجو ۱ ---")
a.report()

print("--- کارنامه دانشجو ۲ ---")
b.report()

print("--- تست نمره نامعتبر ---")
a.add_grade("Chemistry", 25)

print("\n--- تست بخش امتیازی (Classroom) ---")
c = Classroom()
c.add_student(a)
c.add_student(b)

top = c.top_student()
print(f"Top Student: {top.name} with average: {top.average():.2f}")
print(f"Class Average: {c.class_average():.2f}")
