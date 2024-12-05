class Time():
    def __init__(self,hour,mint,second):
        self.hour=hour
        self.mint=mint
        self.second=second
    def display(self):
        print(self.hour,end=" ")
        print(self.mint,end=" ")
        print(self.second,end=" ")

        print()
        
        
t1=Time(5,60,70)
t1.display()    