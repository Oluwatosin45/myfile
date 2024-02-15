

# Program to display grade of student

score = int(input('Enter score: '))

if score >= 70:
    print('A')
elif score >= 60 and score < 70:
    print('B')
elif score >= 50 and score < 60:
    print('C')
elif score >=45 and score <50:
    print('D')
elif score >= 40 and score < 45:
    print('E')
else:
    print('F')
