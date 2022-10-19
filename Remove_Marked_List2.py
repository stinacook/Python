
main_list = [1,1,1,2,3,1,2,3,4]
exclude_list= [1,3]



class List:
    def __init__(self) -> None:
        pass

    def remove(self, integer_list, values_list):
        new_list = []
        for i in integer_list:
            if i not in values_list:
                new_list.append(i)
        return new_list


list_check = List()
new_list2 = list_check.remove(integer_list=main_list, values_list=exclude_list)
print(new_list2)




