# Search student from the list students
def search_students(students):
    if students == []:
        print("if you want to search a students first add something")
    else:
        name_searched = input("write the name of the students that you want to search: ").strip().lower()
        found = False
# Run the list a validated if student name is in the list
        for item in students:
            if item["name"] == name_searched:
                print(f"name: {item['name']} | Id: {item['Id']} | age: {item['age']},| state: {item['state']}")
                found = True

        if found == False:
            print("Student not found")