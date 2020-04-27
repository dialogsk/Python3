########################################################################
# my frist Programming Laguage in python3
#######################################################################
first_name = input('First Your Name: ')
last_name =  input('Last Your Name: ')
# print('Hello ', first_name + last_name)
print('Hello Buddy, '  + first_name.capitalize() + ' ' + last_name.capitalize())
###########################################################################
# TO USE CURRENT DATE WE NEED ACUALLY TO USE DATETIME LIBARERY
############################################################################
 print( 'Today is: ' +  str(today))
 one_day = timedelta(days=1)
 yesterday = today - one_day
 print('Yesterday was: ' +  str(yesterday))
 one_week = timedelta(weeks=1)
 last_week = today - one_week
 print('lastweek was: ' + str(last_week))
###########################################################################
 #  Using the function of timedelta
#########################################################
from datetime import datetime, timedelta
birthday = input('When is your Birthday: (dd/mm/yyyy ?) ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday,' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve= birthday_date - one_day
print('Day Before may Birthday: ' +  str(birthday_eve))
 #############################################################################
 # intoduction in if else statement
 #############################################################################
race = input('How much did you Pay: ')
race = float(race)
if race >= 1.00:
    tax = .07
else:
    tax = 0
    print('Tax Rate is: '+  str(tax))    
