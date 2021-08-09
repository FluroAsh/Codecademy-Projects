# The Boredless Tourist
# Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by.

# Declare lists containing destinations and our lucky test traveller!
destinations = ['Paris, France','Shanghai, China','Los Angeles, USA','São Paulo, Brazi','Cairo, Egypt']

test_traveler = ['Erin Wilkes','Shanghai, China', ['historical site','art']]

# Our function to get the index number in the list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Find travelers location based on location index, then assign that index to a new value called traveler_destination_index
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
