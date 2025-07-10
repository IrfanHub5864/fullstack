from sample import validate_marks,average_marks,garde
name=input("Enter your name: ")
marks=input("Enter your marks separated by space: ")
list_marks=list(map(int,marks.split()))
if validate_marks(list_marks):
    avg=average_marks(list_marks)
    grad=garde(avg)
    print(f"Student:{name}")
    print(f"Marks:{grad}")
    print(f"Average Marks:{avg}")
else:
    print("Invalid marks")

