def calc_qb():
    None
    #convert stats to int
    #compare stats through algorithm
    
def calc_rb():
    None
    #convert stats to int
    #compare stats through algorithm
    
def calc_wr():
    None
    #convert stats to int
    #compare stats through algorithm
    

    
if __name__ == "__main__":
    quaterbacks = []  # List to store the converted integers

    with open('qbs.txt', 'r') as file:
        q=0
        for line in file:
            q=q+1
            if q==1:
                element = line.strip()
                quaterbacks.append(element)
                
                
            elif q==3:
                element = float(line.strip())
                quaterbacks.append(element)
                q=0

            else:
                continue
            # Remove any leading/trailing whitespace and convert to integer


    print(quaterbacks)

    
    backs = []  # List to store the converted integers
    
    with open('rbs.txt', 'r') as file:
        q=0
        for line in file:
            q=q+1
            if q==1:
                element = line.strip()
                backs.append(element)
                
                
            elif q==3:
                element = float(line.strip())
                backs.append(element)
                q=0

            else:
                continue
    print(backs)

    recievers = []  # List to store the converted integers
    
    with open('wrs.txt', 'r') as file:
        q=0
        for line in file:
            q=q+1
            if q==1:
                element = line.strip()
                recievers.append(element)
                
                
            elif q==3:
                element = float(line.strip())
                recievers.append(element)
                q=0
                
            else:
                continue
    print(recievers)



    ends = []  # List to store the converted integers
    
    with open('tes.txt', 'r') as file:
        q=0
        for line in file:
            q=q+1
            if q==1:
                element = line.strip()
                ends.append(element)
                
            elif q==3:
                element = float(line.strip())
                ends.append(element)
                q=0
            else:
                continue
    print(ends)
    
    sal = []  # List to store the converted integers
    
    with open('salaries.txt', 'r') as file:
        q=0
        for line in file:
            q=q+1
            if q==1:
                element = line.strip()
                sal.append(element)
             
            elif q==3:
                element = float(line.strip())
                sal.append(element)
                q=0
            else:
                continue
    print(sal)






