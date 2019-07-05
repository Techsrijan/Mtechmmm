class Student:
    def getdata(self,name,roll):
        self.name=name
        self.roll=roll

class Theory(Student):
    def getmarks(self,part1,part2):
        self.part1=part1
        self.part2=part2

class Result(Theory):
    def display(self):
        print("Name=",self.name)
        print("Roll no=",self.roll)
        print("Part1=",self.part1,"Part2=",self.part2)
        total=self.part1+self.part2
        print("total=",total)


S=Result()
S.getdata("Ram",100)
S.getmarks(250,300)
S.display()