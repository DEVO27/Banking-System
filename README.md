# Banking-System

## Overview:
- This is a simulated version of a simple banking application that uses sqlite3 
for working with SQL databases and the Luhn algorithm for 
validating identification numbers on a credit card. 
Throughout this article, I will demonstrate its properties and how it's used. 

## Luhn algorithm
- The * [Luhn](https://en.wikipedia.org/wiki/Luhn_algorithm) algorithm is a widely 
used mathematical formula that will be used to validate the authenticity of 
identification numbers on the generated credit card numbers in the program. 
The first six digits in the program known as the MII or (Major Industry Identifier) 
will always start with 400000. The proceeding numbers are randomly generated as well 
as the PIN corresponding to its cardmember. 

