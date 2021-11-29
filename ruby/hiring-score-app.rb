def get_input
  system("clear")
  
  puts "--------------------------------------------------------------"
  puts "| Python | Ruby | Bash | Git | HTML | TDD | CSS | JavaScript |"
  puts "--------------------------------------------------------------"
  puts "What are your skills?: "
  puts "-- For multiple choices, seperate with a space"
  print ">> "
  input = gets.chomp.downcase
  input = input.split(/\s+/) if input =~ /\s/ # Returns separated strings (" ")
  puts "--------------------------------------------------------------"
  return input
end

skill_weighting = {
  python: 1,
  ruby: 2,
  bash: 4,
  git: 8,
  html: 16,
  tdd: 32,
  css: 64,
  javascript: 128
}

score = 0
selected_skills = [] # Holds user input

temp_skills = get_input() # If array is being returned, appending the whole array

system("clear")

# Validates user input
if temp_skills[0].length > 1
  # If user input contains multiple strings within an array
  # Maps to selected_skills
  selected_skills = temp_skills.map { |a| a.to_sym } 
else
  # Else, adds single value to the array
  selected_skills.push(temp_skills.to_sym)
end
puts "--------------------------------------------------------------"

# Validates whether user has entered any invalid strings
# If not, calculates sum of their choices based on values from skill_weighting hash
selected_skills.each do |a|
    if skill_weighting.key?(a)
      score += skill_weighting[a] 
    else
      puts "⚠ \"#{a}\" is not a valid choice, try again. "
      exit
    end
end

# Iterates through selected_skills
# Prints users selection(s) with correct formatting
selected = ""
print "It looks like you only selected:"
selected_skills.each do |a|
  selected += "#{a.capitalize}, "
end
puts " #{selected.chomp(", ")}."

puts 
puts "-- To improve your score you could learn: "
# Creates array of keys from skill_weighting 
# Then fetches the score values based on difference from selected_skills
weight_keys = [] 
skill_weighting.each_key { |k| weight_keys.push(k) }
difference = weight_keys.difference(selected_skills) 

# Prints out the difference in keys, and score value
difference.each { |k, v| print "  * #{k}: (#{skill_weighting[k]} points) \n" }  

puts
puts "Your total score is: #{score} points!"
puts "--------------------------------------------------------------"
