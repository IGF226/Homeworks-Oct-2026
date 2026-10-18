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
In Python, 'int' represents whole numbers without decimals, whereas 'float' represents 
real numbers with decimal components. Booleans (bool) store binary truth conditions 
expressed exclusively as True or False, typically generated through comparison operators. 
Validating mathematical domain boundaries—such as filtering out negative metrics where 
physically impossible and actively preventing zero-division scenarios—is critical 
to avert software crashes and avoid runtime exceptions. This script features 6 structured 
problems that handle arithmetic conversions, logical condition blending using 
'and', 'or', 'not' syntax, data validation workflows, and automated test execution.
===============================================================================

===============================================================================
PRINCIPLES AND BEST PRACTICES 
===============================================================================
- Select appropriate data types: use int for tallies/counters, float for real values.
- Cache repetitive or dense calculations inside intermediate variables for speed.
- Validate bounds thoroughly before computing (e.g., test that salary or hours >= 0).
- Assign self-descriptive variable names and write intuitive console layouts.
- Formally document booleans to show exactly what True and False represent.
===============================================================================
"""

# =============================================================================
# PROBLEM 1: Temperature converter and range flag
# =============================================================================
"""
Problem 1: Temperature converter and range flag
Description: Converts a Celsius value (float) to Fahrenheit and Kelvin. It also
determines a boolean flag 'is_high_temperature' which flags True if the Celsius 
value is equal to or greater than 30.0.

Inputs:
- temp_c (float): temperature value in degrees Celsius.

Outputs:
- Fahrenheit converted value.
- Kelvin converted value.
- High temperature boolean indicator.

Validations:
- Input value must be capable of parsing into a float.
- Enforce the absolute physical temperature boundary (Kelvin cannot be < 0.0).

Test cases:
1) Normal: 35.5 -> High temperature: true, correctly converts to F and K.
2) Border: -273.15 -> Absolute zero edge boundary case (Kelvin: 0.0).
3) Error: -300.0 -> Triggers an absolute physical temperature error.
"""

def convert_temperature(temp_c_input):
    print(f"\n--- Testing Problem 1 with input: {temp_c_input} ---")
    
    try:
        temp_c = float(temp_c_input)
    except ValueError:
        print("Error: invalid input")
        return
        
    # Temporal validation to prevent absolute zero violations
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
        return
        
    # Conversions
    temp_f = (temp_c * 9 / 5) + 32
    is_high_temperature = (temp_c >= 30.0)
    
    # Python displays Booleans as True/False; lowercasing to match assignment layout examples
    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {str(is_high_temperature).lower()}")


# =============================================================================
# PROBLEM 2: Work hours and overtime payment
# =============================================================================
"""
Problem 2: Work hours and overtime payment
Description: Computes total weekly wages. Hours up to 40 are paid at regular rate. 
Overtime hours (> 40) are paid at 150% of the normal rate. Tracks whether overtime 
occurred via a boolean flag.

Inputs:
- hours_worked (float): total hours clocked in the week.
- hourly_rate (float): hourly pay scale value.

Outputs:
- Regular base pay.
- Overtime premium pay.
- Total combined pay.
- Has overtime boolean indicator.

Validations:
- Total hours worked must be greater than or equal to 0.
- Hourly wage rate must be strictly greater than 0.

Test cases:
1) Normal: hours=45.0, rate=20.0 -> 40 regular hours, 5 overtime hours.
2) Border: hours=40.0, rate=15.0 -> Exactly on the overtime boundary.
3) Error: hours=-5.0, rate=25.0 -> Triggers a negative attribute error.
"""

def calculate_weekly_pay(hours_worked, hourly_rate):
    print(f"\n--- Testing Problem 2 with hours={hours_worked}, rate={hourly_rate} ---")
    
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return
        
    # Isolate regular and overtime distributions using min/max constraints
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(0.0, hours_worked - 40.0)
    
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    
    has_overtime = (hours_worked > 40.0)
    
    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")


# =============================================================================
# PROBLEM 3: Discount eligibility with booleans
# =============================================================================
"""
Problem 3: Discount eligibility with booleans
Description: Validates discount parameters based on age, student enrollment, 
or total purchase volume. Applies a 10% markdown if criteria match.

Inputs:
- purchase_total (float): aggregate store cart total.
- is_student_text (string): text input flags ('YES' or 'NO').
- is_senior_text (string): text input flags ('YES' or 'NO').

Outputs:
- Discount eligible boolean indicator.
- Final invoice cost.

Validations:
- Cart purchase totals must be greater than or equal to 0.0.
- Normalizes textual conditions; strings must be explicitly 'YES' or 'NO'.

Test cases:
1) Normal: total=500.0, student="YES", senior="NO" -> Eligible via student flag.
2) Border: total=1000.0, student="NO", senior="NO" -> Eligible via purchase volume edge.
3) Error: total=150.0, student="MAYBE", senior="NO" -> Invalid text configuration error.
"""

def evaluate_discount(purchase_total, is_student_text, is_senior_text):
    print(f"\n--- Testing Problem 3 with total={purchase_total}, student='{is_student_text}', senior='{is_senior_text}' ---")
    
    if purchase_total < 0.0:
        print("Error: invalid input")
        return
        
    # Text standardization normalization pipeline
    student_clean = is_student_text.strip().upper()
    senior_clean = is_senior_text.strip().upper()
    
    if student_clean not in ["YES", "NO"] or senior_clean not in ["YES", "NO"]:
        print("Error: invalid input")
        return
        
    # Map textual flags directly to boolean variables
    is_student = (student_clean == "YES")
    is_senior = (senior_clean == "YES")
    
    # Combined Boolean evaluation
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    
    if discount_eligible:
        final_total = purchase_total * 0.90
    else:
        final_total = purchase_total
        
    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")


# =============================================================================
# EXECUTING TEST CASES FOR PART 1
# =============================================================================
print("=== RUNNING TEST CASES FOR PART 1 ===")

# Problem 1 Tests
convert_temperature(35.5)       # Normal
convert_temperature(-273.15)    # Border
convert_temperature(-300.0)     # Error

# Problem 2 Tests
calculate_weekly_pay(45.0, 20.0) # Normal
calculate_weekly_pay(40.0, 15.0) # Border
calculate_weekly_pay(-5.0, 25.0) # Error

# Problem 3 Tests
evaluate_discount(500.0, "YES", "NO")  # Normal
evaluate_discount(1000.0, "NO", "NO")  # Border
evaluate_discount(150.0, "MAYBE", "NO") # Error

# =============================================================================
# PROBLEM 4: Basic statistics of three integers
# =============================================================================
"""
Problem 4: Basic statistics of three integers
Description: Evaluates three integers to compute mathematical metrics: 
total sum, floating-point average, maximum, minimum, and checks if all inputs are even.

Inputs:
- n1, n2, n3 (int): three whole numbers.

Outputs:
- Sum, Average, Max, Min, and All even boolean flag.

Validations:
- Inputs must successfully convert to integer datatypes. Negative values are allowed.

Test cases:
1) Normal: 10, 20, 30 -> Sum=60, Avg=20.0, Max=30, Min=10, All even=true.
2) Border: 0, 0, 0 -> Zero threshold compliance check.
3) Error: "ten", 20, 30 -> Triggers type parsing failure exception.
"""

def calculate_three_int_stats(n1_in, n2_in, n3_in):
    print(f"\n--- Testing Problem 4 with inputs: {n1_in}, {n2_in}, {n3_in} ---")
    
    try:
        n1 = int(n1_in)
        n2 = int(n2_in)
        n3 = int(n3_in)
    except ValueError:
        print("Error: invalid input")
        return
        
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    # Combined logical evaluation to verify parity status
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")


# =============================================================================
# PROBLEM 5: Loan eligibility (income and debt ratio)
# =============================================================================
"""
Problem 5: Loan eligibility (income and debt ratio)
Description: Evaluates financial profile variables against strict credit 
risk constraints to determine loan approvals.

Inputs:
- monthly_income (float): base monthly salary earnings.
- monthly_debt (float): ongoing active recurring debit payouts.
- credit_score (int): standard credit bureau score record.

Outputs:
- Computed debt relative metric ratio.
- Loan approval eligibility decision status.

Validations:
- Monthly income must be strictly greater than 0.0 (prevents division by zero errors).
- Debt and score allocations cannot drop below 0.

Test cases:
1) Normal: income=9000.0, debt=1800.0, score=700 -> Ratio=0.2, Eligible=true.
2) Border: income=8000.0, debt=3200.0, score=650 -> Ratio=0.4, Eligible=true (exact limits).
3) Error: income=0.0, debt=500.0, score=600 -> Zero income triggers input failure.
"""

def evaluate_loan_eligibility(monthly_income, monthly_debt, credit_score):
    print(f"\n--- Testing Problem 5 with income={monthly_income}, debt={monthly_debt}, score={credit_score} ---")
    
    # Early validation routine to prevent zero-division or invalid records
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return
        
    debt_ratio = monthly_debt / monthly_income
    
    # Rules matrix lookup checking parameters simultaneously
    is_eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    
    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {str(is_eligible).lower()}")


# =============================================================================
# PROBLEM 6: Body Mass Index (BMI) and category flag
# =============================================================================
"""
Problem 6: Body Mass Index (BMI) and category flag
Description: Computes Body Mass Index based on mass metrics, and maps outcomes 
to classification boolean flags.

Inputs:
- weight_kg (float): body mass volume in kilograms.
- height_m (float): height metric in meters.

Outputs:
- Calculated BMI index rounded up to 2 decimals.
- Underweight, Normal, and Overweight status values.

Validations:
- Both weight and height input parameters must be strictly greater than 0.0.

Test cases:
1) Normal: weight=70.0, height=1.75 -> BMI=22.86 (Normal weight spectrum).
2) Border: weight=56.66, height=1.75 -> BMI=18.5 (Exact transition boundary).
3) Error: weight=70.0, height=0.0 -> Zero tracking triggers error detection.
"""

def calculate_bmi_metrics(weight_kg, height_m):
    print(f"\n--- Testing Problem 6 with weight={weight_kg}, height={height_m} ---")
    
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return
        
    bmi = weight_kg / (height_m * height_m)
    
    # Mutually exclusive logical boundary mapping
    is_underweight = (bmi < 18.5)
    is_normal = (18.5 <= bmi < 25.0)
    is_overweight = (bmi >= 25.0)
    
    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")


# =============================================================================
# EXECUTING TEST CASES FOR PART 2
# =============================================================================
print("\n=== RUNNING TEST CASES FOR PART 2 ===")

# Problem 4 Tests
calculate_three_int_stats(10, 20, 30)       # Normal
calculate_three_int_stats("0", 0, 0)        # Border
calculate_three_int_stats("ten", 20, 30)    # Error

# Problem 5 Tests
evaluate_loan_eligibility(9000.0, 1800.0, 700) # Normal
evaluate_loan_eligibility(8000.0, 3200.0, 650) # Border
evaluate_loan_eligibility(0.0, 500.0, 600)     # Error

# Problem 6 Tests
calculate_bmi_metrics(70.0, 1.75)   # Normal
calculate_bmi_metrics(56.66, 1.75)  # Border
calculate_bmi_metrics(70.0, 0.0)    # Error


"""
===============================================================================
CONCLUSIONS 
===============================================================================
- Integers and floats work closely together in software engineering, where casting 
  manages conversions when moving from base quantities to precise decimals.
- Relational comparisons produce clear, robust booleans that serve as data checkpoints 
  to steer control flows safely.
- Enforcing structural boundary rules and stopping mathematical errors (like zero-division) 
  safeguards runtime execution from critical software failures.
- Designing chained conditions with 'and', 'or', and 'not' helps translate 
  intricate real-world logic patterns into structured, predictable code execution blocks.
- These programming blueprints easily mirror standard institutional logic patterns, 
  including banking policies, healthcare benchmarks, and paycheck structures.
===============================================================================

===============================================================================
REFERENCES
===============================================================================
References:
1) Python Software Foundation. (2026). Built-in Types: Numeric Types — int, float, complex. 
   Python Documentation. https://python.org
2) Python Software Foundation. (2026). Built-in Types: Boolean Type — bool. 
   Python Documentation. https://python.org
3) Matthes, E. (2023). Python Crash Course: A Hands-On, Project-Based Introduction to Programming (3rd ed.). 
   No Starch Press. (Chapter 2: Variables and Simple Data Types - Numbers).
4) Beazley, D. M., & Jones, B. K. (2013). Python Cookbook: Recipes for Mastering Python 3 (3rd ed.). 
   O'Reilly Media. (Chapter 3: Numbers, Dates, and Times).
5) Downey, A. B. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.). 
   O'Reilly Media. (Chapter 5: Conditionals and Recursion).
===============================================================================

===============================================================================
GitHub Repository URL: https://github.com/IGF226/Homeworks-Oct-2026
===============================================================================
"""