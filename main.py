# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# My solution:
m = float(height)
kg = float(weight)
bmi = kg / m**2
print(int(bmi))

# Teacher Solutions:
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)




