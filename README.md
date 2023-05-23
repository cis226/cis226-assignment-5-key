# Assignment 1 - Review of Python Basic Concepts and Introduction to Git

## Author



## Description

Create a Python console program to work with a `.CSV` beverage list. The program should continually run until the user decides to exit (entering a certain character on the keyboard). The program should allow the following functionality:

1. Display a menu for the user to interact with. Re-display the menu where appropriate. Don't assume the user will know what to do next.
2. Allow the user to populate the beverage collection from the provided CSV file. They should only be able to load the file once. They should be able to load the file from its current location (without moving it).
3. Allow the user to print the entire list of beverages in the beverage collection.
4. Allow the user to search for a beverage by the beverage id, and print out the details of the beverage if found. Error message if not. (Linear search is fine)
5. Allow the user to add a new beverage to the beverage collection. Ensure that the id is unique and can not be duplicated when adding a new beverage item.

Here is a Sample Menu:
  1. Load File
  2. Print List
  3. Search List
  4. Add New Beverage
  5. Exit

The program should consist of 5 files / modules to house the classes that you need to make. Details about which file / module a particular class should belong in is detailed below for each class. However, at a high level, the files / modules that you need are:
* main.py
* program.py
* beverage.py
* user_interface.py
* utils.py

**NOTE:** The `main.py` file should not be altered at all. It already contains all the code needed to get the `main` method in the `program.py` file running. You should treat the `main` method in the `program.py` file as your entry point for this assignment.

### Classes
#### Beverage

Create a class called `Beverage` in the `beverage.py` file.
The `id`, `name`, and `pack` should be `strings`, `price` should be a `decimal`, and `active` should be a `bool`.
This class should have the following variables, constructors, methods, etc.
* Variables: id, name, pack, price, active
* Constructors: 5 parameter constructor (not including self)
* Public Methods: `__str__` magic method - Used to convert an instance of Beverage to a String containing all the properties of the beverage in a readable format.
* Private Methods: Your choice

#### BeverageCollection

Create a class called `BeverageCollection` in the `beverage.py` file.
The purpose of this class is to act as a 'wrapper' class for the Python List. This means that it should contain a private List to hold all of the instances of Beverage, and provide public methods to interact with the Python List. EX: `add`, `search`, and the magic `__str__` method. Rather than the rest of your assignment interacting with a Python List directly, it will call methods on this class, who's sole purpose, will be to interact with the Python List.

The magic `__str__` method for this class will be used to convert the entire collection to a string. This means that it will need to iterate over all of the Beverages in the underlying Python List and convert each one to a string that gets concatenated to a string for the whole collection that can then be returned for displaying in the console.

If you have questions about this class, ask.

This class should have the following variables, constructors, methods, etc.
* Variables: __beverages (List for Beverage instances)
* Constructors: Your choice
* Public Methods: `add`, `search`, magic `__str__` method
* Private Methods: Your choice

#### UserInterface

Create a class called `UserInterface` in the `user_interface.py` file. This class should be implemented however you see fit. It should handle all of the Screen input and output for the program. This includes any errors that occur due to exceptions being raised.
There is a good chance that you will want a more sophisticated UI with more methods than what you saw in the in-class. The in-class version was VERY minimalistic. Your assignment UI class should have more output methods that can do more work. EX: `print_header()`, `get_beverage_id()`, `print_list()`, etc.

This class should have the following variables, constructors, methods, etc.
* Variables: Your choice
* Constructors: Your choice
* Public Methods: Your choice
* Private Methods: Your choice

#### CSVProcessor

Create a class called `CSVProcessor` in the `utils.py` file. This class should be in charge of reading in a CSV file and adding records to the `BeverageCollection`. It may also want to handle ensuring the CSV can only be read in once.

**NOTE:** With the in-class, we send a raw List to the CSVProcessor class so that entries can be added to it. In the assignment, you should't use the List directly. We have a class for that. It is called `BeverageCollection`. Is it possible to send an instance of `BeverageCollection` to `CSVProcessor` in place of a raw List?

This class should have the following variables, constructors, methods, etc.
* Variables: Your choice
* Constructors: Your choice
* Public Methods: Your choice
* Private Methods: Your choice

### Documentation

Documentation should include the following for this, and all future assignments:
* Comments at the top of each file that you add source code to:
  * Your Name
  * Class
  * Date
* A docstring comment for each module describing what it does. You should be using the triple quote (""") method for the docstring.
* A docstring comment for each class describing what it does. You should be using the triple quote (""") method for the docstring.
* A docstring comment for each method describing what it does. You should be using the triple quote (""") method for the docstring.
* Comments in the rest of the code where it isn't obvious what is going on. These should be above the line comments as that will help ensure that you keep your code narrow.

### Requirements

Solution Requirements:

* 5 files / modules (`main.py`, `program.py`, `beverage.py`, `user_interface.py`, `utils.py`)
* 4 classes (`Beverage`, `BeverageCollection`, `CSVProcessor`, `UserInterface`)
* A `while` loop and a `for` loop
* A control structure (`if`/`elif`/`else` statement)
* A `List` [contents will contain instances of `Beverage`]
* At least one `method` / `function`.

Things you do ***NOT*** need to worry about:

* Save the data from the BeverageCollection back to the CSV file
* Update or Delete existing entries

### Notes
Even though you are free to write this however you would like within the constraints laid out above in the requirements, try to follow the single responsibility principle. I would suggest that you should attempt to make the `UserInterface` handle the UI, the `Beverage` and `BeverageCollection` handle representing the data, `CSVProcessor` handle obtaining the data from the file, and the `Program` handle orchestrating all of it.

Try to send any dependencies (instances of classes needed inside other classes) into a class via either a constructor, or a method rather than creating a new one inside the class. Creating multiple instances can lead to weird inconsistencies. Better to have one single instance that gets passed where it is needed. If possible make all of the new instances in `Program`'s `main` method. This is less of a concern for the classes that are obviously related. It is fine for `BeverageCollection` to create a new `Beverage` instance since they are clearly related. The goal is to future proof the program. Think of "what if" cases such as the following:
* What if we wanted to change out the User Interface with a different one? How much work would need to be done to fix it?
* What if instead of reading from a CSV file we wanted to start reading from a database? How much work would need to be done to fix it?

### Suggestions / Hints

* How the user enters the information is your choice (i.e., one at a time, all at once, etc.). However, you should strive to make it user friendly.
* You might need multiple loops, methods, control structures – just depends on your design. However, you must have a least one of each.
* Remember to handle the case when the user has entered no information. You can print a simple message (i.e., “No data entered” or something else). It just needs to be obvious to the user that something has happened.
* Remember to handle (gracefully) cases where the user enters something incorrectly. Your program should not abruptly crash from bad user input.
* Remember to use the appropriate access modifiers for scope. It is highly unlikely that everything should be public. Only the things that need to be public should be.

## Grading
| Feature                          | Points |
|----------------------------------|--------|
| Load CSV                         | 10     |
| Load CSV Only Once               | 5      |
| Print List                       | 10     |
| Search                           | 10     |
| Add New Item                     | 10     |
| Correct files / modules          | 5      |
| `__str__` Magic Methods          | 5      |
| `CSVProcessor` Class             | 5      |
| `UserInterface` Class            | 5      |
| `Beverage` Class                 | 5      |
| `BeverageCollection` Class       | 5      |
| A Control Structure              | 5      |
| A Loop                           | 5      |
| A Method                         | 5      |
| Documentation                    | 5      |
| Readme                           | 5      |
| **Total**                        | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program


