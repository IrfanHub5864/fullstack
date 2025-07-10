def div(a,b):
   try:
       return a/b
   except ZeroDivisionError:
       return "You can't divide by zero"
a,b=map(int,input().split())
print(div(a,b))