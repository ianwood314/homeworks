def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [1,4,9,16,25,36,49,64,81,100]
    list3 = [1,8,27,64,125,216,343,512,729,1000]

    for num1,num2,num3 in zip(list1,list2,list3):
        print(f'{num1} {num2:5} {num3:5}')
main()
