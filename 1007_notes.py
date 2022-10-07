'''10/07 - Notes
    Operator: less than (<)
    Understand how it works on different values.
    Tuples: (0, 100, 5000) < (1, 2, 3) b.c. 0 < 1
        Compares on an elements by element basis
        (1, 2, 1) < (1, 2, 3) because 1 < 3
        (1, 2, 3) < (1, 2, 3, -2) because there are less values in the first sequence
    Strings: cat < dog because c < d
    cat > cab, cat < catalog, Cat < cat, eclair < Éclair
    Every letter has a code point/number that uniquely identifies it (utf).
    Capital letters are earlier than lowercase, special characters are 
    greater than normal letters.
    Find the specific code point for letter using ord(letter)
'''
print(ord("a"))
print(ord("A"))
'''
    There exists a unicode standards list to look everything up
    To print from unicode to letter, \ u(number)
'''
print("\u0058")

'''
    Using less than, you can compare that same types. Can't do 3 < "c"
    You can however, do 3 < 2.1 and 3 < ord("c")
    You can't compare things to None. Can't do 3 < None
    You can do (1, "x", True) < (7, "y", False) since the elements match
    int to int, string to string, boolean to boolean
    Less than can help in comparison, and can be used to sort sequences
    Behind the scenes of a sort, the less than is being used
    
'''
'''
    Two commands that can be used to sort:
        sorted:
            Independent function, with syntax sorted(iterable)
            Returns a new
            Can sort backwards using reverse = True
        list.sort:
            method of the list class, listed.sort()
            only for lists and sorts them in the same list
            however, list.sort returns None. So don't do list = list.sort
            Can sort backwards using reverse = True
'''

lst = [7, -8, -9, 23, 1, -29, 17, -31]
sort_lst = sorted(lst)
lst.sort()
print(lst)
print(sort_lst)
print(sorted("yikes!"))
''' Iterates through the keys in the dictionary '''
print(sorted({"UMD": 76, "Virginia Tech": 2, "Penn State": -3, "Duke": 0}))
lst.sort(reverse = True)
print(lst)

''' 
    If you want to sort things a different way, you can do that!
    Use key to pass a function and sort it by the result of that function
    You DO NOT call the function
    You can't use anything as a key function. It must be able to take one
    argument and return one value.
'''
colleges = {"UMD": 76, "Virginia Tech": 2, "Penn State": -3, "Duke": 0}
print(sorted(colleges, reverse=True, key=colleges.get))
print(sorted(colleges, key=len))

lst.sort(key=abs)
print(lst)

def modulo_three(value):
    return value % 3

lst.sort(key=modulo_three)
print(lst)

def weird_stuff(value):
    return(value % 3, -value)

lst.sort(key=weird_stuff)
print(lst)

'''
    Syntax of lambda expressions
    lambda PARAM, PARAM..., PARAM: EXPR
    You don't need to use these all the time, especially if the
    function already exists.
'''

lambda value: value % 3
lst.sort(key= lambda v: v % 3)
print(lst)

''' Lambda expression that takes a string and eval to all of the string but 
    w/o the first character'''
print(sorted(["wolf", "cow", "capybara", "chicken"], key = lambda s: s[1:]))

''' Lambda expression that takes a list and returns the list in reverse order'''
stuff = [["INST126", "B"], ["INST314", "C"], ["INST326", "A"], ["INST201", "A"]]
print(sorted(stuff, key=lambda l: l[::-1]))
