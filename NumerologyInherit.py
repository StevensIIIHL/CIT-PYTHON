###Harold Stevens
###Code Classes and Numerology with Inheritance
###11/30/2024

# Use NumerologyInherit.py

from NumerologyLifePathDetails import NumerologyLifePathDetails
import re

def validate_date(date):
    # Validate date format (mm-dd-yyyy or mm/dd/yyyy)
    pattern = r'^(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](19|20)\d\d$'
    return bool(re.match(pattern, date))

def validate_name(name):
    # Validate that name is not empty
    return bool(name.strip())

def main():
    # Prompt for user input
    while True:
        name = input("Enter your full name: ")
        if validate_name(name):
            break
        print("Name cannot be empty. Please try again.")

    while True:
        birthdate = input("Enter your birthdate (mm-dd-yyyy or mm/dd/yyyy): ")
        if validate_date(birthdate):
            break
        print("Invalid date format. Please try again.")

    # Create NumerologyLifePathDetails object
    numerology = NumerologyLifePathDetails(name, birthdate)

    # Output results using properties
    print(f"\nNumerology Reading for {numerology.Name}")
    print(f"Birthdate: {numerology.Birthdate}")
    print(f"Attitude Number: {numerology.Attitude}")
    print(f"Birthday Number: {numerology.BirthDay}")
    print(f"Life Path Number: {numerology.LifePath}")
    print(f"Personality Number: {numerology.Personality}")
    print(f"Power Name Number: {numerology.PowerName}")
    print(f"Soul Number: {numerology.Soul}")
    print(f"Life Path Description: {numerology.LifePathDescription}")

if __name__ == "__main__":
    main()
