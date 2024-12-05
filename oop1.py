class Time():
          def setdata(self,hour,mint,second):
                    self.hour=hour
                    self.mint=mint
                    self.second=second
      
          def __truediv__(self,temp):
                   self.hour=self.hour/temp.hour
                   self.mint=self.mint/temp.mint            
                   self.second=self.second/temp.second
          #def add(self,temp):  
                #x=Time()
                #x.setdata(0,0,0)
                #x.hour=self.hour+temp.hour
                #x.mint=self.mint+temp.mint
                #x.second=self.second+temp.second
                #return x
          def display(self):
                 print(self.hour,end=" ")
                 print(self.mint,end=" ")
                 print(self.second,end=" ")
            
                 print()
t1=Time()
t1.setdata(52,5,160)  

t2=Time()
t2.setdata(48,1,120) 
t1/t2

t1.display()
#x=Time()
#x.setdata(0,0,0)

#t1.add(t2,t3) 
#t1.display() 
#t3=t1.add(t2)  
#t3.display()                       