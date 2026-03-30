def add_student(students,name, age, Id,state,program):
            # Build and save a base dictionary in the students list.
            base = {
                "name": name,
                "Id": Id,
                "age": age,
                "program": program,
                "state": state
                  
            }
            students.append(base)
            print("Student added")
            return base,students


