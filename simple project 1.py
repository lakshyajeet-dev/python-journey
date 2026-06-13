# Write a program that:

# Asks the user for name, age, city, course, and CGPA
# Asks for their birth year and calculates age automatically — don't ask age directly
# Prints a neatly formatted bio like this:

# ---- Student Bio ----
# Name    : Lakshyajeet
# Age     : 21
# City    : Kota
# Course  : B.Tech
# CGPA    : 7.5
# ---------------------

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
city = input("Enter your city: ")
course = input("Enter your course: ")
cgpa = float(input("Enter your cgpa: "))
age = 2026 - birth_year
print("---- Student Bio ----")
print(f"Name  :  {name}")
print(f"Age   :  {age}")
print(f"City  :  {city}")
print(f"Course:  {course}")
print(f"CGPA  :  {cgpa}")
print("---------------------")