# Nathan Parker
# 03/14/25
# Program #1: Initials

# define the main function
def main():
    # get the user's name
    name = input('Enter your full name (first middle last): ')

    # split the name at each space
    name_split = name.split()

    # display the uppercase of the first letter of each item in name_split
    for string in name_split:
        print(f'{string[0].upper()}. ', end='')

# call the main function
if __name__ == '__main__':
    main()

