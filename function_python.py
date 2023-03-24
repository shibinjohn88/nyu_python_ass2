def max_num (num1, num2, num3):
    return max ([num1, num2, num3])

def mult_list (list):
    if len (list) == 0:
        return 0
    else:
        prod = list[0]
        for i in list[1:]:
            prod *= i
        return prod

def rev_string (str):
    return str[::-1]
    
def num_within (num, start, end):
    return num in range(start, end+1)

def pascal (n):
    triangle = [[1], [1,1]]
    if n < 1:
        print("number should be greater than 0")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
    #make rows for triangle
        while len (triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            #create new row 
            length = len (row_prev) + 1
            for i in range (length):
                #first number is always 1
                if i == 0:
                    row.append(1)
                #middle numbers are made based on previous rows 
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number-1][i-1] + + triangle[row_number-1][i])
                #last number is also 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for i in triangle:
            print (i)



    
#test case

print (max_num (1,2,3))
print (mult_list ([]))
print (mult_list ([2, 4, 5]))
print (rev_string ('apple'))
print (num_within (3,2,4))
print (num_within (3,1,3))
print (num_within (10,2,5))
(pascal (3))