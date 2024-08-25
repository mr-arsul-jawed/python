def compareTheList(list1,list2):
    if len(list1) != len(list2):
        return False
    for  i in range(len(list1)) :
        if list1[i] != list2[i] :
            return False
    else : return True

list1 = list(input("Enter first list :").split())
list2 = list(input("Enter second list :").split())
print("Is both the list same :", compareTheList(list1, list2))