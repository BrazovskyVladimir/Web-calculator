# Web-calculator

A simple calculator service implemented using the flask framework. Service has one method GET. 
This method passes a string with the formula to be calculated as the expr parameter.

## Usage:
```python
python main.py
```

## Example of using the site

The main page of the site 1:

<img src="https://github.com/SnezhanaM/Web-calculator/blob/master/pictures/main_page.png" width="600" height="250"/>

Next, you need to enter in the URL bar ?expr= a formula for calculating using the urlencode characters. 
The example shows the expression: 5*(200+50)/10. http://calc-diplom.local/?expr=5%2A%28200%2B50%29%2F10

<img src="https://github.com/SnezhanaM/Web-calculator/blob/master/pictures/input.png" width="600" height="250"/>

After pressing "Enter", the result is displayed on the screen.

<img src="https://github.com/SnezhanaM/Web-calculator/blob/master/pictures/result.png" width="600" height="250"/>
