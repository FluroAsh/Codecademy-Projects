class Computer
@@users = {}

  def initialize(username, password)
    @username = username
    @password = password
    @files = {}
    @@users[username] = password
  end

  # CRUD!
  def create(filename)
    @time = Time.now
    @files[filename] = @time
    puts "\"#{filename}\" CREATED BY: \"#{@username}\" @#{@time}"
  end

  def Computer.get_users
    @@users
  end

  def get_files
    puts "#{@username.upcase} LOG: #{@files}"
  end

  # 1. Adds username to the end of @@users, copying last entry
  # 2. Then deletes previous username (@username) from the hash
  def update_name(username)
    @@users[username] = @@users[@username]
    @@users.delete(@username)
    puts "UPDATED \"#{@username}\" >> \"#{username}\" @#{Time.now}"
  end

  def delete_user(username)
    @@users.delete(username)
    puts "DELETED \"#{username}\" @#{Time.now}"
  end

end

puts "[**--ADD-USERS-TEST--**]"
apollo = Computer.new("Apollo", "42069")
sally = Computer.new("Sally", "1552")
john = Computer.new("John", "51155")
puts Computer.get_users # Read
puts ""

puts "[**--CREATE-TEST--**]"
john.create("test.txt")
john.get_files
puts ""
sally.create("test2.txt")
sally.create("test3.txt")
sally.get_files
puts ""

puts "[**--UPDATE-TEST--**]"
john.update_name("Greg")
puts Computer.get_users
puts ""

puts "[**--DELETE-TEST--**]"
john.delete_user("Greg")
puts Computer.get_users
