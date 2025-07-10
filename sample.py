def validate_marks(marks):
    return all(0<mark<100 for mark in marks)
def average_marks(marks):
    return sum(marks)/len(marks)
def garde(average):
    if average>90:
       return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"
    
