from datetime import datetime, time
current_time = datetime.now()

print(f'Date & Time: {current_time}\n')

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time.strftime('%I:%M%p')
    self.end_time = end_time.strftime('%I:%M%p')

  def __repr__(self):
    return (f'The {self.name} menu is available between {self.start_time} & {self.end_time}\n')

    def calculate_bill(self, purchased_items):
      pass

# Objects to be passed into our class. Using 24 hour time to distinguish between AM/PM when it is passed. 
brunch = Menu("Brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, time(11), time(16))

early_bird = Menu("Early Bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }, time(16), time(18))

dinner = Menu("Dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }, time(17), time(23))

kids = Menu("Kid's",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }, time(11), time(21))


###--- TBC ---###
|
|
|
###-----------###

# Test Code
print(brunch)
print(early_bird)
print(dinner)
print(kids)
