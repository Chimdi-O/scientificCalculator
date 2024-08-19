





from indefinate_integration import * 

def definate_basic_integration(lim1,lim2,function): 
    lim1total = 0 
    lim2total = 0
    integrated_function = basic_integration(function)
    integrated_function = integrated_function.split(" + ")[:-1]
    integrated_function_copy = integrated_function.copy()
    print(integrated_function_copy)


    for i in range(len(integrated_function)): 
        if "x" in integrated_function[i]: 
            xIndex = integrated_function[i].find("x")
            if "^" in integrated_function[i]: 
                powerindex = integrated_function[i].find("^")
                integrated_function[i]  = float(integrated_function[i][:xIndex])*lim1**float(integrated_function[i][powerindex+1:])
            else: 
                integrated_function[i]  = float(integrated_function[i][:xIndex])*lim1


    for i in integrated_function: 
        lim1total += i 

    for i in range(len(integrated_function_copy)): 
        print(integrated_function_copy)
        if "x" in integrated_function_copy[i]: 
            xIndex = integrated_function_copy[i].find("x")
            if "^" in integrated_function_copy[i]: 
                powerindex = integrated_function_copy[i].find("^")
                integrated_function_copy[i]  = float(integrated_function_copy[i][:xIndex])*lim2**float(integrated_function_copy[i][powerindex+1:])
            else: 
                integrated_function_copy[i]  = float(integrated_function_copy[i][:xIndex])*lim2


    for i in integrated_function_copy: 
        lim2total += i 

    return  lim1total - lim2total



    
    
    

