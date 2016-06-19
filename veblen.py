from epsilon import *

class Veblen(Epsilon):
    def __init__(self,veblinForm):
        assert(isinstance(veblinForm,(list,tuple)))
        for p in veblinForm:
            assert(isinstance(p,(Ordinal,int,long)))
        for i in range(len(veblinForm)):
            if(isinstance(veblinForm[i],(int,long))):
                veblinForm[i]=Ordinal.int(veblinForm[i])
        assert(len(veblinForm) > 0)
        while(veblinForm[0] == 0):
            veblinForm = veblinForm[1:]
            assert(len(veblinForm) > 0)
        self.vform = veblinForm
        vform = self.vform
        if(len(vform) == 1):
            self.form=[(vform[0],1)]
            return
        #otherwise
        self.form = [(self,1)] #fixed points of w** , so cantor normal form does this.
        if((len(vform) == 2) and (vform[0] == 1)):
            self.epsilon_alpha = vform[1]
        else:
            self.epsilon_alpha = self
        
    def __str__(self):
        return 'phi('+','.join([str(p) for p in self.vform])+')'
        
    def __lt__(self,other):
        if(isinstance(other,(Veblen,Epsilon))):
            if(len(self.vform) == len(other.vform)):
                i = 0
                while((i < len(self.vform)) and (self.vform[i] == other.vform[i])):
                    i += 1
                if(i == len(self.vform)):
                    return False
                if(self.vform[i] < other.vform[i]):
                    j = i+1
                    while(j < len(self.vform)):
                        if(not (self.vform[j] < other)):
                            return False
                        j += 1
                    return True
                else: # it isn't equal, so self.vform[i] > other.vform[i]
                    j = i+1
                    while(j < len(self.vform)):
                        if(self < other.vform[j]):
                            return True
                        j += 1
                    return False
                #this line never reached
            if(len(self.vform) < len(other.vform)):
                for p in self.vform:
                    if(not (p < other)):
                        return False
                return True
            if(len(self.vform) > len(other.vform)):
                for p in other.vform:
                    if(self < p):
                        return True
                return False #Warning: this might be wrong for cases where self == p sometimes. Not sure.
            

def phi(*args):
    if(len(args)==0):
        return z
    if(len(args)==1):
        return w**args[0]
    if((len(args)==2) and (args[0]==sz)):
        return Epsilon(args[1])
    return Veblen(list(args))
