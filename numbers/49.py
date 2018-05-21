def askfornumber():
    print('give me a number')
    number=int(input())
    return number


def findfactors(number):
    list_number=[]
    for factor in range(1,number+1):
        if number % factor == 0:
            list_number.append(factor)
    return list_number


def repeat(which1):
    length_of_1=len(factors1)
    length_of_2=len(factors2)
    global common_numbers_list
    common_numbers_list=[]
    list2_num=0
    for common_numbers in range(1,length_of_1+1):
        if factors2[which1]==factors1[list2_num]:
            common_numbers_list.append(factors1[list2_num])
        list2_num=list2_num+1
       

def commonfactors():
    length_of_1=len(factors1)
    length_of_2=len(factors2)
    for x in range(0,length_of_1):
        repeat(x)
    return common_numbers_list


def repeat3(which2):
    list4_num=0
    length_of_temparary_list=len(tempeary_greatest_list)
    for common_numbers in range(1,tempeary_greatest_list+1):
        if  [which2]<factors1[list4_num]:
            tempeary_greatest_list.append(factors1[list3_num])
        list4_num=list2_num+1


def repeat2(which3):
    list3_num=0
    tempeary_greatest_list=[]
    for common_numbers in range(1,length_of_1+1):
        if tempeary_greatest_list[which3]<factors1[list3_num]:
            tempeary_greatest_list.append(factors1[list3_num])
        list3_num=list2_num-1


if __name__ == '__main__':
    number1=askfornumber()
    # print(number1)
    number2=askfornumber()
    # print(number2)
    factors1=findfactors(number1)
    # print(factors1)
    factors2=findfactors(number2)
    # print(factors2)
    common=commonfactors()
    greatest=greatestfactor()
