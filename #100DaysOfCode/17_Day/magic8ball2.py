# Calling system functions

import random

# Defining variables

answers = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# Defining program logic

print(answers[random.randint(0, len(answers) - 1)])
