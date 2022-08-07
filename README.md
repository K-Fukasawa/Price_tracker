# Price_tracker

Collects price information of LTO Ultrium products (gen 7, 8 and 9) for 4 brands (Fujifilm, IBM, HPE and Quantum) from 5 major e-commerce stores (listed below).

https://www.amazon.com/
https://www.backupworks.com/
https://www.connection.com/
https://www.tape4backup.com/
https://tapeandmedia.com/


## Installation
Create a copy of this [repo](https://github.com/K-Fukasawa/Price_tracker), then clone your new repo onto your local computer by using tools such as GitHub Desktop, and navigate there from the command-line:

```sh
cd ~/Documents/GitHub/Price_tracker/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "price-tracker-env":

```sh
conda create -n price-tracker-env python=3.8
conda activate price-tracker-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration
Chromedriver



Sendgrid API



## Usage
Collect today's price info and store onto csv file:

```sh
python price_tracker.py
```
