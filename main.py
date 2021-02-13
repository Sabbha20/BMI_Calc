weight = int(input('Enter your weight in kgs: '))
height = int(input('Enter your height in cms: '))

bmi = weight/((height/100)**2)

print('Your BMI: '+str(int(bmi)))