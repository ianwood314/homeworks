def odd_or_even(ints):
    for num in ints:
        if (num % 2) == 0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

def main():
    my_ints = [0,7,3,48,53,37,152,32,9,5]
    odd_or_even(my_ints)

if __name__ == '__main__':
    main()
