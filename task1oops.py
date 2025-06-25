class Student:
    def __init__(self,name,roll_number,marks):
        self.nm = name
        self.r = roll_number
        self.m = marks

    def display_percentage(self):
        total = (
            self.m["Math"] +
            self.m["Science"] +
            self.m["Hindi"] +
            self.m["English"] +
            self.m["History"]
        )
        percentage = total / 5
        print("\n---Student Details---")
        print("Name-->",self.nm)
        print("Roll_Number-->",self.r)
        print("Marks-->",self.m)
        print("Percentage-->",round(percentage,2),"%")
nm = "Shekhar"   
r = 7
m = {
    "Math":80,
    "Science":87,
    "Hindi":86,
    "English":90,
    "History":88
}  
s1 = Student(nm,r,m)
s1.display_percentage()  


