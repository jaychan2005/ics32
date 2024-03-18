import tkinter as tk


# Will be used for preserving state
class Student:
    def __init__(self, name, course) -> None:
        self.name = name
        self.course = course
        
        
#Class for GUI and event handling
class StudentRegistrationGUI:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Student Registration System")
        
        self.name_label = tk.Label(master, text="Name")
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(master)          #textbox
        self.name_entry.grid(row=0, column=1)
        
        self.course_label = tk.Label(master, text="Course")
        self.course_label.grid(row=1, column=0, sticky=tk.W)
        self.course_entry = tk.Entry(master)          #textbox
        self.course_entry.grid(row=1, column=1)
        
        #Buttons!
        
        self.register_button = tk.Button(
            master, text="Register", command=self.register_student
            )
        self.register_button.grid(row=2, column=0, columnspan=2)
        
        self.remove_button = tk.Button(
            master, text="Remove", command=self.remove_student
            )
        self.remove_button.grid(row=3, column=0, columnspan=2)
        
        # Textbox for displaying registered students
        
        self.registered_textbox = tk.Text(master, height=10, width=40)
        self.registered_textbox.grid(row=4, column=0, columnspan=2)
        
        # List to store registered students
        self.registered_students = []
        
    # Method to register the students       
    def register_student(self):
        name = self.name_entry.get()
        course = self.course_entry.get()
        
        # Check if the student is already registered
        if self.is_duplicate(name, course):
            self.display_error("Student is already registered!")
        else:
            new_student = Student(name, course)
            self.registered_students.append(new_student)
            self.display_registration(
                new_student
            ) # Sending the student to be displayed !

    def is_duplicate(self, name, course):
        for student in self.registered_students:
            if student.name == name and student.course == course:
                return True
        return False
                
    def display_registration(self, student):
        # creating a string to be added to the textbox
        registration_message = (
            f"Student Registered\nName: {student.name}\nCourse:{student.course}"
        )
        self.registered_textbox.insert(tk.END, registration_message + "\n")
        
    def remove_student(self):
        if self.registered_students:
            removed_student = self.registered_students.pop()
            self.display_removal(removed_student)
            
        
    
if __name__ == "__main__":
    root = tk.Tk()
    gui = StudentRegistrationGUI(root)
    root.mainloop()