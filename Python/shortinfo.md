## Python

-   In this class, Python 3.6 will be used. For those unfamiliar, Python is an interpreted language that will be used in the context of this class to generate dynamic websites and web applications.
-   Some basic Python syntax:
    -   Print a string to the screen:
        
        ```
          print("Hello, world!")
        
        ```
        
    -   Print a format string (variable names enclosed with  `{}`  will be replaced by variable values)
        
        ```
          print(f"Hello, {name}!")
        
        ```
        
    -   Set variable  `name`  to the user input returned by  `input()`
        
        ```
          name = input()
        
        ```
        
    -   Conditional statement:
        
        ```
          if x > 0:
              print("x is positive")
          elif x < 0:
              print("x is negative")
          else:
              print("x is zero")
        
        ```
        
        -   `elif`  and  `else`  blocks are optional.
        -   Note that indentation in Python is not stylistic, but rather is used to demarcate blocks of code. In this example, the Python interpreter knows where the conditional  `if`  block ends and the  `elif`  block begins because of the changes in indentation.

### Data Types

-   `int`  : integer value
-   `float`  : floating point value
-   `str`  : text string
-   `bool`  : boolean value (`True`  or  `False`)
-   `None`  : empty value
-   Note that Python is a weakly typed language.

### Sequences

-   Strings:
    
    ```
      name = "Alice"
      print(name[0])
    
    ```
    
    -   Strings are justs sequence of characters, and can be indexed as such.
-   Tuples:
    
    ```
      coordinates = (10.0, 20.0)
      print(coordinates[1])
    
    ```
    
    -   Tuples are immutable collections of values under a single name, which can be indexed positionally.
-   Lists:
    
    ```
      names = ["Alice", "Bob", "Charlie"]
      print(names[2])
    
    ```
    
    -   Lists are mutable collections of values under a single name, which can be indexed positionally.
    -   Indexing out of range raises a Python ‘exception’. In this case, an  `IndexError`, because there is no fourth value in  `names`  for Python to return.
-   Note that any sequence in Python can contain any number of data types.
    
-   Sets:
    
    ```
      s = set()
      s.add(1)
      s.add(3)
      s.add(5)
    
    ```
    
    -   Sets are unordered collection of unique items. Because they are unordered, they cannot be indexed.
    -   `s`  is a  `set`, an unordered collection of unique items
-   Dictionaries:
    
    ```
      ages = {"Alice": 22, "Bob": 27}
      print(ages["Alice"])
      ages["Alice"] += 1
    
    ```
    
    -   Dictionaries (or dicts) are like lists, except that they are unordered and their  `value`s are indexed by  `keys`.
    -   The  `+=`  operator increments the left-hand side by the right-hand side.

### Loops

```
for i in range(5):
    print(i)

```

-   For-loops iterate over their bodies a limited number of times. In this case, the number of iterations is set by  `range(5)`.
-   `range(5)`  returns the sequence of numbers starting at 0 through 4. Each value is passed to  `i`  once, resulting in the loop running a total of 5 times.  `i`  is normally referred to as an iterator variable.

```
for name in names:
    print(name)

```

-   This for-loop iterates over  `names`, which is a list. Every value in the list is assigned, in order, to the iterator  `name`  once.

### Functions

-   Python has built-in functions, such as  `print()`  and  `input()`, but Python also allows for the creation of user-defined functions
    
    ```
      def square(x):
          return x * x
    
    ```
    
    -   This is a function called  `square`, which takes a single argument  `x`, and returns the value  `x * x`.
    -   Like loops, the body of a function must be indented.
        
        ```
          for i in range(10):
          print("{} squared is {}".format(i, square(i)))
        
        ```
        
        -   This loop, which prints out the results of  `square`  with a range of arguments, using an older method for format strings.
-   Trying to call a function that hasn’t been defined will raise a  `NameError`  exception.

### Modules

-   Modules are separate  `.py`  files of code, often written by others, used in a new file without rewriting all the old code again. Using modules allows, for example, the use of functions across a program larger than a single file.
-   Assuming the  `square`  function in the earlier example was saved in  `functions.py`, adding this line atop a new module will allow for the use of  `square`  there as well.
    
    ```
      from functions import square
    
    ```
    
-   If, for example,  `functions.py`  also included the example loop demonstration of the  `square`  function, that loop would be executed every time  `square`  was imported from  `functions`, because the Python interpreter reads through the entire  `functions.py`  file. To remedy this, code that should only run when their containing file is run directly should be encapsulated in a function, called, for example,  `main`. After, the following should be appended:
    
    ```
      if __name__ == "__main__":
          main()
    
    ```
    
    This should be interpreted as saying ‘if this file is currently being run’, execute  `main`.
    

### Classes

-   A Python  `class`  can be thought of as a way to define a new, custom Python data type, somewhat analagous to defining a custom function.
-   This creates a new  `class`  called  `Point`:
    
    ```
      class Point:
          def __init__(self, x, y):
              self.x = x
              self.y = y
    
    ```
    
    -   The  `__init__`  function is a special function that defines the information needed when a new  `Point`  is created.  `self`  is always required, which refers to the  `Point`  being created, while  `x`  and  `y`  are its coordinates.
    -   `self.x`  and  `self.y`  actually do the work of creating  `x`  and  `y`  attributes for the  `Point`  and assigning the m the values passed to  `__init__`.
    -   By convention,  `class`  names tend to start with a capital letter.
-   This instantiates a new  `Point`  with  `x = 3`  and  `y = 5`:
    
    ```
      p = Point(3, 5)
    
    ```
    
    -   When this line is run, the  `__init__`  function of the  `Point`  class is automatically run.
-   To access the  `x`  attribute of  `p`, use dot notation:
    
    ```
      print(p.x)
    
    ```