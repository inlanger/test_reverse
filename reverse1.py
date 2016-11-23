def inverse_int(x):
    num = x
    output = 0

    n = 1
    div = 1
    while n >= 1:
        div *= 10
        n = num/div

    div /= 10

    if div == 1:
        return x

    n = 1
    while n >= 1:
        output += (num%10) * div
        div /= 10
        num = (num - num%10)/10
        n = num / 10

    output += num

    return output

input_num = input("Enter some integer: ")

print(inverse_int(input_num))