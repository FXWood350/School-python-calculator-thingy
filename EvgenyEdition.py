import math

# flow

choices = {
    'Arithmetic': {
        'add': lambda x, y: x + y,  # same as def add(x, y): return x + y
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else float('nan')
    },
    # try filling the following values yourself:

    'exponential': {
        'exponent':lambda x, y: x ** y,
        'root': lambda x : math.sqrt(x)
    },
    'trigonometric': {
        'cosine': lambda x : math.cos(x),
        'sine': lambda x : math.sin(x),
        'tangent': lambda x: math.tan(x)
    },
    'inverse trigonometric': {
        'invcosine': lambda x: math.acos(x),
        'invsine': lambda x: math.asin(x),
        'invtangent': lambda x: math.atan(x)
    }
}

# test your code, sometimes a subtle change can break everything:
assert choices['Arithmetic']['add'](1, 2) == 3
assert choices['Arithmetic']['subtract'](5, 4) == 1
assert choices['Arithmetic']['multiply'](3, 3) == 9
assert choices['Arithmetic']['divide'](15, 5) == 3
assert math.isnan(choices['Arithmetic']['divide'](5, 0))

# user input

# let's create a mapping between the choice number and the dictionary key.
# although our dictionary lays out possible choices nicely when we instantiate it,
# there is no guarantee that key ordering will remain the same:

# https://stackoverflow.com/questions/5629023/key-order-in-python-dictionaries/5629050


 # this is called a dict comprehension, google it :)
operation_map = {i: op for i, op in enumerate(choices.keys())}

print('Select operation type: ')

# this is called a list comprehension, also goole it :) 
[print(f'{key}: {value}') for key, value in operation_map.items()]

# what will happen if the user types in a character instead of a number?
choice = int(input('? > '))

# notice how we are going to terminate the app now, that the choice is incorrect
# instead of creating multple if statements inside other if statements

if choice not in operation_map:
    raise ValueError('Not a valid choice for an operation.')

operation_name = operation_map[choice]

print('')

# another dict comprehension, exactly the same operation
# but on a different dictionary (i.e. argument)
# may be wrap it in a function?

function_map = {
        i: fu
        for i, fu in enumerate(choices[operation_name])
    }

# let's add a tab here for esthetic purposes
print('\tSelect function: ') 
[print(f'\t{key}: {value}') for key, value in function_map.items()]

# we can reuse the choice variable, since we do not need its 
# value any longer

choice = int(input('? > '))

if choice not in function_map:
    raise ValueError('Not a valid choice for a function.')

function_name = function_map[choice]

# let's copy the link to the function into a separate variable
# we can do this, as all python functions are objects too
func = choices[operation_name][function_name]


print('')
print(f'{operation_name} > {function_name}')

# we are going to assume that the function takes two arguments

arg1 = float(input('    argument 1 > '))
arg2 = float(input('    argument 2 > '))

# ready to execute
result = func(arg1, arg2)

print('')
print(f'result: {result}')
