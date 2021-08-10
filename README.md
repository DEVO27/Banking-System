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
* [Layout](#Layout)
  * [Main Menu](#Main-Menu)
  * [Account Menu](#Account-Menu)
  

## Luhn algorithm
- The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is a widely known 
mathematical formula used to validate the authenticity of identification 
numbers of our generated credit card numbers. This program implements this algorithm to 
authenticate its generated card numbers. The first six digits in the program 
known as the MII or (Major Industry Identifier) will always start with 400000. 
The proceeding numbers are randomly generated along with the corresponding PIN 
cardmember. The pin is a randomly generated card number from 0000 to 9999.

## SQLite
As stated beforehand this program uses sqlite3 for its database configuration.The database 
is created once the program has started. Query requests will be reflected from the user input. All 
data will be stored in this manner and will be used to recall information to the CLI.
Below is the structure of table ``card`` from the database:
  - id number
  - card number
  - pin
  - balance

## Getting Started
Download the application from [bankingapp](bankingsystem.py) and run it in the terminal. 
```
python bankingsystem.py
````
## Layout
At the start of the program, you are given presented to the main menu
  ### Main Menu
```
1. Create an account
2. Log into account
0. Exit
```
  - **1. Create an account:** would produce a randomly generated 16 digits card number beginning 4000000xxxxxxxxx and is its associated four-digit pin. There is no limit as to how many cards you wish to generate. 
  ```
  Your card has been created
  Your card number:
  4000003184705263
  Your card PIN:
  6234
  ```
 - **2. Log into account:**  would produce user sign-in of their newly created card. 
 ```
 Enter your card number:
 4000002846503173
 Enter your PIN:
 7480
 You have successfully logged in!
 ```
 - If incorrect input ``Wrong card number or PIN``
 ### Account Menu
 ```
1. Balance
2. Add funds
3. Do transfer
4. Close account
5. Log out
0. Exit
```
- **1. Balance:** will display the current balance in the account. All balances are set to 0 by default.
```
Balance: 0
```
- ``2. Add funds`` deposit funds into the current working account.
```
Enter deposited amount:
1000
```
– Adding a new amount is based on **sign**. The action can be a withdrawl or deposit. 
```
Balance = 100
Enter deposited amount:
12
Balance = 112
```

- **3. Do transfer:** transfers funds to another credit card from the current working card on file. The card entered must be of a valid length and pass the Luhn algorithm test.
 ```
 Enter card number:
 4000003184705263
 Enter how much money you want to transfer:
 75

Success!
 ```
 This feature supports multiple errors handling conditions such as:<br />
– The amount deposited can not come from the same credit card the user is currently using.<br />
– The entered card number must be within the database and pass the Luhn algorithm test <br />
– Transfer requestion can not exceed the user current balance

- **4. Close account:** The current card will be removed from the database and the session will end. This will return to the [main menu](#Main-Menu). 
```
The Account has been closed!
```
- **5. Log out** The card will be logged out from the account and return to the [main menu](#Main-Menu)
- **0. Exit** This will end the program
