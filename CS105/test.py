class Listops():

    def  __init__(self,inlist):
        self.xlist=inlist

    def charsearch(self,sval):
        # write your code here
        contador = 0 
        for element in self.xlist:
            if element[0] == sval:
                contador+=1
        
        return contador

xlist = ['asdf', 'dfgh', 'sdfg', 'sfghj', 'swertq', 'qtyiu']

listOps = Listops(xlist)

import re

def sget(s):
    # Use regular expression to find all strings beginning with 'c', 'd', or 'e'
    matches = re.findall(r'\b[cde]\d+\b', s)
    
    # Filter the matches to keep only those containing '45'
    result = [match for match in matches if '45' in match]
    
    return result






            