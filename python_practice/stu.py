class student:
    def __init__(self,name,sub,gpa):
        self.name=name
        self.sub=sub
        self.gpa=gpa  
        
    
    def fail(self):
        if self.gpa>6:
            return False
        else:
            return True
    

    