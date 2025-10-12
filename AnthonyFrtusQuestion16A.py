# Question 16(a)
# Student name: Anthony Frtus
def Username():
    Name = input("Please enter your username:")
    print("Welcome", Name, ", to the student result calculator")
    
Username()
student_name = input("Please enter the students name: ")
student_score = float(input("Please enter the students mark: "))
score_as_a_percentage = round(student_score/int(input("Please enter the total amount of marks going for the exam:"))*100, 1)

print(student_name,"scored",score_as_a_percentage,"%")
if score_as_a_percentage < 59.9:
    print(student_name,"scored",score_as_a_percentage,"%. They got a C")
elif score_as_a_percentage < 79.9:
    print(student_name,"scored",score_as_a_percentage,"%. They got a B")#
else:
    print(student_name,"scored",score_as_a_percentage,"%. They got an A")