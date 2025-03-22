# Nathan Parker
# 03/14/25
# Program #2: Word Separator

# define the main function
def main():

    # define variable
    rewritten = ''

    # get a sentence from the user
    sentence = input('Enter a sentence with every word capitalized and no spaces: ')

    # assign the first letter of the sentence to rewritten
    rewritten += sentence[0]

    # loop the length of the sentence minus the first letter
    for index in range(1, len(sentence)):

        # set the next letter in the sentence to the character variable
        character = sentence[index]

        # if the character is uppercase, lower it and add a space
        if character.isupper():
            character = character.lower()
            rewritten = rewritten + ' '

        # add the character to the rewritten sentence
        rewritten = rewritten + character

    # display the rewritten sentence
    print(rewritten)

# call the main function
if __name__ == '__main__':
    main()
