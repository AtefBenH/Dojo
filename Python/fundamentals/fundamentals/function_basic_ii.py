#1- Countdown 
def countdown (num) :
    result = []
    for i in range (num, -1, -1):
        result.append(i)
    return result

#2- Print and Return
def print_and_return (list):
    print (list[0])
    return list [1]

#3- First Plus Length
def first_plus_length (list):
    return list[0]+len(list)

#4- Values Greater than Second
def values_greater_than_second (list):
    result= []
    if len(list)<2 :
        return False
    else :
        for i in list :
            if i > list [1] :
                result.append(i)
        return result

#5 This Length, That Value
def length_and_value (size, value):
    result = []
    for i in range (size) :
        result.append(value)
    return result


#Main
my_list = [5, 3, 68, 2, 4, 1]

# print (countdown(100))

# x = print_and_return([5,10])
# print(x)

# print (first_plus_length(my_list))

# print(values_greater_than_second(my_list))
# print(values_greater_than_second([3]))

print (length_and_value(7,9))