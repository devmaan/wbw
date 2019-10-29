def computeSimple(string):
    sum = 0
    for ch in string:
        sum+=ord(ch)
    
    return sum

def computeByIndex(string):
    sum = 0
    for i in range(len(string)):
        sum += i*string[i]


    return sum

def main():
    string = input('> ')
    sumSimple = computeSimple(string)
    sumByIndex = computeByIndex(string)
    print('sumSimple:', sumSimple, '\nsumByIndex:', sumByIndex)

main()
