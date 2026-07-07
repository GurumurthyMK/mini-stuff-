# Build functions to
# Add student
# Remove student
# Update marks
# Find topper
# Find average
# Count pass/fail
# Search student by name

# Initializing student DB in a list of dicts 
stud_db: list = [
    
    { "Name": "Aditya",
      "Course": "CS",
      "Roll": 100,
      "Final percentage": 89
     }

]


# Definig CLI menu 
def opr_menu(DB:list):
    
    # Defining logic for each feature 
    def add_stud():
        name = input("Enter the name : ")
        course = input("Enter the course : ")
        roll = input("Enter roll : ")
        final_percentage = input("Enter final percentage : ")

        DB.append({
            "Name": name,
            "Course": course,
            "Roll": roll,
            "Final percentage": final_percentage
        })

    def remove_stud():
        name = input("Enter student name to be removed: ")

        for i, entry in enumerate(DB):
            if entry.get("Name") == name:
                index = i
                break 
        if index is not None:
            del DB[i]
            print("Deleted entry successfully\n", DB)
        else:
            return "record not found"
        
    def display_studs():
        for item in DB:
            print(item)

         
  # routing requests     
    if  "Add" and "add" in opr:
        add_stud()
    if  "Remove" and "remove" in opr:
        remove_stud()
    if  "Display" and "display" in opr:
        add_stud()

    while True:
        opr = (input("Choose an operation from below: "
                     "\nAdd student"
                     "\nRemove student"
                     "\nUpdate marks"
                     "\nFind topper"
                     "\nFind average"
                     "\nCount pass/fail"
                     "\nSearch student by name"
                     "\nDisplay students"
                     "\n"
                ))


# 4. Updating and sorting DB after operations 

opr_menu(DB=stud_db)