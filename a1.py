class employee:
    def __init__(self):
        print("employee creater")
    def __del__(self):
        print("Employee object deleted")

obj=employee() # constructor
del obj # destructor