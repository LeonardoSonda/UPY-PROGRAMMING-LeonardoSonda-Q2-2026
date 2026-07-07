# ==============================================================================
# Project: Classwork #10 - School Management System
# Rules: No functions, no classes, no imports, completely sequential execution.
# ==============================================================================

# REQUIRED DATA STRUCTURES
users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# LOGIN PHASE

current_user = ""
current_role = ""
current_name = ""
authenticated = False

while not authenticated:
    print("#########################################")
    print("         SCHOOL MANAGEMENT LOGIN         ")
    print("#########################################")
    # INPUT
    input_username = input("User: ")
    input_password = input("Password: ")
    
    # PROCESS
    if input_username in users:
        if users[input_username]['password'] == input_password:
            current_user = input_username
            current_role = users[input_username]['rol']
            current_name = users[input_username]['name']
            authenticated = True
        else:
            # OUTPUT
            print("\nInvalid credentials. Try again.\n")
    else:
        # OUTPUT
        print("\nInvalid credentials. Try again.\n")

# OUTPUT
print(f"Welcome!, {current_name}")


# STUDENT MODE

if current_role == "student":
    # OUTPUT
    print("              School Report              ")

    approved_set = set()
    
    # PROCESS & OUTPUT
    for subject in subjects:
        student_grade = notes[current_user][subject]
        print(f"- {subject}: {student_grade}")
        
        if student_grade >= 7.0:
            approved_set.add(subject)
            
    pending_set = set(subjects) - approved_set
    
    print("Approved Subjects (Grade >= 7.0):")

    for subject in approved_set:
        print(f"  * {subject}")
        
    print("Pending Subjects:")

    for subject in pending_set:
        print(f"  * {subject}")


# PROFESSOR MODE

elif current_role == "professor":
    keep_grading = True
    
    while keep_grading:
        # OUTPUT
        print("                Students                 ")
        
        # PROCESS & OUTPUT
        for username in users:
            if users[username]['rol'] == 'student':
                print(f"User: {username} | Student: {users[username]['name']}")
        
        # INPUT
        target_student = input("Student to grade (username): ")
        
        # PROCESS (Validation)
        while target_student not in users or users[target_student]['rol'] != 'student':
            print("Invalid student username. Please choose from the list.")
            # INPUT
            target_student = input("Student to grade (username): ")
            
        # OUTPUT
        print("                Subjects                 ")
        for subject in subjects:
            print(f"  - {subject}")
        
        # INPUT
        target_subject = input("Subject to grade: ")
        
        # PROCESS (Validation)
        while target_subject not in subjects:
            print("Invalid subject name. Please type it exactly as shown.")
            # INPUT
            target_subject = input("Subject to grade: ")
            
        # INPUT
        valid_grade = False
        new_grade_float = 0.0
        while not valid_grade:
            input_grade = input("New grade: ")
            
            # Simple numeric string check for conversion safety
            is_numeric = True
            dot_count = 0
            for char in input_grade:
                if char == '.':
                    dot_count += 1
                elif char < '0' or char > '9':
                    is_numeric = False
            
            if is_numeric and dot_count <= 1 and input_grade != '.':
                new_grade_float = float(input_grade)
                if 0.0 <= new_grade_float <= 10.0:
                    valid_grade = True
                else:
                    print("Grade must be between 0 and 10.")
            else:
                print("Invalid format. Please enter a number.")
                
        # OUTPUT
        current_grade = notes[target_student][target_subject]
        print(f"\n{target_subject}: {current_grade} ==> {new_grade_float}")
        
        # INPUT
        confirmation = input("Do you confirm (yes/no)? ")
        
        # PROCESS
        if confirmation.lower() == 'yes':
            notes[target_student][target_subject] = new_grade_float
            # OUTPUT
            print("\nGrade updated!\n")
            

            print(f"Updated Grades for {users[target_student]['name']}:")


            for subject in subjects:
                print(f"- {subject}: {notes[target_student][subject]}")

        else:
            # OUTPUT
            print("\nUpdate cancelled.\n")
            
        # INPUT
        another = input("Would you like to grade another student? (yes/no): ")
        if another.lower() != 'yes':
            keep_grading = False



# COORDINATOR MODE

elif current_role == "coordinator":
    # OUTPUT
    print("=========================================")
    print("               Professors                ")
    print("=========================================")
    for username in users:
        if users[username]['rol'] == 'professor':
            print(f"User: {username} | Professor: {users[username]['name']}")
            
    print("\n=========================================")
    print("                Students                 ")
    print("=========================================")
    for username in users:
        if users[username]['rol'] == 'student':
            print(f"User: {username} | Student: {users[username]['name']}")
            
    print("\n=======================================================================================================================")
    print("                                                       Records                                                         ")
    print("=======================================================================================================================")
    
    # Table Header Alignment formatting (Left column width 50, standard cells width 10)
    print(f"{'Subjects':<50} | {'jperez':<8} | {'dromo':<8} | {'mjuarez':<8} | {'mlopez':<8} | {'euc':<8} | {'cbalam':<8}")
    print("-" * 119)
    
    # PROCESS & OUTPUT
    for subject in subjects:
        g1 = notes['jperez'][subject]
        g2 = notes['dromo'][subject]
        g3 = notes['mjuarez'][subject]
        g4 = notes['mlopez'][subject]
        g5 = notes['euc'][subject]
        g6 = notes['cbalam'][subject]
        
        print(f"{subject:<50} | {g1:<8.1f} | {g2:<8.1f} | {g3:<8.1f} | {g4:<8.1f} | {g5:<8.1f} | {g6:<8.1f}")
    print("=======================================================================================================================\n")