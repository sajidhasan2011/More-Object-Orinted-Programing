class Employee:
    
    def __init__(self) :
        print("Employee Created")
        
    def __del__ (self):
        print("Destructor Called")
        
def Create_job():
    print("Starting Function....")
    obj = Employee()
    print("Function End.....")
    return obj    
    
    
obj = Create_job()
print("Program End .......")
        