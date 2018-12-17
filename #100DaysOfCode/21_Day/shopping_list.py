# Import libraries

import pprint

# Defining values

shopping_List = []
keep_Working = 'Y'
select_Option = None
item = None

# Defining functions

def add_Item(new_Item):
    shopping_List.append(new_Item)

def remove_Item(bye_Item):
    shopping_List.remove(bye_Item)

def menu():

    print('-------MENU-------')
    print('------------------')
    print('Agregar Item_____A')
    print('Borrar Item______B')
    print('Ver Lista________V')
    print('Salir____________S')

# Defining logic & Output
while keep_Working == 'Y':

    menu()
    print('Opcion?')
    select_Option = input() # Input option

    # Output for options

    if select_Option == 'A': # Adding items to the list

        print('Input the item to add: ')
        item = input()
        add_Item(item)
        print(shopping_List)

        print('Do you wish to keep working? Y/N')
        keep_Working = input()
        if keep_Working == 'Y':
            continue
        else:
            print('Bye!')
            break

    elif select_Option == 'B':

        print('Input the item to delete: ')
        item = input()
        remove_Item(item)
        print(shopping_List)

        print('Do you wish to keep working? Y/N')
        keep_Working = input()
        if keep_Working == 'Y':
            continue
        else:
            print('Bye!')
            break

    elif select_Option == 'V':
        pprint.pprint(shopping_List)

        print('Do you wish to keep working? Y/N')
        keep_Working = input()
        if keep_Working == 'Y':
            continue
        else:
            print('Bye!')
            break

    else:
        print('Bye!')
        break  