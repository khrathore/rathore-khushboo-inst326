'''
Regular expressions:
    - Determining if a particular string or substring matches another string
    - Can match things that repeat, but can't recognize nested structures (check parenthesis nesting or HTML matching tags)
    -  Escape sequences: Tell python to insert something special into a string (\n, \t, \\, etc)
    - Raw strings: Python ignores escape sequences in these by putting an r before opening quote r"string", can combine w fstring fr"string"
    - regex101.com: Shows a bunch of how to use regular expressions
    Building blocks:
        - Will match whatever it finds (r"the -> other, their, the, etc.)
        - Can use the pipe character (|) to match two diff things, not limited to whole words
        - Can use groups, which allows for making subexpressions
            - Capturing group: (subexpression) (red|orange|yellow) -> will get a match and then the group term which matched
            - Named capturing group (?P<NAME>subexpression) (?P<color>red|orange|yellow) -> stores with a group label
            - Non-capturing group (?:subexpression) (?:red|orange}yellow) -> won't store information in any special form
        - Then you can add quantifiers into the mix, telling it to do things a certain amount of times
            - optionality - ?, matches 0 or 1 of the thing r"e(?:a|e|i|o|u)?r"gm -> er, ear, eor, etc.
            - kleene star: *, matches for zero or more r"c(?:a|e|i|o|u|y)*"gm -> c or ca, ce, etc.
            - kleene plus: + matches one or more
            - {N}: specific number of instances (a|e|i|o|u){3}
            - {M,N}: between a certain number of instances
            - "Lazy" quantifiers ??, *?, +? (etc) will match as few as possible
    Character classes:
        - \d: decimal digit (0-9)
        - \w (alphanumberic or word characters)
        - \s (space character, including tab, newline, etc)
        - the "anything but" of those is \D, \W, \S
        - .: grab anything
        - Defining your own character classes:
            - By inclusion [], [aeiouAEIOU], [A-Za-Z], can include predefined classes
            - By exlucsion [^], [^ao]


'''