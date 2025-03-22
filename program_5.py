# Nathan Parker
# 03/14/25
# Program #5: Course Info

# define the main function
def main():

    # define variable
    answer = 0

    # create an empty dictionary
    courses = {}

    # loop through the program until the user enters 3
    while answer != '3':

        # display the instructions
        print('''Enter the number of the desired action.
1 - Add an item to the dictionary.
2 - Look up an item from the dictionary.
3 - Exit the program.''')

        # get an answer from the user
        answer = input()

        # call the function that corresponds with the user's choice
        if answer != '1' and answer != '2' and answer != '3':
            while answer != '1' and answer != '2' and answer != '3':
                answer = input("Enter '1', '2', or '3': ")
        if answer == '1':
            add_1(courses)
        if answer == '2':
            look_up_2(courses)

# define the add_1 function
def add_1(courses):

    # get a course ID from the user
    course_id = input('Enter the course ID: ').upper()

    # if it is as new course ID, get the name and add it to the dictionary
    if course_id not in courses:
        course_name = input('Enter the course name: ')
        courses[course_id] = course_name
        print()
    else:
        print(f'{course_id} has already been entered.')
        print()

# define the look_up_2 function
def look_up_2(courses):

    # get a subject from the user
    subject = input('Enter a subject: ').upper()

    # create a dictionary that contains the items from the courses dictionary that are in the subject
    dictionary_of_subject = {k:v for k,v in courses.items() if k[:2] == subject[:2]}

    # create a dictionary that limits the keys of dictionary_of_subject to the first 3 characters
    # this dictionary will be searched and dictionary_of_subject will be displayed
    first_3_char_of_subject = {k[:3]:v for k,v in dictionary_of_subject.items()}

    # if the subject is in the dictionary, display every course in that subject
    if subject in first_3_char_of_subject:
        print(f'Here are the classes that are in the {subject} subject:')
        for k,v in dictionary_of_subject.items():
            print(k,v)
        print()
    else:
        print('Subject not found.')
        print()

# call the main function
if __name__ == '__main__':
    main()

