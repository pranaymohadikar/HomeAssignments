import logging as lg
lg.basicConfig(filename='E:\\ineuron_projects\\i _neuron_course\\assignment_5.log', level=lg.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

try:
    lg.info('string class started')
    class String:
        def __init__(self,s):
            self.s=s
        
        def extractData(self):
            lg.info('extract data from index one to index 300 with a jump of 3')
            return self.s[0:300:3]
        
        def Reverse(self):
            lg.info('Try to reverse a string without using reverse function ')
            return self.s[::-1]
        
        def UpperSplitConvert(self):
            lg.info('Try to split a string after conversion of entire string in uppercase')
            upper=self.s.upper()
            return upper.split()
        
        def LowerConvert(self):
            lg.info('try to convert the whole string into lower case ')
            return self.s.lower()
        
        def Capitalize(self):
            lg.info('Try to capitalize the whole string ')
            return self.s.capitalize()
        
        
            
        
except Exception as e:
    lg.exception(e)
    lg.error(e)
finally:
    lg.info('Done Deal')
    

s=String("this is My First Python programming class and i am learNING python string and its function")

#print(s.extractData())
#print(s.Reverse())
#print(s.UpperSplitConvert())
#print(s.LowerConvert())
#print(s.Capitalize())

import logging as lg
lg.basicConfig(filename='E:\\ineuron_projects\\i _neuron_course\\assignment_5.log', level=lg.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
lg.info('list class started')

class List:
    
    def __init__(self,l):
        self.l=l
        
    def Reverse(self):
        
        try:
            lg.info('Try to reverse')
            if type(self.l)==list:
                return self.l[::-1]
            else:
                lg.info('not a list')
        except Exception as e:
            lg.exception(e)


    def Extract(self):
        
        try:
            lg.info('try to access 234 out of this list')
            a=self.l[7][0]
            b=list(self.l[8].keys())[1]
            return a,b
        except Exception as e:
            lg.exception(e)
            
    
    def ExtractValues(self):
        
        try:
            lg.info('extracting dict values from list')
            dict_values=[]
            if type(self.l)==dict:
                dict_values.append(self.l.values())
            elif type(self.l)==list:
                for i in self.l:
                    if type(i)==dict:
                        dict_values.append(i.values())
            
            lg.info(f' values : {dict_values}')
            
            return dict_values
        except Exception as e:
            lg.exception(e)   
            
    def ExtractKeys(self):
        
        try:
            lg.info('extract dict keys from list')
            dict_keys=[]
            if type(self.l) ==dict:
                dict_keys.append(self.l.keys())
            elif type(self.l) == list:
                for i in self.l:
                    if type(i) ==dict:
                        dict_keys.append(i.keys())
            lg.info(f'keys : {dict_keys}')
            
            return dict_keys
        except Exception as e:
            lg.exception(e)
            
    def ExtractList(self):
        
        try:
            lg.info('extract list from list')
            lst=[]
            for i in self.l:
                if type(i) == list:
                    lst.append(i)
                    lg.info(f'list : {lst}')
            return lst
        except Exception as e:
            lg.exception(e)
            
    def ExtractTuple(self):
        
        try:
            lg.info('extracting tuples')
            tup=[]
            for i in self.l:
                if type(i) == tuple:
                    tup.append(i)
                    lg.info(f'tuple: {tup}')
            return tup
        except Exception as e:
            lg.exception(e)
                               
    def ExtractNumericData(self):
        
        try:
            lg.info('Extracting numeric data')
            num=[]
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            num.append(j) 
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == int:
                            num.append(k)
                        if type(v) == int:
                            num.append(v)
                            lg.info(f'numeric values : {num}')
            return num
        except Exception as e:
            lg.exception(e)  
            
            
lst=List([3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6), {'key1':'pranay',
                                                                  234:[23,45,656]}])

#print(lst.Reverse())
#print(lst.Extract())
#print(lst.ExtractValues())
#print(lst.ExtractKeys())
#print(lst.ExtractList())
#print(lst.ExtractTuple())
print(lst.ExtractNumericData())
