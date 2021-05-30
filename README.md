# covid_info_search

## Prerequisite Software
* Python 3.x

## Build Steps on local server 
* Install flask, pandas python packages using pip
  ```
  pip install flask
  pip install pandas
  ```
* Run the app.py file to access the web app in port 5000
  ```
  python app.py
  ```


## Temporary hosting using pagekite 

> app.py file must be run first before executing the below steps 

* Download the pagekite.py file using the below command 
  ```
  curl -O https://pagekite.net/pk/pagekite.py
  ```
* Execute the pagekite.py file by providing the information to access the website over internet
  ```
  python pagekite.py 5000 yoursitename.pagekite.me
  ```
  
