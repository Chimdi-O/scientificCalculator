#this works with funcitions with exponents expressed as ^ and a gap between every symbol and number#
#for example 3x^2 + 6x + 2 is valid but 
# 9x**3 + 2x**2 +1  is not 

def basic_integration(function): 
    
    function = function.split(" ")

    endOfList = False 
    listIndex = 0 
    while endOfList == False: 

        if function[listIndex] == "-": 
            function[listIndex+1] =str(int(function[listIndex+1])*-1) 
            function.pop(listIndex)
            listIndex -= 1 
        if function[listIndex] == "+": 
            function.pop(listIndex)
            listIndex -= 1 

        listIndex += 1 

        if listIndex ==  len(function): 
            endOfList = True 

    integratedFunction = []

    for i in range(len(function)): 

        if "x" not in function[i]: 
            power = 0 
            coefficient = int(function[i])
        elif "^" not in function[i]: 
            power = 1 
            coefficient = int(function[i][:function[i].index("x")])
        else: 
            power = int(function[i][function[i].index("^")+1]) 
            coefficient = int(function[i][:function[i].index("x")])

            

        

        finalPower = power+1 
        finalCoefficient = coefficient/finalPower

        if str(finalCoefficient)[-2:] == ".0": 
            finalCoefficient = int(finalCoefficient)

        if finalPower == 0: 
            integratedFunction.append(str(finalCoefficient)) 
        
        elif finalPower == 1: 
            integratedFunction.append(str(finalCoefficient)+"x")

        
        else: 
            integratedFunction.append(str(finalCoefficient)+"x^"+str(finalPower))

    return integratedFunction + " + c" 
