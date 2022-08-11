
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
conda create -n price-tracker-env
conda activate price-tracker-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Python Packages
This program requires the following python packages to run. These packages are listed in the requirements.txt file.

 + pandas
 + sendgrid==6.6.0
 + python-dotenv
 + beautifulsoup4
 + requests
 + xlsxwriter
 + pytest

## Usage 1: Price scrape and output as excel
By executing the program, the program will collect today's price information and stores onto an xlsx file.
Pass the following command into command line to execute program:

```sh
python monthly_price_tracker.py
```

After executing the py file, an xlsx file named "Internet_pricing_All_YYYY-MM-DD" will be created on the root directory. It will also show a table with the collected price information on the command line.

NOTE: If the program is ran multiple times within the same day, the program will overwrite the previously exported excel file. If you want to keep multiple files from different times within a day, make sure to move the old excel file into a different directory or folder.

## Usage 2: Send excel file to specified recipient
### Setup:
To enable this feature, first create a file named .env on your root directory.
In the .env file, enter the following scripts and populate with required information:

    SENDGRID_API_KEY="---------------YOUR SENDGRID API KEY---------------"
    SENDER_EMAIL_ADDRESS="---------------SENDER EMAIL ADDRESS---------------"
    RECIPIENT_EMAIL_ADDRESS="---------------RECIPIENT EMAIL ADDRESS---------------"

In case you want to send the excel report to multiple emails, separate the addresses with a comma. Example shown below:

    RECIPIENT_EMAIL_ADDRESS="sample.address1@stern.nyu.edu,sample.address2@stern.nyu.edu"

### Program execution:
To execute program, pass the following script into the command line:

```sh
python email_monthly_report.py
```

If program is ran successfully, an email with the excel report attached will be sent from the sender address to the recipient address.

### In case of an error:
If for some reason the program encounters and error (perhaps due to change of URL or html script), the program will send an error notification email to the sender address with error detail included.

## Setup auto-run using Heroku
You can set up auto-run by installing this repo onto a Heroku server, and enable auto-run by using the Heroku scheduler.

To set up, first log into your heroku account by passing the following command from command line (*for Windows user, using Anaconda command or Windows command prompt is recommended):

```sh
heroku login
```

Then create a new remote server by passing the following command:

```sh
heroku create
```

### Configuration for Heroku
Once you've created a new server, you need to set the environmental variables (API key, sender address and recipient address) within the Heroku server. You can do this either from the heroku server settings -> Config Vars, or by passing the information through the command line:

```sh
heroku config:set SENDGRID_API_KEY="---------------YOUR SENDGRID API KEY---------------"
heroku config:set SENDER_EMAIL_ADDRESS="---------------SENDER EMAIL ADDRESS---------------"
heroku config:set RECIPIENT_EMAIL_ADDRESS="---------------RECIPIENT EMAIL ADDRESS---------------"
```

Finally, install the repo onto the heroku server:

```sh
git push heroku main
```

You can use add-in tools such as [Heroku Scheduler](https://dashboard.heroku.com/apps/enigmatic-beach-10029/resources/new?addonService=scheduler) to have the heroku server automatically execute the program.

## Limitations
This program is designed to work specifically for the URLs within the py files (12 product pages from the 3 listed webisites) and does not have the flexibility to collect price information from other websites.