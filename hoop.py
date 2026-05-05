class abc:
    msg="GOOD MORNING"
    def set_dim(self,a,b):
        self.tot=a+b
    def display(self):
        print("the sum is ",self.tot)
        print(abc.msg)
a=abc()
b=abc()
a.set_dim(20,30)
b.set_dim(40,50)
a.display()
