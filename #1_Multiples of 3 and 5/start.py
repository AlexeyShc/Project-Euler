def Sum_multiples_of_3_and_5(number_range):
    sum = 0
    for number in range(number_range):
        if number % 3 == 0 or number % 5 == 0:
            sum+=number
    print(sum)

if __name__ == '__main__':
    number_range = input('Input range:') 
    Sum_multiples_of_3_and_5(1000)
