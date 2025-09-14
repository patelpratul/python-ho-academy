import os

# Environment Variables

# Access an environment variable
api_key = os.environ.get('API_KEY')
# Print the value (if it exists)
print(api_key)


#Setting Environment Variables
#You can temporarily set environment variables in your Python script:

# Set an environment variable
os.environ['API_KEY'] = 'your_api_key_here'

# Access it
print(os.environ['API_KEY'])


#other way you can pass environment variables when running a script from the command line:
#run this first line ❯ export password="patel" that will set the environment variable
#then run the python script ❯ python 07_Evnironmentvariable.py
print (os.getenv("password"))
