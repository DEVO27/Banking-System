# Banking-System

## Overview
- This is a simulated version of a simple banking application that uses sqlite3 
for working with SQLite databases and the Luhn algorithm for 
validating identification numbers on a credit card. 
Throughout this article, I will demonstrate its properties and how it's used. 

## Legend
* [Luhn algorithm](#Luhn-algorithm)
* [SQLite](#SQLite)
* [Getting Started](#Getting-Started)

## Luhn algorithm
- The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is a widely used 
mathematical formula that will be used to validate the authenticity of identification 
numbers of our generated credit card numbers. The first six digits in the program 
known as the MII or (Major Industry Identifier) will always start with 400000. 
The proceeding numbers are randomly generated along with the corresponding PIN 
cardmember. The pin is a randomly generated card number from 0000 to 9999.

## SQLite
As stated beforehand this program uses the sqlite3 for its database configuration. 
Below is the structure of the database:
  - id number
  - card number
  - pin
  - balance
All data will be stored in this manner and will be used to recall information to the CLI.

## Getting Started
Download the application and run the CLI. 
