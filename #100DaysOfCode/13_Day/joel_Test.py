# Define global variables

joel_Score_Value = 0
joel_Answer = ''
result = ''

# Define functions

def joeltestresult(score_Value):
    if score_Value == 1:
        return 'DEFCON 1 | Cocked Pistol | Inminent Nuclear World War'
    elif score_Value == 2:
        return 'DEFCON 2 | Fast Pace | One Step to Nuclear War'
    elif score_Value == 3:
        return 'DEFCON 3 | Round House'
    elif score_Value == 4:
        return 'DEFCON 4 | Double Take'
    elif score_Value == 5:
        return 'DEFCON 5 | Fade Out'
    elif score_Value == 6:
        return 'SCORE 6 | Not defcon but stil a disaster'
    elif score_Value == 7:
        return 'SCORE 7 | Is this a team or just a bunch of newbies?'
    elif score_Value == 8:
        return 'SCORE 8 | Meh, i am not going to pay for copy-paste code from StackOverFlow'
    elif score_Value == 9:
        return 'SCORE 9 | Well, the team is getting better'
    elif score_Value == 10:
        return 'SCORE 10 | The team still has serious problems'
    elif score_Value == 11:
        return 'SCORE 11 | The team is not, a torable development team!'
    elif score_Value == 12:
        return 'SCORE 12 | You have the perfect team! CONGRATS!!!'

# Define the questions!

# Question 1

print('Do you use source control? Y/N')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 2

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Can you make a build in one step?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 3

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you make daily builds?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 4

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you have a bug database?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 5

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you fix bugs before writing new code?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 6

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you have an up-to-date schedule?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 7

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you have a spec?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 8

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do programmers have quiet working conditions?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 9

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you use the best tools money can buy?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 10

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you have testers?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 11

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do new candidates write code during their interview?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Question 12

print('Actual Joels Score: ') 
print(joel_Score_Value)
print('')

print('Do you do hallway usability testing?')
joel_Answer = input()

if joel_Answer == 'y':
    joel_Score_Value = joel_Score_Value + 1

# Define the logic

result = joeltestresult(joel_Score_Value)
print(result)