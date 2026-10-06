class Student:
    def __init__(self, name, student_id, major):
        self.name = name           
        self.student_id = student_id 
        self.major = major          
    def introduce(self):
        print(f"سلام، من {self.name} هستم و در رشته {self.major} تحصیل می‌کنم.")

    def show_info(self):
        print("--- اطلاعات سیستم ---")
        print(f"شماره دانشجویی: {self.student_id}")
        print("-" * 20)

student1 = Student("رضا", 40123456, "مهندسی کامپیوتر")

student2 = Student("علی", 40198765, "هوش مصنوعی")

student1.introduce()
student1.show_info()

student2.introduce()
student2.show_info()