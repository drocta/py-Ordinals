"""
This handles ordinal numbers in python using cantor normal form.
This uses natural operations (hessenberg operations) on ordinals.
This only expresses ordinals less than epsilon_0.
"""


class Ordinal:
    def __init__(self,form=[]):
        """Create an Ordinal object from a list of pairs of an ordinal object and a positive integer"""
        assert(type(form)==list)
        for p in form:
            assert(type(p) == tuple)
            assert(len(p) == 2)
            assert(isinstance(p[0],Ordinal))
            #type(p[1]) should be a positive integer
        self.form = form
    
    def formToStr(self,form):
        if(form == []):
            return '0'
        if(len(form)>1):
            return " + ".join([self.formToStr([p]) for p in form])
        if(form[0][0].form == []):
            return str(form[0][1])
        if(form[0][1] == 1):
            if(len(form[0][0].form) == 1):
                if(str(form[0][0]) == "1"):
                    return 'w'
                return "w**" + str(form[0][0])
            return "w**(" + str(form[0][0]) + ")"
        if(len(form[0][0].form) == 1):
            if(str(form[0][0]) == "1"):
                return str(form[0][1]) + 'w'
            return str(form[0][1]) + "*w**" + str(form[0][0])
        return str(form[0][1]) + "*w**(" + str(form[0][0]) + ")"
        
    
    def __str__(self):
        return self.formToStr(self.form)
    
    def toPureForm(self):
        """This gets the ordinal as expressed purely using lists tuples and integers."""
        return [(p[0].toPureForm(),p[1]) for p in self.form]
    
    def is_finite(self):
        if(len(self.form) == 0):
            return True
        if(self.form[0][0].form == []):
            return True
        return False

    def to_int(self):
        assert(self.is_finite())
        if(len(self.form)==0):
            return 0
        return self.form[0][1]

    def __lt__(self,other):
        """Checks whether self is less than other"""
        if(isinstance(other,(int,long))):
            return self.__gt__(self.int(other))
            
        if(len(other.form) == 0):
            return False
        n = min(len(other.form),len(self.form))
        i = 0
        while(i < n):
            if(self.form[i][0] < other.form[i][0]):
                return True
            if(other.form[i][0] < self.form[i][0]):
                return False
            if(self.form[i][1] < other.form[i][1]):
                return True
            if(other.form[i][1] < self.form[i][1]):
                return False
            i += 1
        if(len(self.form) < len(other.form)):
            return True
        return False
    
    def __gt__(self,other):
        """Checks whether self is greater than other"""
        if(isinstance(other,(int,long))):
            return self.__gt__(self.int(other))
        return other < self
        
    def __eq__(self,other):
        """checks whether self is equal to other"""
        return not((self < other) or (self > other))
            
    def __add__(self, other):
        if(isinstance(other,(int,long))):
            return self.__add__(self.int(other))
        n = len(self.form)
        m = len(other.form)
        i = 0
        j = 0
        resultList = []
        while((i < n) and (j < m)):
            if(self.form[i][0] < other.form[j][0]):
                resultList.append(other.form[j])
                j += 1
            elif(other.form[j][0] < self.form[i][0]):
                resultList.append(self.form[i])
                i += 1
            else:
                resultList.append((self.form[i][0],self.form[i][1]+other.form[j][1]))
                i += 1 
                j += 1
        while(i < n):
            resultList.append(self.form[i])
            i += 1
        while(j < m):
            resultList.append(other.form[j])
            j += 1
        return Ordinal(resultList)
    
    def __radd__(self,other): #handles int + Ordinal
        if(isinstance(other,(int,long))):
            return self.__add__(self.int(other))
        else:
            print("couldn't add " + str(other) + "+" + str(self))
            return self.int(0)
    
    def __mul__(self,other):
        if(isinstance(other,(int,long))):
            return self.__mul__(self.int(other))
        if(len(self.form) == 0):
            return self
        if(len(other.form) == 0):
            return other
        if(len(self.form) == 1):
            if(len(other.form) == 1):
                return Ordinal([(self.form[0][0]+other.form[0][0],self.form[0][1] * other.form[0][1])])
            return reduce((lambda x,y:x+y),map((lambda y: self*y),[Ordinal([p]) for p in other.form]))
        return reduce((lambda x,y:x+y),map((lambda x:x*other),[Ordinal([p]) for p in self.form]))
    
    def __rmul__(self,other): # allows int * ordinal
        if(isinstance(other,(int,long))):
            return self.__mul__(self.int(other))
        else:
            print("couldn't multiply " + str(other) + "*" + str(self))
            return self.int(0)
    
    def __pow__(self,other):#allows using w**w**w**3, or w**(w**2+w+7)
        """This only currently supports powers where the base is w,
        or where the base is 0 or 1, or where the power is finite.
        This allows using w**w**w**3, or w**(w**2+w+7).
        This should make expressing some ordinals more convenient."""
        #This would be in __xor__ instead, but because of operator priority, ** works better than ^ .
        
        if(isinstance(other,(int,long))):
            return self.__pow__(self.int(other))
        
        if(str(self) in ('0','1')):
            return self
        
        if(str(self) == 'w'):
            if(other.form[0][0] == other):
                return other
            return Ordinal([(other,1)])
        
        if(other.is_finite()):
            n = other.to_int()
            if(n == 1):
                return self
            if(n == 0):
                return self.int(1)
            n2 = n/2
            n1 = n - 2*n2
            temp = (self**n2)
            return (self**n1)*(temp)*(temp)
        
        #otherwise, we don't know what to do, so give warning and return the 0 ordinal
        print("WARNING: __pow__ not defined for these parameters, and defaults to 0 instead.")
        print(self)
        print(other)
        return Ordinal([])
        
    def __xor__(self,other): 
        if(str(self) != 'w'):
            print("WARNING: __xor__ not defined for bases other than w, and defaults to __pow__ instead")
            print(self)
            return self**other #returns the exponent
        return Ordinal([(other,1)])

    @classmethod
    def int(cls,n):
        """Create an ordinal from an integer.
        Use is (e.g.): Ordinal.int(5)
        to produce the ordinal 5."""
        assert(isinstance(n,(int,long)) and n >= 0)
        if(n == 0):
            return Ordinal([])
        return Ordinal([(Ordinal.int(0),n)])


z = Ordinal([])
sz = Ordinal([(z,1)])
w = Ordinal([(sz,1)])
