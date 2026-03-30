# Delete students function 
def delete_student(students):
# Verify if the students list is not empty
    if students == []:
        print("if you want to delete in the inventory first add something")
    else:
        name_deleted = input("write the name of the student that you want to delete: ").strip().lower()
        new_students = []
        found = False
# Run the list if found student deleted the students for the list
        for item in students:
            if item["name"] == name_deleted:
                found = True
            else:
                new_students.append(item)

        if found == True:
            students.clear()
            for item in new_students:
                students.append(item)
            print("Students deleted")
        else:
            print("Students not found")