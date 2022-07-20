'''assignment--> concepts into programs atleast 10 examples

make sure that ineuron students, class class_type, affiliates, blog, 
internship,jobs as reference examples
'''
#inheritance

#1

import logging as lg
lg.basicConfig(filename='E:\\ineuron_projects\\i _neuron_course\\assignmemnt_6.log', level=lg.INFO)

lg.info('creating class for single inheritence')

class ineuronStudent:
    lg.info('class for student details')
    
    def __init__(self, name, package, qualification, status):
        try:
            lg.info('trying ot get inforamtion abut students')
            
            self.name=name
            self.package=package
            self.qualification=qualification
            self.status=status
            
        except Exception as e:
            lg.exception(e)
            
    
    
    def printData(self):
        lg.info('printing the information of students')
        
        print(self.name,self.package,self.qualification, self.status)
        
    def noteToNew(self):
        print(f'hello : {self.name}')

class internship(ineuronStudent):
    lg.info('class for multilevel inheritance')
    
    def __init__(self,name,package,qualification,status, projectname, stipend):
        super().__init__(name, package, qualification, status)#to use objects of parent class
        try:
            lg.info('trying to get information about internship')
            self.projectname=projectname
            self.stipend=stipend
        except Exception as e :
            lg.exception(e)
            
    def printInternshipData(self):
        lg.info('printing internship details')
        print(self.name, self.projectname, self.stipend)
        
i=internship( 'pranay','FSDS','Masters','employed','sarcasm detector', 15000)
print(i.printInternshipData())    

class course(ineuronStudent):
    def __init__(self, name, package, qualification, status, coursename):
        super().__init__(name, package, qualification, status)
        try:
            lg.info('trying info about course')
            self.coursename=coursename
        except Exception as e :
            lg.exception(e)
            
    def printCourse(self):
        print(self.name, self.coursename)
        
c=course( 'pranay','FSDS','Masters','employed','FSDS')
print(c.printCourse())


#polymorphism

class contactInfo_Student:
    def contactInfo(self, phone, email):
        try:
            lg.info('fetching contact information of the student for teacher')
            self.phone=phone
            self.email=email
        except Exception as e:
            lg.exception(e)
            
    def printDetails(self):
        print(self.phone, self.email)
        
class contactInfo_Teacher:
    def contactInfo(self, phone, email):
        try:
            lg.info('fetching contact information of the teacher for student')
            self.phone=phone
            self.email=email
        except Exception as e :
            lg.exception(e)
    def printDetails(self):
        print(self.phone, self.email)


def Details(a):
    a.printDetails()
    
s=contactInfo_Student() 
s.contactInfo(123, 'pranay')
t=contactInfo_Teacher()

Details(s)  
            
#method overriding

class FSDS(ineuronStudent):
    def __init__(self, name, package, qualification, status):
        super().__init__(name, package, qualification, status)
    
    def noteToNew(self):
        print(f'hello FSDS student : {self.name}')


f=FSDS('pranay', 'package', 'qualification', 'status')

f.noteToNew()


# multiple inheritence

class internships:
    def __init__(self,name,college,year,area_of_interest):
        try:
            lg.info('try to get info of student for internship')
            self.name=name
            self.college=college
            self.year=year
            self.area_of_interest=area_of_interest
        except Exception as e:
            lg.exception(e)
    def printDetails(self):
        print(self.name, self.college,self.year, self.area_of_interest)
        
class jobs:
    def __init__(slef, name, college, area_of_interest, experience):
        try:
            lg.info('try to get info of job professional')
            self.name=name
            self.college=college
            self.area_of_interest=area_of_interest
            self.experience=experience
        except Exception as e:
            lg.exception(e)
        
    def printDetails(self):
        print(self.name, self.college, self.area_of_interestself.experience)
        

class experiences(internships, jobs):
    pass

