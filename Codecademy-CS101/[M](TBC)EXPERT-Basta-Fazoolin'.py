'''Type Error with datetime and str on line 23... TBC'''

from datetime import datetime, time
import pytz

tz_au = pytz.timezone('Australia/Melbourne') 
datetime_au = datetime.now(tz_au)
print('\t\tMelbourne Time:', datetime_au.strftime('%I:%M%p'), '\n')

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return (f'The address is: {self.address}\n')

  # Returns a list of available menu's by testing if it falls in our window of
  # time for any given menu
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time: 
        available_menus.append(menu) # Because it's a list, use .append()!
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time.strftime('%I:%M%p')
    self.end_time = end_time.strftime('%I:%M%p')

  def __repr__(self):
    return (f'The {self.name} menu is available between {self.start_time} & {self.end_time}\n')

# Check if purchased_items exists in self.items. Add to the bill if found in 
# 'brunch/dinnner' etc. using it as the key to find our values
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# Objects to be passed into our class. Utilizes 24 hour time to get AM/PM.
# Brunch Menu 
brunch = Menu('Brunch',{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }, time(11), time(16))

# Early Bird Menu 
early_bird = Menu('Early Bird',{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }, time(16), time(18))

# Dinner Menu 
dinner = Menu('Dinner',{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }, time(17), time(23))

# Kids Menu 
kids = Menu('Kid\'s',{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }, time(11), time(21))

# List to hold the collection of dictionaries that belong to our menus
menus = [brunch, early_bird, dinner, kids]

# Flagship Store
flagship_store = Franchise('1232 West End Road', menus)

# New Installment Store
new_installment = Franchise('12 East Mulberry Street', menus)

# Test Code
print(brunch)
print(early_bird)
print(dinner)
print(kids)

print('Bill Total: $' + str(brunch.calculate_bill(
  ['pancakes', 'home fries', 'coffee'])))
print('Bill Total: $' + str(early_bird.calculate_bill(
  ['salumeria plate', 'mushroom ravioli (vegan)'])) + '\n')

#print(flagship_store)
print(flagship_store.available_menus((12)))
