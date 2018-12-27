# Defining global values

input_Text = None
len_Text = None

# Defining functions

def textLen(text):
    len_Text = len(text)
    print('Your text lenght is: ' + str(len_Text) + ' characters')

# Script logic

print('Write something, please')
input_Text = input() # Introducing some text

textLen(input_Text) # Counting the text lenght
