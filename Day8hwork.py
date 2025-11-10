class employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)

class trainer(employee):
    def __init__(self, name, role, specialization):
        employee.__init__(self, name, role)
        self.specialization = specialization
        
    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)
        print("Specialization :", self.specialization)
        
class Yogainstructor(employee):
    def __init__(self, name, role, yoga_style):
        employee.__init__(self, name, role)
        self.yoga_style = yoga_style
        
    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)
        print("Yoga Style :", self.yoga_style) 
        

class multitrainer(trainer, Yogainstructor):
    def __init__(self, name, role, specialization, yoga_style):
        trainer.__init__(self, name, role, specialization)
        Yogainstructor.__init__(self, name, role, yoga_style)
        
    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)
        print("Specialization :", self.specialization)
        print("Yoga Style :", self.yoga_style)
        

emp = employee("Akash", "Cleaner") 
trainer1 = trainer("Nasim", "Gym Trainer", "Weight Trainer")
yoga_instructor1 = Yogainstructor("Sumi", "Yoga Instructor", "Hatha Yoga")
multi_trainer1 = multitrainer("Archa", "Senior Trainer", "Cardio Trainer", "Vinyasa Yoga")

print("Employee Details:")
emp.display()

print("\nTrainer Details:")
trainer1.display()

print("\nYoga Instructor Details:")
yoga_instructor1.display()

print("\nMulti Trainer Details:")
multi_trainer1.display()
