# Change Engine  APi :moneybag: :pound:

ChangeEngine functionality - use the API to manage change in your vending machine:

- Initialise the vending machine to a known state (which coin, and how many)
- Register coins that have been deposited by a user.
- Return the correct change to a user as coins when an order is received and remove the coins from the
machine
#
Table of Contents:
- [Change Engine  APi :moneybag: :pound:](#change-engine--api-moneybag-pound)
- [Check out functionality](#check-out-functionality)
  - [Setup](#setup)
  - [Configuration:](#configuration)
  - [Run](#run)
  - [How to interact with it?](#how-to-interact-with-it)
  - [Exitting program](#exitting-program)
- [Reference:](#reference)
    - [Files included](#files-included)
- [Change engine API Reference](#change-engine-api-reference)
    - [Methods](#methods)
    - [<ins>\__init__(**init_coins**)</ins>](#ins_init_init_coinsins)
    - [<ins>return_change(**product_price**)</ins>](#insreturn_changeproduct_priceins)
    - [<ins>insert_coin(**coin**)</ins>](#insinsert_coincoinins)
    - [<ins>get_user_balance()</ins>](#insget_user_balanceins)
    - [<ins>get_coins_status()</ins>](#insget_coins_statusins)
    - [<ins>get_coins_denomination()</ins>](#insget_coins_denominationins)
  - [Change object](#change-object)
    - [Methods](#methods-1)
    - [<ins>\__init__(change)</ins>](#ins_init_changeins)
    - [<ins>get_total()</ins>](#insget_totalins)
    - [<ins>get_change()</ins>](#insget_changeins)

# Check out functionality

[**main.py**](./main.py) - is a file holding a simple test program that utilise API and imitates a vending machine funcionality.

## Setup

The program was run on:
- Windows 11, Python 3.10.8
- Oracle Linux 7.9, Python 3.6.8

If you do not have Python installed on the machine, please download it from [here](https://www.python.org/downloads/). You will not need any additional python libraries.

## Configuration:

[config.py](./config.py) -  holds your configuration for initial coins in the machine and Vending machine products offering. The initial denomination of coins can not be changed, only the amount. You can also add or delete items from the `menu`; however, follow the existing syntax.

## Run

To run the program, open terminal window change the directory to the folder where [**main.py**](./main.py) resides and type:

**SIDE NOTE: For the best experience, please maximise your terminal window**

```bash
python3 main.py
```
or

```bash
python main.py
```

If your setup is correct, upon running the test program, you should see the following:

```bash
Welcome to the vending machine
Please select a product from the list:

 ________________________________________________ 
| Number: 1 | Name: Apple juice  | Price: 1      |
| Number: 2 | Name: Orange juice | Price: 1.2    |
| Number: 3 | Name: Pepsi        | Price: 1.51   |
| Number: 4 | Name: Fanta        | Price: 1.5    |
| Number: 5 | Name: RedBull      | Price: 2      |
| Number: 6 | Name: Monster      | Price: 3      |
 ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ 

Please select a number:
```

## How to interact with it?

The program will respond to the keyboard input,
follow instructions on the command line.

## Exitting program

The program runs continuously. To exit the program, either press `ctr + C` or kill the terminal


# Reference:

### Files included

| File        | Description           | 
| ------------- |:-------------:        | 
|[ChangeEngine.py](./api/ChangeEngine.py)| API logic  | 
|[Change.py](./api/Change.py)| Helper class to represent a money change  | 
|[Statics.py](./api/Statics.py)| Holds allowed coins denomination | 
|[config.py](./config.py)| Holds setup for initial coins in the machine and products available  | 
|[main.py](./main.py)| Program to test the API  | 

# Change engine API Reference

### Methods

| Method        | Description           | 
| ------------- |:-------------:        | 
| [\__init__(init_coins)](#_init_init_coins)      | Creates a new `ChangeEngine` client | 
| [return_change(*product_price*)](#return_changeproduct_price)      | Calculates and returnes change for customer      |
| [insert_coin(*coin*)](#insert_coincoin) | Takes customer deposit      |
| [get_user_balance()](#get_user_balance) | Returns balance deposited by the customer      |
| [get_coins_status()](#get_coins_status) | Returns coins available in the machine      |
| [get_coins_denomination()](#get_coins_status) | Returns available coins allowed denomination      |

### <ins>\__init__(**init_coins**)</ins>
Creates a new *ChangeEngine* client

**Parameters**:

`init_coins(dict)` - It will initialise the number of coins in a machine. You must provide the amount for each coin stated in the [static file](./api/Statics.py) e.g.:

```python
initial_coins = {
                  2: 100,
                  1: 100,
                  0.5: 100,
                  0.2: 100,
                  0.1: 100,
                  0.05: 100,
                  0.02: 100,
                  0.01: 100
                }
```

### <ins>return_change(**product_price**)</ins>

Calculates and returnes change for a customer

**Parameters**:

`product_price(float)` - Product price must be a float or an int. The argument will be rejected if negative or greater than the user deposit.

**Returns**:

A`List` consisting of a [Change](./api/Change.py) object and bool value. The bool value is `True` if the change will be given. If `False`, this will indicate that there were not enough coins to return accurate change; hence, the Change object consists of the amount the user deposited. 



###  <ins>insert_coin(**coin**)</ins>

Takes customer deposit

**Parameters**:

`coin(float)` - a coin must be a float or an int. The argument will be rejected if it is not a value of British currency coins [reflected here.](./api/Statics.py) 

**Returns**: `None`

###  <ins>get_user_balance()</ins>

Returns balance deposited by the customer

**Parameters**: `None`

**Returns**: `float`

###  <ins>get_coins_status()</ins>

Returns coins available in the machine

**Parameters**: `None`

**Returns**: `dict`

###  <ins>get_coins_denomination()</ins>

Returns coins denomination allowed to use 

**Parameters**: `None`

**Returns**: `list`



## Change object

[class Change](./api/Change.py) - It creates an object which holds the total value of customer change. In addition, it stores information about specific coin distribution. ChangeEngine initialises the object. It is not designed to be created manually.  

### Methods

| Method        | Description           | 
| ------------- |:-------------:        | 
| [\__init__(change)](#_init_change)      | Creates a new `Change` instance | 
| [get_total()](#get_total)     | Returns value of customer change      |
| [get_change()](#get_change) | Returns customer change coin distribution     |

### <ins>\__init__(change)</ins>
Creates a new *Change* object

**Parameters**:

`change(dict)` - The dictionary reflects coin distribution in a customer change. The `key` would be a coin nominal, e.g. 0.2 and `value` is the number of coins in a change.

###  <ins>get_total()</ins>

Returns value of customer change

**Parameters**: `None`

**Returns**: `float`

###  <ins>get_change()</ins>

Returns customer change coin distribution

**Parameters**: `None`

**Returns**: `dict`




