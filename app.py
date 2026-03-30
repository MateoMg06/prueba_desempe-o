from menu_students import menu_students
from validations import validation
from validations import validations
from add_students import add_student
from show_students import show_students
from search_students import search_students
from delete_students import delete_student
from update_students import update_students



# Main control flag for the menu loop.
ok = True
# In-memory students list (list of dictionaries).
students = []
while ok == True:
    # Show menu and read the selected option.
    menu_students()
    opcion = validation()

    
    if opcion == 1:
            # Add a new  after validating input values.
            name, Id, age, program, state = validations()
            add_student(students, name, Id, age,program,state)

    elif opcion == 2:
            # Show inventory summary.
            show_students(students)

    elif opcion == 3:
            search_students(students)

    elif opcion == 4:
            update_students(students)

    elif opcion == 5:
            delete_student(students)

        # Exit program.
    elif opcion == 6:
            
            print("Thanks for using the program")
            ok = False

    else:
            print("Choose a valid option")

    