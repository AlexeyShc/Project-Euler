def sum_even_Fibonacci_numbers(last_number):
    first_element = 1
    second_element = 2
    sum = 0
    while second_element < last_number:
        next_element = first_element + second_element
        first_element = second_element
        if second_element % 2 == 0:
            sum+=second_element
        second_element = next_element
    print(sum)


if __name__ == '__main__':
    last_number = int(input('Input last number:'))
    sum_even_Fibonacci_numbers(last_number)
