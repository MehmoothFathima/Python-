"""
Given an integer array A of size N, find sum of elements in it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of input. First line contains N the size of the array A. The second line contains the elements of the array.

Output:
For each testcase, print the sum of all elements of the array in separate line.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Ai <= 100

Example:
Input:
2
3
3 2 1
4
1 2 3 4
Output:
6
10

"""



list1 = []
list2 = []
arr_list = []
t = int(input())
print(t)
if (t>=1) and (t<=100):
    for i in range(t):
        n = int(input())
        print(n)
        if (n>=1) and (n<=100):
            elem = input()
            elem1 = elem.split()
            for i in elem1:
                print(i)
                if (int(i)>=1) and (int(i)<=100):
                    list1.append(i)
                    print(list1)
                else:
                    print("Invalid Input")
                    break
            if len(list1) != n:
                print("out of range")
                break
            list2 = list1.copy()
            arr_list.append(list2)
            list1.clear()
        else:
            print("Invalid Input")
else:
    print("Invalid Input")

def sumOfArray(arr_list):
    out_list = []
    result1 = []
    sum = 0
    for i in arr_list:
        for j in i:
            sum += int(j)
        out_list.append(sum)
        sum = 0
    return out_list



result = sumOfArray(arr_list)
print(*result, sep="\n")
