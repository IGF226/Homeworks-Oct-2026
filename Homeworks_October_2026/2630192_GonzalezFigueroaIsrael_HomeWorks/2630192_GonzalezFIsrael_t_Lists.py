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
In Python, lists, tuples, and dictionaries are the core built-in data collections.
A list is an ordered, mutable sequence ideal for dynamic data handling. Conversely,
a tuple is an ordered, immutable collection designed to protect fixed datasets.
Dictionaries associate unique keys with values, providing high-efficiency lookup 
and data relationship mapping. Mutability governs whether a collection can be changed 
in place or requires a new memory slot assignment. This document covers structured 
solutions for 6 distinct data problems using input sanitation, boundary analysis, 
and automated code verification scripts for lists, tuples, and dictionary lookups.
===============================================================================

===============================================================================
PRINCIPLES AND BEST PRACTICES
===============================================================================
- Choose lists for ordered collections that require constant insertion or deletion.
- Choose tuples for unalterable multi-element records like geometric coordinate pairs.
- Choose dictionaries for fast lookup mapping patterns using descriptive string keys.
- Do not alter the index or structure of a list while iterating over it via loop.
- Apply defensive get() methods or explicit membership 'in' keywords on dictionary records.
===============================================================================
"""

# =============================================================================
# PROBLEM 1: Shopping list basics (list operations)
# =============================================================================
"""
Problem 1: Shopping list basics (list operations)
Description: Builds a list of elements from a comma-separated string, appends 
a target single element, measures the collection size, and looks up a search parameter.

Inputs:
- initial_items_text (string): comma-separated words.
- new_item (string): element to append.
- search_item (string): element to find.

Outputs:
- Current dynamic items list.
- Calculated list length count.
- Found item tracking boolean flag.

Validations:
- Base string input sequence must not be empty after strip() operations.
- Clean text segments by dropping extra spaces from individual string items.
- Empty lists are flagged with an error.

Test cases:
1) Normal: "apple,banana,orange", new="grapes", search="banana" -> Success layout.
2) Border: "apple", new="peach", search="apple" -> Minimum element boundary check.
3) Error: "   ", new="", search="apple" -> Triggers empty list validation error.
"""

def process_shopping_list(initial_items_text, new_item, search_item):
    print(f"\n--- Testing Problem 1 with input: '{initial_items_text}' ---")
    
    if not initial_items_text.strip():
        print("Error: invalid input")
        return
        
    # Split text sequence and normalize individual word slots
    raw_list = initial_items_text.split(",")
    items_list = [item.strip() for item in raw_list if item.strip()]
    
    if len(items_list) == 0 or not new_item.strip() or not search_item.strip():
        print("Error: invalid input")
        return
        
    # Perform list operations
    items_list.append(new_item.strip())
    is_in_list = search_item.strip() in items_list
    
    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# =============================================================================
# PROBLEM 2: Points and distances with tuples
# =============================================================================
"""
Problem 2: Points and distances with tuples
Description: Generates two 2D immutable coordinate tuple positions, calculates 
their Euclidean distance space value, and derives a central midpoint location tuple.

Inputs:
- x1, y1, x2, y2 (float): geometric numeric point scalars.

Outputs:
- Tuple A coordinates.
- Tuple B coordinates.
- Calculated Euclidean distance value.
- Midpoint coordinate tuple position.

Validations:
- Coordinates must successfully parse into float values. No range boundaries required.

Test cases:
1) Normal: x1=0.0, y1=0.0, x2=3.0, y2=4.0 -> Distance=5.0, Midpoint=(1.5, 2.0).
2) Border: x1=1.5, y1=-1.5, x2=1.5, y2=-1.5 -> Overlapping points (Distance=0.0).
3) Error: x1="zero", y1=0.0, x2=1.0, y2=1.0 -> Triggers variable conversion error.
"""

def calculate_tuple_distance(x1_in, y1_in, x2_in, y2_in):
    print(f"\n--- Testing Problem 2 with points: ({x1_in}, {y1_in}), ({x2_in}, {y2_in}) ---")
    
    try:
        x1, y1 = float(x1_in), float(y1_in)
        x2, y2 = float(x2_in), float(y2_in)
    except ValueError:
        print("Error: invalid input")
        return
        
    # Pack parameters into tuple structures
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    # Calculate geometric values
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 4)}")
    print(f"Midpoint: {midpoint}")


# =============================================================================
# PROBLEM 3: Product catalog with dictionary
# =============================================================================
"""
Problem 3: Product catalog with dictionary
Description: Hosts a static mock inventory dictionary map. Pulls a target 
key, verifies match availability, and multiplies unit prices by purchase order metrics.

Inputs:
- product_name (string): name key lookup parameter.
- quantity (int): order unit multiplier value.

Outputs:
- Unit price tracking value.
- Ordered unit quantity.
- Computed total invoice cost.

Validations:
- Quantities ordered must be strictly greater than 0.
- Key name parameters cannot be empty strings.
- Key selection must match dictionary registry data.

Test cases:
1) Normal: name="apple", quantity=5 -> Found successfully.
2) Border: name="orange", quantity=1 -> Minimum order validation limit.
3) Error: name="banana", quantity=0 or name="pizza" -> Triggers out-of-stock or structure errors.
"""

def query_catalog_price(product_name, quantity):
    print(f"\n--- Testing Problem 3 with product='{product_name}', quantity={quantity} ---")
    
    # Hardcoded dictionary inventory map template
    product_prices = {
        "apple": 10.50,
        "banana": 5.75,
        "orange": 8.20
    }
    
    clean_name = product_name.strip().lower()
    if not clean_name or quantity <= 0:
        print("Error: invalid input")
        return
        
    # Look up item with key membership verification
    if clean_name not in product_prices:
        print("Error: product not found")
        return
        
    unit_price = product_prices[clean_name]
    total_price = unit_price * quantity
    
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {round(total_price, 2)}")


# =============================================================================
# EXECUTING TEST CASES FOR PART 1
# =============================================================================
print("=== RUNNING TEST CASES FOR PART 1 ===")

# Problem 1 Tests
process_shopping_list("apple,banana,orange", "grapes", "banana") # Normal
process_shopping_list("apple", "peach", "apple")                # Border
process_shopping_list("   ", "", "apple")                       # Error

# Problem 2 Tests
calculate_tuple_distance(0.0, 0.0, 3.0, 4.0)       # Normal
calculate_tuple_distance(1.5, -1.5, 1.5, -1.5)     # Border
calculate_tuple_distance("zero", 0.0, 1.0, 1.0)    # Error

# Problem 3 Tests
query_catalog_price("apple", 5)    # Normal
query_catalog_price("orange", 1)   # Border
query_catalog_price("pizza", 3)    # Error

# =============================================================================
# PROBLEM 4: Student grades with dict and list
# =============================================================================
"""
Problem 4: Student grades with dict and list
Description: Queries a nested list dictionary map storing records of student names 
and grade scores, evaluates mean performance averages, and assigns passage flags.

Inputs:
- student_name (string): key identification lookup parameter.

Outputs:
- List of raw grade objects.
- Total evaluated statistical mean average.
- Passed achievement status boolean flag.

Validations:
- Checked text inputs cannot be empty spaces.
- Target student entry must match a dictionary key.
- Grade arrays cannot be empty.

Test cases:
1) Normal: name="Alice" -> Average=87.5, Passed=true.
2) Border: name="Charlie" -> Average=70.0, Passed=true (Exact cutoff border).
3) Error: name="Bob" or name="Unknown" -> Triggers collection missing exceptions.
"""

def evaluate_student_grades(student_name):
    print(f"\n--- Testing Problem 4 with student='{student_name}' ---")
    
    # Internal map containing a dictionary of float list entries
    student_records = {
        "Alice": [90.0, 85.0, 87.5],
        "Bob": [], # Edge configuration for empty score arrays
        "Charlie": [60.0, 80.0, 70.0]
    }
    
    clean_name = student_name.strip()
    if not clean_name:
        print("Error: invalid input")
        return
        
    if clean_name not in student_records:
        print("Error: student not found")
        return
        
    grades_list = student_records[clean_name]
    
    # Validation constraint against division anomalies
    if len(grades_list) == 0:
        print("Error: invalid input")
        return
        
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0
    
    print(f"Grades: {grades_list}")
    print(f"Average: {round(average, 2)}")
    print(f"Passed: {str(is_passed).lower()}")


# =============================================================================
# PROBLEM 5: Word frequency counter (list + dict)
# =============================================================================
"""
Problem 5: Word frequency counter (list + dict)
Description: Parses a raw text sentence into an array list of tokens, drops common 
punctuation marks, counts word occurrence loops, and returns the highest tally.

Inputs:
- sentence (string): raw text prose paragraph line.

Outputs:
- Tokenized items words list.
- Dynamic key-value occurrences frequency map.
- Top recurring modal word token indicator.

Validations:
- Prose structure must not resolve into an empty string array after stripping.

Test cases:
1) Normal: "Python is great, and programming in Python is fun." -> Standard count.
2) Border: "   Word!   " -> Evaluates single tracking boundary values safely.
3) Error: "     " -> Raises structural empty validation text block flags.
"""

def count_word_frequencies(sentence):
    print(f"\n--- Testing Problem 5 with sentence: '{sentence}' ---")
    
    clean_sentence = sentence.strip()
    if not clean_sentence:
        print("Error: invalid input")
        return
        
    # Punctuation cleaning pipeline normalization
    normalized_text = clean_sentence.lower()
    punctuation_marks = [".", ",", "!", "?", ";", ":"]
    for mark in punctuation_marks:
        normalized_text = normalized_text.replace(mark, "")
        
    words_list = normalized_text.split()
    if len(words_list) == 0:
        print("Error: invalid input")
        return
        
    # Construct frequency dictionary map via loop parsing
    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
            
    # Locate highest occurring string match pattern key
    most_common_word = words_list[0]
    max_count = 0
    
    for key, val in freq_dict.items():
        if val > max_count:
            max_count = val
            most_common_word = key
            
    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# =============================================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# =============================================================================
"""
Problem 6: Simple contact book (dictionary CRUD)
Description: Simulates an abstract dictionary tracking database to perform database 
CRUD operations (ADD, SEARCH, DELETE) on address book parameters.

Inputs:
- action_text (string): runtime control keyword ('ADD', 'SEARCH', 'DELETE').
- name (string): lookup target reference parameter.
- phone (string): data attribute number (Applies for 'ADD' contexts).

Outputs:
- Contextual logging message matching targeted operation types.

Validations:
- Action options must perfectly map to supported keyword variations.
- Structural variables must clear empty string conditions.

Test cases:
1) Normal: action="ADD", name="David", phone="5551234" -> Inserts record.
2) Border: action="SEARCH", name="Alice" -> Fetches existing profile key.
3) Error: action="INVALID", name="Alice" or action="DELETE", name="Missing" -> Fails safely.
"""

# Global context initialization simulation
global_contacts = {
    "Alice": "111-2222",
    "Bob": "333-4444"
}

def execute_contact_crud(action_text, name, phone=""):
    print(f"\n--- Testing Problem 6 with action='{action_text}', name='{name}' ---")
    
    clean_action = action_text.strip().upper()
    clean_name = name.strip()
    
    if clean_action not in ["ADD", "SEARCH", "DELETE"] or not clean_name:
        print("Error: invalid input")
        return
        
    if clean_action == "ADD":
        clean_phone = phone.strip()
        if not clean_phone:
            print("Error: invalid input")
            return
        global_contacts[clean_name] = clean_phone
        print(f"Contact saved: {clean_name}, {clean_phone}")
        
    elif clean_action == "SEARCH":
        if clean_name in global_contacts:
            print(f"Phone: {global_contacts[clean_name]}")
        else:
            print("Error: contact not found")
            
    elif clean_action == "DELETE":
        if clean_name in global_contacts:
            global_contacts.pop(clean_name)
            print(f"Contact deleted: {clean_name}")
        else:
            print("Error: contact not found")


# =============================================================================
# EXECUTING TEST CASES FOR PART 2
# =============================================================================
print("\n=== RUNNING TEST CASES FOR PART 2 ===")

# Problem 4 Tests
evaluate_student_grades("Alice")   # Normal
evaluate_student_grades("Charlie") # Border
evaluate_student_grades("Bob")     # Error (Empty grades array validation)

# Problem 5 Tests
count_word_frequencies("Python is great, and programming in Python is fun.") # Normal
count_word_frequencies("   Word!   ")                                        # Border
count_word_frequencies("      ")                                             # Error

# Problem 6 Tests
execute_contact_crud("ADD", "David", "555-1234") # Normal
execute_contact_crud("SEARCH", "Alice")          # Border
execute_contact_crud("DELETE", "Ghost")          # Error


"""
===============================================================================
CONCLUSIONS
===============================================================================
- Lists, tuples, and dictionaries play unique roles in application development, 
  balancing execution speed with memory mutability rules.
- Lists provide highly flexible sequences for storing data streams that experience 
  constant appending, shifting, or sorting adjustments.
- Tuples protect spatial layout parameters and critical coordinates from accidental 
  mutations during running routines.
- Dictionaries speed up key lookups, serving as high-performance alternatives 
  to traditional slow indexing loops.
- Mixing collections—like populating dictionaries with float list payloads—creates 
  powerful architectures capable of modeling complex real-world data tracking apps.
===============================================================================

===============================================================================
REFERENCES
===============================================================================
References:
1) Python Software Foundation. (2026). Data Structures — Lists, Tuples, and Dictionaries. 
   Python Documentation. https://python.org
2) Real Python Team. (2025). Dictionaries in Python: Defining and Mutating Key-Value Pairs. 
   Real Python Tutorials. https://realpython.com
3) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media. 
   (Chapter 8: Lists and Dictionaries, Chapter 9: Tuples).
4) McKinney, W. (2022). Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.). 
   O'Reilly Media. (Chapter 3: Built-in Data Structures, Functions, and Files).
5) Phillips, D. (2018). Python 3 Object-Oriented Programming (3rd ed.). Packt Publishing. 
   (Chapter 6: Python Data Structures).
===============================================================================

===============================================================================
GitHub Repository URL: https://github.com/IGF226/Homeworks-Oct-2026
===============================================================================
"""