# Build functions to
# Add student
# Remove student
# Update marks
# Find topper
# Find average
# Count pass/fail
# Search student by name
# Display all

# Initializing student DB in a list of dicts
stud_db: list = [

    { "Name": "Aditya",
      "Course": "CS",
      "Roll": 100,
      "Final percentage": 89
     }

]

def operations(DB:list):

    # defining logic for each feature

    # addin student
    def add_stud():
        name = input("Enter the name : ")
        course = input("Enter the course : ")
        roll = input("Enter roll : ")
        final_percentage = int(input("Enter final percentage : "))

        DB.append({
            "Name": name,
            "Course": course,
            "Roll": roll,
            "Final percentage": final_percentage
        })
        print("Added successfully\n")

    # removing student
    def remove_stud():
        name = input("Enter student name to be removed: ")

        for i, entry in enumerate(DB):
            if entry.get("Name") == name:
                index = i
                break
                if index is not None:
                     del DB[i]
                     print("Deleted entry successfully\n")
        else:
            return "record not found"

    # updating centage
    def update_marks():
        name = input("Enter the name of student who's marks need to be updated: ")

        for item in DB:
            if item["Name"] == name:
                print("Data found, current final percentage is: ", {item["Final percentage"]})
                item["Final_percentage"] = input("Enter the updated percentage: ")
                print("Updated succesfully\n")
                break
        else:
            return "Invalid input"


    # Find topper
    def find_topper():
        topper = max(DB, key=lambda stud: stud["Final percentage"])
        if topper in DB:
            print(f"Topper: {topper["Name"]} \n Percentage: {topper["Final percentage"]}")
        return "Enter a valid input"

    # find average
    def find_avg():
        for stud in DB:
            avg = sum(stud["Final percentage"] for stud in DB) / len(DB)
            print(f"The total average is: {avg}")
        return "Enter a valid input"

    # counting pass and fail
    def p_f():
        n = 35
        Pass = sum( 1 for stud in DB if stud["Final percentage"] > n )
        fail = sum( 1 for stud in DB if stud["Final percentage"] < n )
        print(f"Number of passed students: {Pass} \n Number of failed students: {fail}")

    # find by name
    def find_name():
        name = input("Enter student name to be found: ")
        for stud in DB:
            if stud["Name"] == name:
                print(f"Data found \nName: {stud["Name"]}\n"
                        f"\nCourse: {stud["Course"]}"
                        f"\nRoll: {stud["Roll"]}"
                        f"\nFinal percent: {stud["Final percentage"]}")
            return "Not found"

    # displaying students
    def display_studs():
        for item in DB:
            print(item)



    # definig CLI menu
    while True:
        opr = (input("\n Choose an operation from below: "
                     "\nAdd student"
                     "\nRemove student"
                     "\nUpdate marks"
                     "\nFind topper"
                     "\nFind average"
                     "\nCount pass/fail"
                     "\nSearch student by name"
                     "\nDisplay students"
                     "\nExit"
                     "\n"
                )).lower()

        # routing requests
        if "add" in opr:
            add_stud()
        elif "remove" in opr:
            remove_stud()
        elif "update" in opr:
            update_marks()
        elif "find topper" in opr:
            find_topper()
        elif "find average" in opr:
            find_avg()
        elif "count" in opr:
            p_f()
        elif "search" in opr:
            find_name()
        elif "display" in opr:
            display_studs()
        elif "exit" in opr:
            break
        else:
            return "Invalid option"

operations(DB=stud_db)
