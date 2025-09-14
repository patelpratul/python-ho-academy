# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)


# String length
text = "HO Python academy"
length = len(text)
print("Length of the string:", length)



# String length
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)


# String replacement
new_text = text.replace("HO", "Capgemini - HO")
print("Modified text:", new_text)

# String split
words = text.split()
print("Words:", words)

# String strip
txtstrip = "   HO Python academy   "
stripped_text = txtstrip.strip()
print("Stripped text:", stripped_text)

# String substring
substring = "Python"
if substring in text:
    print(substring, "found in the text")
