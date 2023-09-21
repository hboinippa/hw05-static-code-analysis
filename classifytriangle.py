
def classifyTriangle(a,b,c):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "Input must be numerical."

  
    
    #if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        #return "Right"
    if (a <= 0 or b<=0 or c<=0) or ((a > b + c) or (b > a + c) or (c > a + b)):
        return "NotATriangle"
    elif a == b == c:
        return "Equilateral" 
    elif a == b or b == c or c == a:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Right"
        else:

            return "Isosceles"
    #elif (a!=b) and (b!=c) and (a!=c):
    else:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Right"
        else:
            return "Scalene"
    #else:
        #return "NotATriangle"

#print(classifyTriangle(1,1,1.5))
