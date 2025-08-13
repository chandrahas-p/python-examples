# Step 1: Personal information variables
name = "Binod"
age = 25
height = 1.68  # meters
weight = 80    # kg
is_student = True
is_employed = False
favorite_number = 8
age_in_days = age * 365

bmi = weight / height ** 2
is_adult = age >= 18

if bmi < 18.5:
    bmi_indication = "Underweight"
elif bmi < 24.9:
    bmi_indication = "Normal weight"
elif bmi < 29.9:
    bmi_indication = "Overweight"
else:
    bmi_indication = "Obese"

# Status information
status = "Student" if is_student else "Professional"

# Step 3: Create formatted profile

profile = f"""
🧑 PERSONAL PROFILE
==================
Name: {name}
Age: {age} years ({age_in_days:,} days old!)
Height: {height} Mtrs 
Weight: {weight} kg
BMI: {bmi:.2f}
BMI Indication: {bmi_indication}
Status: {status}
Adult: {"Yes" if is_adult else "No"}
Lucky Number: {favorite_number}
"""

print(profile)