def find_common(which_length,which_length_2):
    for list_number in range(1,which_length):
        for common in range(1,which_length_2):
            find_common=0
            if numbers_1[list_number]==numbers_2[find_common]:
                common_numbers.append(numbers_1[list_number])    
            find_common=find_common+1 


def main():
    factor_1=int(input('give me a number:'))
    factor_2=int(input('give me another number:'))
    # print(factor_1)
    # print(factor_2)
    numbers_1=[]
    numbers_2=[]
    for number_1 in range(1,factor_1+1):
         if factor_1 % number_1 == 0:
            numbers_1.append(number_1)
    for number_2 in range(1,factor_2+1):
        if factor_2 % number_2 == 0:
            numbers_2.append(number_2)
    # print(numbers_1)
    # print(numbers_2)
    length_of_1=len(numbers_1)
    length_of_2=len(numbers_2)

    common_numbers=[]

        
    if length_of_1 >= length_of_2:
        find_common(length_of_1,length_of_2)
    elif length_of_1 <= length_of_2:
        find_common(length_of_2,length_of_1)
    print(common_numbers)
    # elif length_of_1 < length_of_2:

if __name__ == '__main__':
    main()
