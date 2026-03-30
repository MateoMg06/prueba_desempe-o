def validation ():
    # Validate the selected menu option.
    its_ok=True

    while its_ok == True:

        
       
        try:
            menu=int(input("Write an option: "))
            if menu <=0:
                print("Write a valid number")
                its_ok=True
            elif menu == "":
                print("Write something")
                its_ok=True
            else:
                its_ok=False
            
        except ValueError:

            print("Write numbers only")
            its_ok=True
    
    return menu




def validations ():
        # Validate student name, Id, Age ,program  and state.
        name_ok = False
        while name_ok == False:
            name = input("Student name: ").strip().lower()
            try:
                float(name)
                print("Write only letters")
                name_ok = False
            except:
                if name =="":
                    print("Write something ")
                else:
                    name_ok = True
                    
        
        id_ok = False
        while id_ok == False:
            try:
                Id = int(input("students ID: "))
                if Id <= 0:
                    print("students ID cannot be negative")
                    id_ok = False
                else:
                    id_ok = True
            except:
                print("Write a number")

        age_ok = False

        while age_ok == False:
            try:
                age = int(input("Age: "))
                if age <= 0:
                    print("Age cannot be negative")
                    age_ok = False
                else:
                    age_ok = True
            except:
                print("Write a whole number")
                
        
        program_ok = False
        while program_ok == False:
            program = input("Program name: ").strip().lower()
            try:
                float(program)
                print("Write ony letters")
                name_ok = False
            except:
                if program =="":
                    print("Write something")
                else:
                    program_ok = True

        state_ok = False
        while state_ok == False:
            state = input("what is the student state? active or idle : ").strip().lower()
            if state == "active" or state == "idle":
                    state_ok = True       
           
                
            if state == "":
                    print("write something")
                    state_ok== False  
            
                
            else:
                print("write a valid state")
                state_ok == False


            
                
                

                    


                        

        return name, age, Id, state, program