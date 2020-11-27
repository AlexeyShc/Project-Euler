def largest_simple_divider(number):
    divider = 2
    list_dividers = []
    while divider * divider <= number:
        while number % i == 0:
            list_dividers.append(i)
            number /= i
        i += 1
    if number > 1:
        list_dividers.append(int(number))
    print(max(list_dividers))

if __name__ == '__main__':
    number = int(input('Input number:'))
    largest_simple_divider(number)