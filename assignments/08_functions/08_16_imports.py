#
#
# 
 
import fav_book
# this will import the module from another file  

from fav_book import display_message
# imports a specific function 

from fav_book import display_message as fb
# imports a specific function and creates a nickname for it as to not confuse it with another

import fav_book as fb
# imports a module and makes a nickname for it as to not confuse it with another

from fav_book import*
#imports every function from a module 

print(fav_book.favorite_book("Book of Stuff"))