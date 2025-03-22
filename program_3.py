# Nathan Parker
# 03/14/25
# Program #3: Capital Quiz

# define the main function
def main():

    # import the random module
    import random

    # define variables
    correct = 0
    incorrect = 0

    # create dictionary
    state_capitals = {'Alabama' : 'Montgomery',
                      'Alaska' : 'Juneau',
                      'Arizona' : 'Phoenix',
                      'Arkansas' : 'Little Rock',
                      'California' : 'Sacramento',
                      'Colorado' : 'Denver',
                      'Connecticut' : 'Hartford',
                      'Delaware' : 'Dover',
                      'Florida' : 'Tallahassee',
                      'Georgia' : 'Atlanta',
                      'Hawaii' : 'Honolulu',
                      'Idaho' : 'Boise',
                      'Illinois' : 'Springfield',
                      'Indiana' : 'Indianapolis',
                      'Iowa' : 'Des Moines',
                      'Kansas' : 'Topeka',
                      'Kentucky' : 'Frankfort',
                      'Louisiana' : 'Baton Rouge',
                      'Maine' : 'Augusta',
                      'Maryland' : 'Annapolis',
                      'Massachusetts' : 'Boston',
                      'Michigan' : 'Lansing',
                      'Minnesota' : 'St. Paul',
                      'Mississippi' : 'Jackson',
                      'Missouri' : 'St. Louis',
                      'Montana' : 'Helena',
                      'Nebraska' : 'Lincoln',
                      'Nevada' : 'Carson City',
                      'New Hampshire' : 'Concord',
                      'New Jersey' : 'Trenton',
                      'New Mexico' : 'Santa Fe',
                      'New York' : 'Albany',
                      'North Carolina' : 'Raleigh',
                      'North Dakota' : 'Bismarck',
                      'Ohio' : 'Columbus',
                      'Oklahoma' : 'Oklahoma City',
                      'Oregon' : 'Salem',
                      'Pennsylvania' : 'Harrisburg',
                      'Rhode Island' : 'Providence',
                      'South Carolina' : 'Columbia',
                      'South Dakota' : 'Pierre',
                      'Tennessee' : 'Nashville',
                      'Texas' : 'Austin',
                      'Utah' : 'Salt Lake City',
                      'Vermont' : 'Montpelier',
                      'Virginia' : 'Richmond',
                      'Washington' : 'Olympia',
                      'West Virginia' : 'Charleston',
                      'Wisconsin' : 'Madison',
                      'Wyoming' : 'Cheyenne'}

    # display instructions
    print('Instructions: There will be 10 questions. Enter the capital of the given state.')

    # loop 10 times for 10 questions
    for loop in range(10):

        # randomly choose a state from the dictionary
        question = random.choice(list(state_capitals))

        # get an answer from the user
        answer = input(f'Enter the capital of {question}: ')

        # if the answer is correct display 'Correct!' and add 1 to the correct variable
        if answer == state_capitals[question]:
            print('Correct!')
            correct += 1
        # otherwise display 'Incorrect' and add 1 to the incorrect variable
        else:
            print('Incorrect')
            incorrect += 1

    # display the number of correct answers and incorrect answers
    # display the score as a percent
    print(f'''You entered {correct} correctly and {incorrect} incorrectly.
Score: {correct / 10 * 100:.0f}%''')

# call the main function
if __name__ == '__main__':
    main()

