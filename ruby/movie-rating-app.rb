## METHODS
# Method to check if our string contains spaces
# If it does, return new string replaced with '_'s
def get_input
  title = gets.chomp
  title = title.gsub!(/\s+/, '_') if title =~ /\s/
  title.downcase.to_sym
end
## 

# Rating out of 10
movies = {
  interstellar: 9,
  the_joker: 8
}

menu = true

while menu
puts "Please select an option:"
puts "-- Type (1) to add a movie." 
puts "-- Type (2) to update a movie." 
puts "-- Type (3) to display all movies." 
puts "-- Type (4) to delete a movie." 
puts "-- Type (5) to exit." 
choice = gets.chomp.to_i

  case choice
  when 1 # Add Movie
    system("clear") 
    puts "Please enter a title:"
    # Get & convert input to correct format 
    # (symbol & any spaces replaced with '_'s)
    title = get_input()

    if movies[title] == nil 
      puts "Please enter a rating:"
      rating = gets.chomp.to_i
      movies[title] = rating
      puts "Movie & rating added!" 
      puts "-- New record: {#{title}: #{movies[title]}}"
      puts
    else
      puts "#{title} already exists!"
      puts
    end

  when 2 # Update Movie
    system("clear") 
    puts "Which movie would you like to update?:"
    title = get_input()
    
    if movies[title] == nil
      puts "#{title} is not in our records!"
      puts
    else 
      # If the title (key) exists, update rating
      if movies.has_key?(title) 
        puts "Please enter a NEW rating:"
        rating = gets.chomp.to_i
        movies[title] = rating
        
        puts "Movie record updated!"
        puts "-- New record: {#{title}: #{movies[title]}}"
        puts
      else 
        puts "ERROR: #{title} does not exist!"
        puts
      end
    end

  when 3 # Display Movies
    system("clear")
    if movies.length > 0
      puts "--------------------"
      movies.each do |k, v| # Loop & print k:v pairs
        puts "[TITLE]: #{k}"
        puts "[RATING]: #{v}"
        puts "--------------------" 
      end
    else
      puts "ERROR: There are no records!"
      puts
    end

  when 4 # Delete Movie
    system("clear")
    puts "Which movie would you like to delete?:"
    title = get_input()
    
    if movies[title] == nil
      puts "ERROR: #{title} is not in our records!"
    else
      movies.delete(title)
      puts "\"#{title}\" record deleted!"
      puts
    end
  
  when 5 # Exit the loop
    system("clear")
    menu = false
    puts "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    puts "~~ Thanks for dropping in! :) ~~"
    puts "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

  else # None of the above valid
    system("clear")
    puts "ERROR: Did not select a valid choice! [1, 2, 3 or 4]"
  end
end
