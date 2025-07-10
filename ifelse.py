class Name:
    def visible(self,name=None,age=None,gender=None):
        print(name)
        '''if name and age and gender:
            print("3 arg")
        elif name and age:
            print("2 arg")
        elif name:
            print("1 arg")
        else:
            print("0 arg")'''
name=Name()
name.visible()
name.visible(name="irfan",age=18,gender="male")
name.visible(18)