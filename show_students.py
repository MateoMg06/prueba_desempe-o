def show_students(base):
    # Show each students in a clear line format.
    print("SUMMARY")

    if base == []:
        print("empty")
        
    else:
        for item in base:
            name = item["name"]
            Id = item["Id"]
            age = item["age"]
            program = item["program"]
            state = item["state"]
            print(f"name: {name} | ID: {Id} | age: {age},| program: {program} | state: {state}")
