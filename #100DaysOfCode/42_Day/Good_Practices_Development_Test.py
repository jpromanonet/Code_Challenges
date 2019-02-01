# Define global variables

gpr_Score_Value = 0
gpr_Answer = ''
result = ''

# Define lists and values

test_Grade_Answer = [
    '''Score : 1 | You don't have any good practices nor you do know the concept''',
    '''Score : 2 | You know at least the concept of good practices but never applied one''',
    '''Score : 3 | You're thinking on apply some basic good practices''',
    '''Score : 4 | You sometimes apply good practices''',
    '''Score : 5 | You are learning more good practices daily and thinking on how to apply them''',
    '''Score : 6 | You are applying good practices daily''',
    '''Score : 7 | You can apply good practices to another developer code.''',
    '''Score : 8 | Now, first you put on paper the idea for your development workflow around good practices''',
    '''Score : 9 | Already can make a whole project alone and share it to another developers without worry about conventions''',
    '''Score : 10 | You came a long way, and now beome a Software Architect'''
]

# Define functions

def gprTestResult(score_Value):
    if score_Value == 1:
        return test_Grade_Answer[0]
    elif score_Value == 2:
        return test_Grade_Answer[1]
    elif score_Value == 3:
        return test_Grade_Answer[2]
    elif score_Value == 4:
        return test_Grade_Answer[3]
    elif score_Value == 5:
        return test_Grade_Answer[4]
    elif score_Value == 6:
        return test_Grade_Answer[5]
    elif score_Value == 7:
        return test_Grade_Answer[6]
    elif score_Value == 8:
        return test_Grade_Answer[7]
    elif score_Value == 9:
        return test_Grade_Answer[8]
    elif score_Value == 10:
        return test_Grade_Answer[9]

# Define the questions!

# Question 1

print('Do you use source control or at least make safe local copies of your code? Y/N')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 2

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you indent as required with Tabs(not spaces)?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 3

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you make comments often?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 4

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you have a bug database and a bugtracker like MantisBT or Redmine?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 5

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you fix bugs before writing new code?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 6

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you respect the 80 characters rule?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 7

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you have a DER and your software is make in modules?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 8

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Could you apply the previous questions to another developer work?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 9

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you ask to your peers or the comunnity of your program language when you are stuck?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Question 10

print('Actual Score: ') 
print(gpr_Score_Value)
print('')

print('Do you have testers and write use cases and UML flows?')
gpr_Answer = input()

if gpr_Answer == 'y':
    gpr_Score_Value = gpr_Score_Value + 1

# Define the logic

result = gprTestResult(gpr_Score_Value)
print(result)