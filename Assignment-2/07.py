'''
A person wants to know his Body Mass Index (BMI). He knows his weight in pounds 
and height in inches. The evaluator knows the formula for calculating BMI using the formula,
BMI = (weight in kilograms) / (height in m * height in m)
Help the person in finding his BMI by writing a program for him. 
(Use the conversion formulae: 1 pound =0.4536 kilograms, 1 inch = 2.54 cms)
'''

weight = float(input('Enter weight in pounds : '))
height = float(input('Enter height in inches : '))

weight_kg = weight * 0.4536
height_m = (height * 2.54) / 100

bmi = weight_kg / (height_m * height_m)

print('BMI of person : ' , format(bmi,".2f"))