class personalinfo:
  def __init__(self, name1, age, height, weight, is_student, is_employed, favorite_number):
    self.name = name1
    self.age = age
    self.height = height
    self.weight = weight
    self.is_student = is_student
    self.is_employed = is_employed
    self.favorite_number = favorite_number
    self.is_good_looking = True

  def calculate_bmi(self):
    self.age_in_days = self.age * 365
    self.height_in_inches = self.height * 100 / 2.54  # convert meters to cm to inches
    self.bmi = self.weight / self.height ** 2
    self.is_adult = self.age >= 18

    if self.bmi < 18.5:
        self.bmi_indication = "Underweight"
    elif self.bmi < 24.9:
        self.bmi_indication = "Normal weight"
    elif self.bmi < 29.9:
        self.bmi_indication = "Overweight"
    else:
        self.bmi_indication = "Obese"

    # Status information
    self.status = "Student" if self.is_student else "Professional"  
  
  def print_dummy():
    print ("dummy")


  def print(self):
    profile = f"""
    🧑 PERSONAL PROFILE
    ==================
    Name: {self.name}
    Age: {self.age} years ({self.age_in_days:,} days old!)
    Height: {self.height} Mtrs ({self.height_in_inches:.1f} inches)
    Weight: {self.weight} kg
    BMI: {self.bmi:.1f}
    BMI Indication: {self.bmi_indication}
    Status: {self.status}
    Adult: {"Yes" if self.is_adult else "No"}
    Lucky Number: {self.favorite_number}
    Good looking: {self.is_good_looking}
    """

    print(profile)

vamshi = personalinfo("Vamshi Krishna", 22, 1.68, 65, True, False, "Blue")
vamshi.calculate_bmi()
vamshi.print()
personalinfo.print_dummy()