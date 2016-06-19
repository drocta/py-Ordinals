from ordinals import *

class Epsilon(Ordinal):
    def __init__(self,alpha):
        if(isinstance(alpha,(int,long))):
            alpha=Ordinal.int(alpha)
        assert(isinstance(alpha,Ordinal))
        self.vform=[1,alpha]
        self.form = [(self,1)]
        self.epsilon_alpha = alpha
        
    def __str__(self):
        return "Epsilon("+str(self.vform[1])+")"
        
    def __lt__(self,other):
        if(isinstance(other,(int,long))):
            return False
        assert(isinstance(other,Ordinal))
        if(not isinstance(other,Epsilon)):
            if(len(other.form) == 0):
                return False
            if(other.form[0][0] is other):
                print("everything like this should derive from Epsilon, so there is a problem!")
                return True # Maybe it is really big?
            if(self < other.form[0][0]):
                return True
            if(not( other.form[0][0] < self)):
                if(other.form[0][1] > 1):
                    return True
                if(len(other.form) > 1):
                    return True
                print("this probably shouldn't ever happen?")
                return False
            #otherwise self > other, so
            return False
        #otherwise other is an Epsilon
        return self.epsilon_alpha < other.epsilon_alpha

