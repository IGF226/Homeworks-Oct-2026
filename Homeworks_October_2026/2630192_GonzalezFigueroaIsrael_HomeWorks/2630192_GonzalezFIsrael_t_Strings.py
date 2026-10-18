"""
===============================================================================
HEADER
===============================================================================
Student Name: Israel Gonzalez Figueroa
Student ID: 2630192
Group: 2
===============================================================================

===============================================================================
EXECUTIVE SUMMARY
===============================================================================
In Python, a string (str) is a fundamental, built-in data type used to represent 
text sequences. A key characteristic of strings is their immutability; once 
created, their contents cannot be altered in place, meaning any operation that 
modifies a string always generates a completely new string object. 
Basic manipulations include concatenation, fetching sequence length, extracting 
substrings via slicing, pattern searching, and replacing characters. 
Validating and normalizing user input (e.g., trimming whitespace or aligning 
letter casing) is crucial to guarantee data integrity, prevent system errors, 
and secure applications from broken layouts or malicious inputs. 
This script implements 6 distinct problems focusing on advanced text manipulation, 
structured validation workflows, and algorithmic constraints using built-in string methods.
===============================================================================

===============================================================================
PRINCIPLES AND BEST PRACTICES
===============================================================================
- Strings are immutable: modifying operations always allocate new text objects.
- Input data should be normalized using strip() and lower() before comparisons.
- Avoid 'magic numbers' in string indices; explicitly document slice targets.
- Rely on built-in string methods rather than re-inventing basic loop logic.
- Structure validation sequences logically: check for empty values first, 
  followed by strict format requirements.
- Write maintainable code: use expressive variable naming and explicit errors.
===============================================================================
"""

# =============================================================================
# PROBLEM 1: Full name formatter (name + initials)
# =============================================================================
"""
Problem 1: Full name formatter (name + initials)
Description: Takes a single string representing a person's full name, 
normalizes redundant spaces or mixed casing, and converts it to Title Case. 
It also extracts the first letter of each word to build initials separated by periods.

Inputs:
- full_name (string): raw text containing names and surnames.

Outputs:
- Formatted name in Title Case.
- Extracted initials.

Validations:
- The input string must not be empty after strip().
- Must contain at least two separate words (e.g., a name and a surname).
- Must not consist exclusively of blank spaces.

Test cases:
1) Normal: "  juan carlos tovar  " -> Title Case and 'J.C.T.' initials.
2) Border: "a b" -> Minimal distinct words validation.
3) Error: "    " or "SingleWord" -> Triggers empty or missing surname errors.
"""

def format_full_name(full_name_input):
    print(f"\n--- Testing Problem 1 with input: '{full_name_input}' ---")
    
    # Validation 1: Check for empty string after strip
    clean_name = full_name_input.strip()
    if not clean_name:
        print("Error: invalid input")
        return
        
    # Validation 2: Split words to ensure at least two elements exist
    name_parts = clean_name.split()
    if len(name_parts) < 2:
        print("Error: invalid input")
        return
        
    # Processing logic
    # Rebuild normalized title case name from the split parts to drop internal multi-spaces
    formatted_name = " ".join(name_parts).title()
    
    # Generate initials
    initials_list = [word[0].upper() + "." for word in name_parts]
    initials = "".join(initials_list)
    
    # Expected structured outputs
    print(f"Result: success")
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# =============================================================================
# PROBLEM 2: Simple email validator (structure + domain)
# =============================================================================
"""
Problem 2: Simple email validator (structure + domain)
Description: Verifies if a given string adheres to basic email structure rules:
contains exactly one '@' character, has at least one '.' after the '@', 
and contains no whitespace character sequences. Extracts domain if valid.

Inputs:
- email_text (string): raw user email input.

Outputs:
- "Valid email: true" or "Valid email: false"
- Domain part string (only if valid).

Validations:
- Input must not be empty after cleaning.
- Exactly one '@' symbol must be present.
- At least one dot '.' must appear in the substring following the '@'.
- No whitespace characters are allowed inside the text.

Test cases:
1) Normal: "user@domain.com" -> Valid: true, Domain: domain.com.
2) Border: "a@b.c" -> Smallest possible valid layout structure.
3) Error: "user @domain.com" or "invalid@domain" -> Triggers validation failures.
"""

def validate_simple_email(email_text):
    print(f"\n--- Testing Problem 2 with input: '{email_text}' ---")
    
    clean_email = email_text.strip()
    
    # Validation 1: Check if empty
    if not clean_email:
        print("Valid email: false")
        print("Error: invalid input")
        return
        
    # Validation 2: Check for forbidden spaces anywhere inside the string
    if " " in clean_email:
        print("Valid email: false")
        return
        
    # Validation 3: Must contain exactly one '@'
    if clean_email.count("@") != 1:
        print("Valid email: false")
        return
        
    # Slicing out the domain part
    at_index = clean_email.find("@")
    domain_part = clean_email[at_index + 1:]
    
    # Validation 4: Domain must contain at least one '.' and not be empty
    if "." not in domain_part or not domain_part:
        print("Valid email: false")
        return
        
    print("Valid email: true")
    print(f"Domain: {domain_part}")


# =============================================================================
# PROBLEM 3: Palindrome checker (ignoring spaces and case)
# =============================================================================
"""
Problem 3: Palindrome checker (ignoring spaces and case)
Description: Determines whether a text phrase is a palindrome by verifying 
if it reads identically backwards and forwards. Casing and whitespace are ignored.

Inputs:
- phrase (string): raw text to test.

Outputs:
- "Is palindrome: true" or "Is palindrome: false"
- Displays normalized sentence structure.

Validations:
- String must not be empty after stripping spaces.
- Clean text must meet a minimum length constraint of 3 characters.

Test cases:
1) Normal: "Anita lava la tina" -> Is palindrome: true.
2) Border: "AbA" or "   x y x   " -> Short valid structure.
3) Error: "No" or "   " -> Triggers length or empty exceptions.
"""

def check_palindrome(phrase):
    print(f"\n--- Testing Problem 3 with input: '{phrase}' ---")
    
    # Validation 1: Initial empty validation
    if not phrase.strip():
        print("Error: invalid input")
        return
        
    # Normalization: lower case and eliminate all white spaces
    normalized_phrase = phrase.lower().replace(" ", "")
    
    # Validation 2: Enforce a minimum length of 3 valid characters
    if len(normalized_phrase) < 3:
        print("Error: invalid input")
        return
        
    # Inversion slicing check
    reversed_phrase = normalized_phrase[::-1]
    is_palindrome = (normalized_phrase == reversed_phrase)
    
    # Output formatting
    print(f"Normalized text: {normalized_phrase}")
    if is_palindrome:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# =============================================================================
# EXECUTING TEST CASES FOR PART 1
# =============================================================================
print("=== RUNNING TEST CASES FOR PART 1 ===")

# Problem 1 Tests
format_full_name("  juan carlos tovar  ") # Normal
format_full_name("a b")                    # Border
format_full_name("SingleWord")             # Error

# Problem 2 Tests
validate_simple_email("user@domain.com")   # Normal
validate_simple_email("a@b.c")              # Border
validate_simple_email("user @domain.com")  # Error

# Problem 3 Tests
check_palindrome("Anita lava la tina")    # Normal
check_palindrome("   x y x   ")            # Border
check_palindrome("No")                     # Error

# =============================================================================
# PROBLEM 4: Sentence word stats (lengths and first/last word)
# =============================================================================
"""
Problem 4: Sentence word stats (lengths and first/last word)
Description: Analyzes an input sentence to count total words, extract the 
first and last words, and locate the shortest and longest words based on character length.

Inputs:
- sentence (string): sequence of text words.

Outputs:
- Total word count, first word, last word, shortest word, and longest word.

Validations:
- String must not be empty after applying strip().
- Must contain at least one valid word after split parsing.

Test cases:
1) Normal: "Python is an amazing programming language" -> Correct breakdown.
2) Border: "   Hello   " -> Single word boundary handling.
3) Error: "     " -> Structural validation failure.
"""

def get_sentence_stats(sentence):
    print(f"\n--- Testing Problem 4 with input: '{sentence}' ---")
    
    clean_sentence = sentence.strip()
    if not clean_sentence:
        print("Error: invalid input")
        return
        
    words = clean_sentence.split()
    if len(words) == 0:
        print("Error: invalid input")
        return
        
    # Extract first and last positions
    first_word = words[0]
    last_word = words[-1]
    
    # Algorithm to find shortest and longest elements
    shortest_word = words[0]
    longest_word = words[0]
    
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
            
    print(f"Word count: {len(words)}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# =============================================================================
# PROBLEM 5: Password strength classifier
# =============================================================================
"""
Problem 5: Password strength classifier
Description: Scans character properties inside an input string to assign 
a security tier classification: weak, medium, or strong.

Rules applied:
- Weak: Length < 8 characters, or entirely uppercase, or entirely lowercase, or entirely digits.
- Strong: Length >= 8 and contains >=1 uppercase, >=1 lowercase, >=1 digit, and >=1 symbol.
- Medium: Fits neither category (e.g., length >= 8 but lacks a required strong symbol type).

Inputs:
- password_input (string): raw password characters.

Outputs:
- "Password strength: weak" | "medium" | "strong"

Validations:
- Password string cannot be empty.

Test cases:
1) Normal: "SecureP@ss123" -> Strength: strong.
2) Border: "abc12345" -> Strength: medium (No upper/symbols).
3) Error: "" or "123" -> Triggers empty validation or defaults to weak.
"""

def classify_password(password_input):
    print(f"\n--- Testing Problem 5 with input: '{password_input}' ---")
    
    if not password_input:
        print("Error: invalid input")
        return
        
    password_len = len(password_input)
    
    # Booleans tracking character classes
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True
            
    # Conditional logic tree classification
    if password_len < 8 or (password_input.isdigit() or password_input.islower() or password_input.isupper()):
        print("Password strength: weak")
    elif password_len >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")


# =============================================================================
# PROBLEM 6: Product label formatter (fixed-width text)
# =============================================================================
"""
Problem 6: Product label formatter (fixed-width text)
Description: Generates a unified product price tag forced into a fixed length 
of exactly 30 characters via pad truncation configurations.

Inputs:
- product_name (string)
- price_value (string or numeric value)

Outputs:
- "Label: <exactly 30 characters layout>"

Validations:
- product_name must not be empty after strip().
- price_value must successfully convert into a non-negative float.

Test cases:
1) Normal: name="Laptop", price=999.99 -> Padded appropriately.
2) Border: name="SuperLongProductNameThatExceedsTheLimit", price=10.0 -> Truncated precisely.
3) Error: name="   ", price=-50.0 -> Invalid formatting context.
"""

def generate_product_label(product_name, price_value):
    print(f"\n--- Testing Problem 6 with inputs: Name='{product_name}', Price={price_value} ---")
    
    clean_name = product_name.strip()
    if not clean_name:
        print("Error: invalid input")
        return
        
    try:
        numeric_price = float(price_value)
        if numeric_price < 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return
        
    # Build standard raw base template label
    base_label = f"Product: {clean_name} | Price: ${numeric_price:.2f}"
    base_len = len(base_label)
    TARGET_LENGTH = 30
    
    if base_len > TARGET_LENGTH:
        # Truncate string sequence down to limit
        final_label = base_label[:TARGET_LENGTH]
    else:
        # Pad remaining space using trailing blank slots
        final_label = base_label + " " * (TARGET_LENGTH - base_len)
        
    # Wrap in single quotes to visualize spaces explicitly inside console
    print(f"Label: '{final_label}'")
    print(f"Length: {len(final_label)}")


# =============================================================================
# EXECUTING TEST CASES FOR PART 2
# =============================================================================
print("\n=== RUNNING TEST CASES FOR PART 2 ===")

# Problem 4 Tests
get_sentence_stats("Python is an amazing programming language") # Normal
get_sentence_stats("   Hello   ")                            # Border
get_sentence_stats("     ")                                    # Error

# Problem 5 Tests
classify_password("SecureP@ss123")  # Normal
classify_password("abc12345")       # Border
classify_password("")               # Error

# Problem 6 Tests
generate_product_label("Laptop", 999.99)                                # Normal
generate_product_label("SuperLongProductNameThatExceedsTheLimit", 10.0) # Border
generate_product_label("   ", -50.0)                                    # Error


"""
===============================================================================
CONCLUSIONS
===============================================================================
- String management is essential for standard inputs and outputs, acting as the 
  primary gateway between user input and back-end logic.
- Built-in methods like lower(), strip(), and split() drastically minimize 
  manual iteration overhead and prevent text analysis bugs.
- Early text normalization protects databases from holding polluted or duplicate records 
  (e.g., differentiating data due to trailing spaces).
- Rigid validation routines trap data anomalies and empty entries before processing, 
  reducing runtime exceptions.
- Working with string immutability highlights that text modifications generate new 
  objects, reinforcing the memory efficiency value of slicing configurations.
===============================================================================

===============================================================================
REFERENCES
===============================================================================
References:
1) Python Software Foundation. (2026). Built-in Types: Text Sequence Type — str. 
   Python Documentation. https://python.org
2) Real Python Team. (2025). Python Strings and Character Data: An Introduction. 
   Real Python Tutorials. https://realpython.com
3) Sweigart, A. (2020). Automate the Boring Stuff with Python (2nd ed.). No Starch Press. 
   (Chapter 6: Manipulating Strings).
4) Van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 -- Style Guide for Python Code. 
   Python Enhancement Proposals. https://python.org
5) W3Schools Portal. (2026). Python String Methods Reference Catalog. 
   W3Schools Reference Guide. https://w3schools.com
===============================================================================

===============================================================================
GitHub Repository URL: https://github.com/IGF226/Homeworks-Oct-2026
===============================================================================
"""