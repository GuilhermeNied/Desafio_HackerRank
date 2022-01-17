class No(object):
 
   def __init__(self, data=None, prox_no=None):
       self.data = data
       self.prox = prox_no


def Ciclo(head):
    devagar = head
    rapido = head.prox
    count = 0
    while devagar and rapido and count==0:
        if devagar == rapido:
            count=1
        else:
            devagar= devagar.prox
            rapido = rapido.prox.prox
    if rapido !=None or count == 1:
        return(1)
    else:
        return(0)    
    







