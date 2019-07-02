class Test:
    def msg(self):
        print("Running successfully")
    #constructor--it call automatically when the object is created
    #whose task is to initialize data member
    #__init__ is special method
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("automatically calls",self.cpu,self.ram)

    '''def __init__(self):
        print("without parameter")'''


t1=Test("Corei3",'8Gb')
t2=Test("Corei5",'16Gb')
#t3=Test()
t1.msg()
t2.msg()
