# LTO Price Tracker

This program collects price information of LTO Ultrium products (gen 7, 8 and 9) for 4 brands (Fujifilm, IBM, HPE and Quantum) from 3 major e-commerce stores (listed below).

 + https://www.backupworks.com/
 + https://www.tape4backup.com/
 + https://tapeandmedia.com/

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
Collects today's price info and stores onto xlsx file.
Pass the following command into command line to execute.

```sh
python monthly_price_tracker.py
```

After executing the py file, an xlsx file named "Internet_pricing_All_YYYY-MM-DD" will be created on the root directory. It will also show a table with the collected price information on the command line.

