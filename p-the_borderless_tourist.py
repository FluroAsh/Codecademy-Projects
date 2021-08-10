'''This is the foundation for how apps like Uber, Yelp & other similiar services work. 
Great example of how multiple functions form the basis for a users experience. But this
is only the beginning, as this is not what the user SEES!'''

# -- Setting Up... --
# Declare lists containing destinations and our lucky test traveller!
destinations = ['Paris, France','Shanghai, China','Los Angeles, USA','São Paulo, Brazi','Cairo, Egypt']

test_traveler = ['Erin Wilkes','Shanghai, China', ['historical site','art']]

# Our function to get the index number in the list.
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# -- Travelling To Faraway Lands! -- 
# Find travelers location based on location index, then assign that 
# index to a new value called traveler_destination_index.
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# -- Visiting Interesting Places! -- 
# Loop Comprehension creates an empty attraction list for every list 
# in destinations inside the initial attractions list.
attractions = [] 
for destination in destinations:
    attractions.append([])

print(attractions)

'''Can also use (1 line):
attractions = [[] for destination in destinations]'''

# Gets the destination index and appends the attraction to the 
# location of that index to our new list. Exit function if there's a ValueError.
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    return
  except ValueError:
    return

# Add attractions to our attractions list!
add_attraction('Los Angeles, USA', ['Venice Beach',['Beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

# -- Finding the BEST places to go! -- 
# Function to validate whether we have called a valid destination & attraction.
# Checks to see whether the interest matches the tag passed into the function based
# on what is stored in the attraction list. 
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

# -- See The Parts of a City You want to See! -- 
# Runs through our other functions and prints recommendations for our traveler
# based on their interests. Performs a check on this using an if loop for each element
# in the traveler_attractions list.
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places around " + traveler[1] + ': ' 
  # This loop checks to see if the last element in the list matches the first index[0]
  # if it does then it adds the value and "." as there is only one value. 
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the " + traveler_attractions[i] + "."
  # Self explanatory, more than one value, will add all the values with a comma.   
    else: 
      interests_string += "the " + traveler_attractions[i] + ","
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

# Program as a whole does not handle multiple tags PERFECTLY. Further improvements can be made. 
