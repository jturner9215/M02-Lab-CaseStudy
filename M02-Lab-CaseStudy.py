#Jessica Turner
#M02-Lab-CaseStudy.py
#program to take student information and determine whether they make dean's list, honor roll, or neither, based on gpa

lastName = ""
firstName = ""
gpa = 0.0


while (lastName != "ZZZ"):
    lastName = input("\nEnter the student's last name, or ZZZ to exit\n")
    
    if (lastName != "ZZZ"):
        firstName = input("\nEnter the student's first name.\n")

        gpa = input("\nEnter the student's GPA.\n")

        if (float(gpa) >= 3.25):
            print("\n" + firstName + " " + lastName + " has made the Honor Roll.")

            if (float(gpa) >= 3.5):
                print("\n" + firstName + " " + lastName + " has made the Dean's List.")

        else:
            print("\nThe student did not make the Honor Roll or Dean's List.")