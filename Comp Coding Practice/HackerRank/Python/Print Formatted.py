def print_formatted(n):
    # your code goes here
    length = len(bin(n)) - 1
    for i in range(1, n + 1):
        print(f"{i: >{length -1}}{oct(i)[2:]: >{length}}"
              f"{hex(i)[2:].upper(): >{length}}{bin(i)[2:]: >{length}}")
    return


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
