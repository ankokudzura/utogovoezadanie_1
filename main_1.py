import re
def filling_list(tmp_list):
    new_variable=''
    while True:
        new_variable = input("Please enter veriable, or press enter to finish: ")
        if new_variable == '':
            return tmp_list
        tmp_list.append(new_variable)
def solution (list1):
    for i in list1:
        counter = [0, 0, 0, 0, 0]
        for j in i:
            if re.search("[`1234567098\-=~!@#$%^&*()_+]", j): counter[0] += 1
            if re.search("[`qwertyuiop\[\]QWERTYUIOP{}|]", j): counter[1] += 1
            if re.search("[asdfghjklASDFGHJKL;':\"]", j): counter[2] += 1
            if re.search("[zxcvbnm,\.\/ZXCVBNM<>\?]", j): counter[3] += 1
            if (j == " "): counter[4] += 1
        cout = 0
        for k in counter:
            if k > 0:
                cout += 1
        if cout > 1:
            list1.remove(i)
    print(list1)



print("Enter data for the  list")
list1=[]
filling_list(list1)
solution(list1)