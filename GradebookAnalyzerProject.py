import pandas as pd 

df = pd.read_csv('grades.csv')

print('Summary statistics:\n', df[Score].describe())

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
df['Grade'] = df['Score'].apply(assign_grade)

top_students = df[df['Score'] == df['Score'].max()]
bottom_students = df[df['Score'] == df['Score'].min()]

print('Top performer(s):\n', top_students)
print('Bottom performer(s):\n', bottom_students)

print('Grade distribution:\n', df['Grade'].value_counts())
