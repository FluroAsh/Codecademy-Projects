letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creates lowercase letters in our letters list, and then doubles points in our points list to create values for our new lowercase letters
letters += [letter.lower() for letter in letters] 
points *= 2  

# Zip our lists together & then using a list comprehension map the letters to their point values
zipped_letters_points = zip(letters, points)
letters_to_points = {key:value for key, value in zip(letters, points)}

# Create new '' value that represents a 0 in 'letters_to_points'
letters_to_points[''] = 0

print(letters_to_points, '\n')

# Words passed through this function; .get utilised to match the 'char' in our word, and return the value -- default value being '0' if there is no match. Returns 'point_total'
def score_word(word):
  point_total = 0
  for char in word:
    char_points = letters_to_points.get(char, 0)
    point_total += char_points
  return point_total

brownie_points = score_word('BROWNIE')

# Creates a dictionary for 'players' and their 'word' choices. 
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}

# Function to take in the keys and values from 'player_to_words', add the totals based on the point values and allocate them to our dictionary 'player_to_points' respective of each player
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()
print(player_to_points, '\n')

# Simple function to add words to our player_to_words list using 2 variables: 'player' & 'word'
def play_words(player, word):
  player_to_words[player].append(word)

play_words('player1', 'HELLO')
print(player_to_words)
