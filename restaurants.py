# Bianca Beltran
# restaurants.py

vegetarian = False
vegan = False
gluten_free = False
response = input('Is anyone in your party a vegetarian?: ')
if response == 'yes':
    vegetarian = True
response = input('Is anyone in your party a vegan?: ')
if response == 'yes':
    vegan = True
response = input('Is anyone in your party gluten-free?: ')
if response == 'yes':
    gluten_free = True
print('Here are your restaurant choices: ')
if vegetarian == False and gluten_free == False:
    print('Joes Gourmet Burgers')
if vegan == False and gluten_free == False:
    print('Mamas Fine Italian')
if vegan == False:
    print('Main Street Pizza')
    print('Chefs Kitchen')

    
    
    



