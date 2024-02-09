# Project Description

This project is a Python command-line interpreter for a simple version of AirBnB, designed to manage objects in a file storage system. It includes a base model class and a command interpreter to interact with instances of various classes.

## Command Interpreter

The command interpreter allows users to create, destroy, update, and display instances of the classes defined in the project. It supports both interactive and non-interactive modes.

### How to Start

To start the command interpreter, navigate to the project directory and run the `console.py` script.

```bash```
$ ./console.py

# How to Use
    Once the command interpreter is started, users can enter commands to interact with the objects. The supported commands include:

    create: Create a new instance of a class.
    show: Display information about a specific instance.
    destroy: Delete a specific instance.
    update: Update attributes of a specific instance.
    all: Display information about all instances of a class or all classes.
    quit or EOF: Exit the command interpreter.
    The command interpreter supports tab completion, history, and command line editing using the GNU readline library.

## Examples
    Here are some examples of how to use the command interpreter:

    1. Creating a new instance:

(hbnb) create BaseModel
    2. Showing information about an instance:

(hbnb) show BaseModel 1234-5678-9012
    3. Updating attributes of an instance:

(hbnb) update BaseModel 1234-5678-9012 name "New Name"
    4.Displaying information about all instances:

(hbnb) all
    5.Exiting the command interpreter:

(hbnb) quit

## Additional Information
    This README provides an overview of the project, the command interpreter, how to start and use it, and some    examples of commands. If you have any further questions or need assistance, feel free to reach out!
