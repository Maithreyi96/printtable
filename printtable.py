def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

def powertable(x,y):
    for i in range (1,y+1):        
        print (i**x)

if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(2,4)
    powertable(3,3)



