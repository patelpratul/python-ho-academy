What is the main() function in Python?
Unlike some other languages like C or Java, Python does not require a main() function to run a script. However, using one is considered good practice for organizing code, especially in larger projects.


Why use a main() function?
• Improves readability: Makes it clear where the program starts.
• Encourages modularity: Keeps code organized into functions.
• Supports reusability: Allows parts of the script to be imported without running everything.
Helps with testing: Prevents code from executing when imported as a module.

 Basic Structure of a Python Script with main()

```python
 def main():
  print("Hello from main!")
 if __name__ == "__main__":
  main()


  # def main():
  This defines the main function where your core logic goes.
  # if __name__ == "__main__":
  This checks whether the script is being run directly or imported as a module.
  # If run directly → main() is called.
  If imported → main() is not called automatically.



  #Example
  # ```python 
  def greet(name):
   print(f"Hello, {name}!")
  def main():
   user_name = input("Enter your name: ")
   greet(user_name)
  if __name__ == "__main__":
   main()



   #Project Structure 
   Basic Project Structure with main.py
   This is common for small to medium-sized scripts or applications.
   my_project/
   ├── main.py
   ├── utils.py
   ├── config.py
   └── README.md

   # main.py
   • Entry point of the application.
   Contains the main() function and the if __name__ == "__main__" block.

   #utils.py
   • Helper functions used by main.py.
   # config.py
   Configuration variables or constants.
   

   # Package Structure (for larger projects or libraries)
   This is more modular and scalable.
   my_package/
   ├── my_package/
   │   ├── __init__.py
   │   ├── main.py
   │   ├── module1.py
   │   └── module2.py
   ├── tests/
   │   ├── test_module1.py
   │   └── test_module2.py
   ├── requirements.txt
   ├── setup.py
   └── README.md
   
 

# __init__.py
• Makes the folder a Python package.
• Can initialize package-level variables or imports.
# main.py
• Can contain the main() function or CLI logic.
# setup.py
• Used for packaging and distribution.
# tests/
Contains unit tests for each module.
