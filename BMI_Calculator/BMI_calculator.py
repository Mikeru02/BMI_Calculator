print("Welcome to BMI Calculator")
print("Please Enter the Following")
first_name = input("First Name: ")
print(f"Welcome! {first_name}")

print("Select Weight Measurement")
print("lbs , kg")

while True:
  weight_measure = input('Measurement: ')
  if weight_measure == 'lbs':
    while True:
      weight = input("Your Weight: ")
      if weight.isdigit() == True:
        lbs_kg = int(weight) * 0.454
        final_weight = round(lbs_kg, 0)
        print(f'{final_weight} kg')
        break
      else:
        print('Invalid Entry')
        continue
    break
  elif weight_measure == 'kg':
    while True:
      weight = input("Your Weight: ")
      if weight.isdigit() == True:
        kg = int(weight) * 1
        final_weight = round(kg, 0)
        print(f'{final_weight} kg')
        break
      else:
        print('Invalid Entry')
        continue
    break
  else:
    print('Invalid Entry')
    continue

print("Select Measurement")
print("ft , inch , cm , m , m2")

while True:
  height_measure = input('Measurement: ')
  if height_measure == 'ft':
    while True:
      h_ft = input('Your Height(ft): ')
      h_inch = input('Your Height(inch): ')
      if h_ft.isdigit() and h_inch.isdigit() == True:
        ft_inch = int(h_ft) * 12 + int(h_inch)
        inch_cm = ft_inch * 2.54
        cm_m = round(inch_cm, 0) / 100
        m_m2 = cm_m * cm_m
        final_height = round(m_m2, 2)
        print(f'{final_height} m^2')
        break
      else:
        print('Invalid Entry')
        continue
    break
  elif height_measure == 'inch':
    while True:
      height = input('Your Height: ')
      if height.isdigit() == True:
        inch_cm = int(height) * 2.54
        cm_m = round(inch_cm, 0) / 100
        m_m2 = cm_m * cm_m
        final_height = round(m_m2, 2)
        print(f'{final_height} m^2')
        break
      else:
        print('Invalid Entry')
        continue
    break
  elif height_measure == 'cm':
    while True:
      height = input('Your Height: ')
      if height.isdigit() == True:
        cm_m = round(int(height), 0) / 100
        m_m2 = cm_m * cm_m
        final_height = round(m_m2, 2)
        print(f'{final_height} m^2')
        break
      else:
        print('Invalid Entry')
        continue
    break
  elif height_measure == 'm':
    while True:
      height = input('Your Height: ')
      if height.isdigit() == True:
        m_m2 = int(height) * int(height)
        final_height = round(m_m2, 2)
        print(f'{final_height} m^2')
        break
      else:
        print('Invalid Entry')
        continue
    break
  elif height_measure == 'm2':
    while True:
      height = input('Your Height: ')
      if height.isdigit() == True:
        m2 = int(height) * 1
        final_height = round(m2, 2)
        print(f'{final_height} m^2')
        break
      else:
        print('Invalid Entry')
        continue
    break
  else:
    print('Invalid Entry')
    continue

BMI = final_weight / final_height
print(round(BMI, 2))
if BMI <= 18.5:
  print(f"{first_name} you are 'Underweight'")
elif BMI <= 24.9:
  print(f"{first_name} you are 'Normal Weight'")
elif BMI <= 29.9:
  print(f"{first_name} you are 'Overweight'")
elif BMI <= 34.9:
  print(f"{first_name} you are 'Class 1 Obese'")
elif BMI <= 39.9:
  print(f"{first_name} you are 'Class 2 Obese'")
else:
  print(f"{first_name} you are 'Class 3 Obese'")
