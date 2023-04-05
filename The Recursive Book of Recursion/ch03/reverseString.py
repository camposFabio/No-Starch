def rev(theString):
    #if len(theString) == 0 or len(theString) == 1:
    if len(theString) <= 0: 
        # BASE CASE
        return theString
    else:
        # RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head
    
print(rev('abcdef'))
print(rev('Hello, world!'))
print(rev(''))
print(rev('X'))