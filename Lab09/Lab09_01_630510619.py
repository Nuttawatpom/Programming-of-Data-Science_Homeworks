#630510619 
#nuttawat khamwangsawat
#Lab09_1

import copy
from multiprocessing.sharedctypes import Value
def upd_student(stu_list, stu_id, new_weight):
    dict_stu = {}
    for i in stu_list:
        key = i[0]
        Value = i[1:]
        dict_stu[key] = Value

    dict_stuold = copy.deepcopy(dict_stu) 
    if stu_id in dict_stu:
        dict_stu[stu_id][2] = new_weight
    else:
        new_data = ['', 0, new_weight]
        dict_stu[stu_id] = new_data

    return(dict_stuold,dict_stu)


if __name__=="__main__":
    main()