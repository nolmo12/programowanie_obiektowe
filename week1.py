#zad 9 podpunkt d
def replaceBiggerNeighbour(list):
    for x in range(1, len(list)-2, 1):
        if(list[x]>list[x+1]):
            list[x+1]=list[x]
        else:
            list[x]=list[x+1]
    return list

lista=[1,2,4,5,2]
#zad 9 podpunkt e
def removeElements(list):
    pom=int((len(list)-1)/2)
    if(len(list)%2==0):
        list.pop(pom)
        list.pop(pom)
    else:
        list.pop(pom)
    return list
lista=[1,2,4,5,2,6]
print(removeElements(lista))
print(replaceBiggerNeighbour(lista))
#zad 9 podpunkt f
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
#zad 9 podpunkt g
def drugiNajwiekszy(list):
    pom=[list[0], list[0]]
    for x in list:
        if(x>pom[0]):
            pom[1]=pom[0]
            pom[0]=x
    return pom[1]
lista=[1,2,4,5,2]
print(drugiNajwiekszy(lista))
