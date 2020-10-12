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
arr_list = []

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

def testcase(t):
    if (t>=1) and (t<=100):
        for i in range(t):
            n = int(input())
            print(n)
            if (n>=1) and (n<=100):
                #for i in range(n):
                elem = list(input())
                print(elem)
                list1 = [i for i in elem if (int(i)>=1) and (int(i)<=100)]
                print(list1)
            else:
                print("out of range")
                break
            arr_list.append(list1)
            print(arr_list)
    else:
        print("Invalid Input")
    result = sumOfArray(arr_list)
    return result


t = int(input())
print(t)
output = testcase(t)
print(output)
print(*output, sep="\n")
