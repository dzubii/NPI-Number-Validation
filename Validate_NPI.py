# -*- coding: utf-8 -*-
# A National Provider Identifier (NPI) is a unique 10-digit identification number issued to health care providers in the United States.

# Given that an NPI number follows the algorithm defined https://www.eclaims.com/articles/how-to-calculate-the-npi-check-digit/, write a function that validates a given number.

# Do not use any libraries, show us how you would solve this problem without the use of a library.

def validate_npi(npi):
    
    # Transform npi input into a list using list comprehension
    npi_list = [int(x) for x in str(npi)]
    
    # Assign cDigit to index=10 of npi_list
    cDigit = npi_list[-1]
    
    # Make a list without the check digit
    short_list = npi_list[0:-1]
    
    # Step 1 - double the value of every second digit
    for digit in range(0, 9, 2):
        short_list[digit] *= 2
        
    # Step 2 - take the sum of the individual digits
    sumDigits = 0
    double_digits_list = []
    # Adding all single digits to sumDigits
    for digit in short_list:
        if digit < 10:
            sumDigits += digit
        # Splitting double digits       
        if digit >= 10:
            double_digits_list += map(int,str(digit))
            
    # Adding double digits that have been split to sumDigits
    for i in double_digits_list:
        sumDigits += i
    
    # Step 3 - add 24 to sumDigits
    sumDigits += 24
    
    # Step 4 - take the units digit from sumDigits
    sumDigits_list = [int(y) for y in str(sumDigits)]
    unitsDigit = sumDigits_list[-1]
    
    # Step 5 & 6 - subtract the units digit from 10 if required
    if unitsDigit != 0:
        checkDigit = 10 - unitsDigit
    
    # Validate given npi against calculated npi
    if checkDigit == npi_list[-1]:
        return True
    else:
        return False
