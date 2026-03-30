# Update the list function
def update_students(students):
    # Verify if the list students is empty
    if students == []:
        print("if you want to update a student first add something")
    else:
        name_updated = input("write name of the students ").strip().lower()
        found = False
        updated = False
# Run the list student if this student is found ask for the updates you want to do
        for item in students:
            if item["name"] == name_updated and updated == False:
                found = True

                new_state_text = input("write new state of student (or press enter to keep): ").strip()
                new_program_text = input("write new program of student (or press enter to keep): ").strip()

                if new_state_text != "":
                    try:
                        item["state"] = new_state_text
                    
                    except ValueError:
                        
                        print("write a valid state (active or idle)")
                    
# validate if the new updates no are empty

                if new_program_text != "":
                    try:

                            item["program"] = new_program_text
                    
                    except ValueError:
                        
                        print("write a valid program")    
                        
                print("student updated")
                updated = True

        if found == False:
            print("student not found")