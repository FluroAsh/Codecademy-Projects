# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

# To keep track of the kinds of pizzas you sell, create a list called toppings
toppings = [["Pepperoni"], ["Pineapple"], ["Cheese"], ["Sausage"], ["Olives"], ["Anchovies"], ["Mushrooms"]]

# To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out
num_two_dollar_slices = prices.count(2)

# ind the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)

# Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
print("We sell", num_pizzas, "different kinds of pizza! \n")

# Convert our toppings and prices lists into a two-dimensional list called pizza_and_prices that has the following associated values. 
pizza_and_prices = [[2, "Pepperoni"], [6, "Pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "Olives"], [7, "Anchovies"], [2, "Mushrooms"]]
# Print pizza_and_prices. 
print(pizza_and_prices, "\n")

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending). 
pizza_and_prices.sort()
print(pizza_and_prices, "\n")

# Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza, "\n")

# Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza, "\n")

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop(-1)
print(pizza_and_prices, "\n")

# Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings.
pizza_and_prices.insert(4, [2.5, "Peppers"])
print(pizza_and_prices, "\n")

# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest. 
' The colon comes FIRST, so it selects the FIRST 3.
' If the colon came LAST, then it would select the LAST 3.
three_cheapest = pizza_and_prices[:3] 
print(three_cheapest, "\n")
