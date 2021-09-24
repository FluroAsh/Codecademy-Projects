from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# -- CREATE THE STACKS
stacks = [] 
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# Now our stacks are all in our 'stacks' list!
stacks += [left_stack, middle_stack, right_stack]

# -- SET UP THE GAME
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

# -- GET USER INPUT
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True: # Always true until we return a valid condition
    for i in range(len(stacks)): # 'i' = Every stack in stacks
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    
    user_input = input("").upper()

    # Returns "Left, Middle or Right" if valid
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i] # Exit with our return statement
        
# -- PLAY THE GAME
num_user_moves = 0

# All disks should be on our right stack for the player to win!
while right_stack.get_size() != num_disks: # 'Main loop'
  
  print("\n\n\n...Current Stacks...") 
  for stack in stacks:
    stack.print_items()

  while True: 
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.is_empty(): 
      print("\n\nInvalid Move. Try Again")    
    elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again (Else)")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
