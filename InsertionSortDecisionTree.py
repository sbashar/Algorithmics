import itertools

elementPermutation = list(itertools.permutations([1, 2, 3]))

for elementList in elementPermutation:
    elementList = list(elementList)
    inputSequence = "Input sequence:"
    sortedSequence = "Sorted sequence:"
    for i in range(len(elementList)):
        inputSequence += " a" + str(i+1) + " = " + str(elementList[i])
    print(inputSequence)
    for i in range(1,len(elementList)):
        j = i
        while j > 0:
            if elementList[j-1] > elementList[j]:
                print("a" + str(j) + " > a" + str(j+1))
                temp = elementList[j]
                elementList[j] = elementList[j-1]
                elementList[j-1] = temp
                j = j - 1
            else:
                print("a" + str(j) + " <= a" + str(j+1))
                break
    for i in range(len(elementList)):
        sortedSequence += " a" + str(i+1) + " = " + str(elementList[i])
    print(sortedSequence)
