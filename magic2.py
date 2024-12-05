class Time:
    def __init__(self,hour,mint,second):
        self.hour=hour
        self.mint=mint
        self.second=second
    def __str__(self):
        print("hello")
        return""

t1=Time(3,4,5)
print(t1.__str__())
print(dir(t1))