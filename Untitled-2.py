#Q.no.1

items = [3, 5, 7, 9, 11, 13]
removed_item = items.pop(4)
items.insert(1, removed_item)
items.append(removed_item)
print(items)




#Q,no,2

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
common = first_set.intersection(second_set)
print("Intersection:", common)

first_set = first_set - common
print("Updated first_set:", first_set)



#Q.no.3

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("first_set is subset of second_set")
    first_set.clear()

elif first_set.issuperset(second_set):
    print("first_set is superset of second_set")
    second_set.clear()

print("first_set:", first_set)
print("second_set:", second_set)




#Q.no.4
month = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}

value_list = list(month.values())
unique_values = list(set(value_list))
print(unique_values)




#Q.no.5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_numbers = list(set(sample_list))
number_tuple = tuple(unique_numbers)

print("Tuple:", number_tuple)
print("Minimum:", min(number_tuple))
print("Maximum:", max(number_tuple))




#Q.no.6
club_a = {"ram", "hari", "shyam"}
club_b = {"ram", "gita", "hari"}

common_members = club_a.intersection(club_b)

if common_members:
    print("following members exist in both groups:")
    print(common_members)
else:
    print("no overlapping members found between groups")


    #Q.no.7
required_tasks = {"email", "report", "meeting"}
completed_tasks = {"email", "report"}

if required_tasks.issubset(completed_tasks):
    print("All tasks done")
else:
    print("some tasks pending")


#Q,no.8
students = {
    "Ram": "ram@gmail.com",
    "Hari": "hari@gmail.com",
    "Sita": "sita@gmail.com"
}


name = input("Enter student name: ")


if name in students:
    print("Email:", students[name])
else:
    print("Contact not found")



    #Q.no.9
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}


remaining = shopping_list - bought


if remaining:
    print("Items still to buy:", remaining)
else:
    print("Shopping complete")


    #Q.no.10
class_list = ["ram", "sita", "laxman"]

new_student = input("Enter student name: ")


if new_student.lower() not in class_list:
    class_list.append(new_student.lower())
    print("Student added successfully")
else:
    print("Student already present")

print(class_list)


#Q.no.11
votes = ["Blue", "Red", "Blue", "Green", "Blue"]

blue_count = votes.count("Blue")

print("Blue votes:", blue_count)


if blue_count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")



    #Q.no.12
grades = {"Ram": 92, "Sita": 88}
student_name = input("Enter student name: ")

if student_name in grades:
    print("Grade:", grades[student_name])
else:
    print("Grade not available")

#q.no.13
applicant = {
    "name": "Priya",
    "skills": ["Java", "SQL"],
    "experience_years": 1
}

required_skills = {"Python", "Java"}
if (
    set(applicant["skills"]).intersection(required_skills)
    and applicant["experience_years"] >= 2
):
    print("Priya qualifies")
else:
    print("Priya does not qualify")


#Q.no.14
banned_items = {"scissors", "knife", "lighter"}


weight = float(input("Enter baggage weight: "))
item = input("Enter item name: ").lower()

if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")


#Q.no.15
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)



#Q.no.16
ram_items = {"apple", "milk", "bread"}
laxman_items = {"eggs", "juice", "rice"}

common_items = ram_items.intersection(laxman_items)

if len(common_items) == 0:
    print("They picked completely different items")
else:
    print("They have some common items")
    print("Common items:", common_items)
