def sublist(list, selected):
    
    if list == []:
        
        print (selected)
    
    else:
        
        tem = list[0]
        
        remainder = list[1:]
        
        sublist(remainder, selected+[tem]) # tem participates
        sublist(remainder, selected)       # tem doesn't participate
    

guest = ["a","b","c"]

print (sublist(guest, []))


def sublist2(list, selected):
    
    if list == []:
        
        return [selected]
    
    else:
        
        tem = list[0]
        
        remainder = list[1:]
        
        return sublist2(remainder, selected+[tem]) +  sublist2(remainder, selected)  
    

guest = ["a","b","c"]

print (sublist2(guest, []))
