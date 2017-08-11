# Log Analysis 
Made by Lyn Scott with Python 3.6, Vagrant 1.9.7 and VirtualBox 5.1.26.

## Intro
This code is designed to connect to the database, query for your desired information, return it and close the connection.

##### Requirements:

  - [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
  - [Install Vagrant](https://www.vagrantup.com/downloads.html)
  - [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - Download the `newsdb.py` file, available [here](https://github.com/lynscott/Log-Analysis/blob/master/news/newsdb.py).
  
##### Setup:
  - Download the VM Configuration: [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
  - Place the _newsdb.py_ and the _newsdata.sql_ file in the \FSND-Virtual-Machine\vagrant directory.
  - In your terminal change into your vagrant directory, run `vagrant up` to start your VM.
  - Enter `vagrant ssh` to enter your VM's terminal. To load the data, use the command `psql -d news -f newsdata.sql`.
  - Lastly, enter `python newsdb.py` to run the file.
 
