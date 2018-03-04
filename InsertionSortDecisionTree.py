import itertools

threeElementPermutation = list(itertools.permutations([1,2,3,4]))

for elementList in threeElementPermutation:
    elementList = list(elementList)
    print(elementList)
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
