import re


# Scans the entire string for a match. 
# Returns the first match found, even if it's not at the beginning.
# Useful when the pattern can appear anywhere in the string.

text = "HO Python academy 2025"
pattern = r"academy"

search =re.search(pattern, text)
if search:
    print("Pattern found:", search.group())  # Output: academy
else:
    print("Pattern not found")

#match
# Only checks for a match at the beginning of the string.
# If the pattern doesn't start at index 0, it returns None.

pattern = r"HO"

match =re.match(pattern, text)
if match:
    print("Match found:", match.group())  # Output: HO
else:
    print("Match not found")


#replace
# Replaces all occurrences of the pattern in the string with a specified replacement string.
pattern = r"HO"

replacement = "Capgemini - HO"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)


#split
# Splits the string at each occurrence of the pattern and returns a list of substrings.
pattern = r" "  # Split at spaces

split_result = re.split(pattern, text)
print("Split result:", split_result)
