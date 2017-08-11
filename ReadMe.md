# Log Analysis 
Made by Lyn Scott with Python 3.6, Vagrant 1.9.7 and VirtualBox 5.1.26.

## Intro
This code is designed to connect to the PostGre SQL database for a fictional news website. 
The news db holds information on: articles, authors, and a log of the news website's activity with visits, links, and HTTP responses.
This code will query the db for the answer to three questions:
- What are the top three articles and how many views do they have?
- Who are the most popular authors and how many views do their articles have?
- On what days did more than 1% of requests lead to errors?

##### Requirements:

  - [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
  - [Install Vagrant](https://www.vagrantup.com/downloads.html)
  - [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - Download the `newsdb.py` file, available [here](https://github.com/lynscott/Log-Analysis/blob/master/news/newsdb.py)
  - Download the VM Configuration: [here](https://github.com/lynscott/Log-Analysis/blob/master/news/VagrantFile)
  
##### Setup:
  - Unzip newsdata.zip to extract the _newsdata.sql_ file. 
  - Place the _newsdb.py_, _newsdata.sql_ and _VagrantFile_ in the same directory. Call it vagrant.
  - In your terminal, change into your vagrant directory, run `vagrant up` to start your VM.
  - Enter `vagrant ssh` to enter your VM's terminal. Then load the news sites data with the command: `psql -d news -f newsdata.sql`.
  - Lastly, enter `./newsdb.py` to run the file on mac/linux, `python3 newsdb.py` to run the file on windows.
    - _Note: if you are using python version < 3 enter `python` instead of `python3`_. 
 
