#zad 9 podpunkt d
def replaceBiggerNeighbour(list):
    for x in range(1, len(list)-2, 1):
        if(list[x]>list[x+1]):
            list[x+1]=list[x]
        else:
            list[x]=list[x+1]
    return list

lista=[1,2,4,5,2]
print(replaceBiggerNeighbour(lista))
#zad 9 podpunkt e
def moveParzysteToTheFront(list):
    pom=[]
    for x in range(0, len(list), 1):
        if(list[x]%2==0):
            pom.append(list[x])
    for y in range(0, len(list), 1):
        if(list[y]%2!=0):
            pom.append(list[y])
    return pom
lista=[1,2,4,5,2]
print(moveParzysteToTheFront(lista))
