# INVC Package
## Iranians National Code Validation
### This package validates the national code of Iranians
	
Now in most production software, there is a need to use the **national code** as a unique feature for personal information.
This package verifies the national code of individuals.

The national code is a 10-digit number from the left, three digits of the city code of the place of issuance of the identity card, the next six digits of the unique code for the person holding the ID card in the place of issuance, and the last digit of a control digit of 9 digits from the left. obtained. To check the code control, it is enough to recalculate the control digit from the 9 digits on the left.
Because in the national code system, there is usually a number before the code (the first digit and the second digit from the left of the national code may be zero) and in many cases, the user may not have entered these zeros or if these Zeros are not stored, it is better to add the required number (one to two to zero) to the left of the number before any action, if the length of the larger code is 8 and less than 10.

## Program logic
1. To calculate the control digit from other digits, multiply each digit in its position and add the result together.
2. Divide the sum obtained from step one by 11.
3. If the remainder is less than 2, the control digit must be equal to the remainder, otherwise the control digit must be equal to eleven minus the remainder.
## INCV in PyPi
You can find this package [here](https://pypi.org/project/INCV/).
## Install
`pip install INCV`

## How to use?
```
from INCV import CodeValidation

code = "0123456789"
result = CodeValidation(code)
```
The result is True or False.