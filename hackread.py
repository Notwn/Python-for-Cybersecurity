#get the file
file_name= "hackme.txt"
#reading the file
with open(file_name, 'r') as file:
          #printing the introduction message
          print("Here is someone to hack - information! ")
          #reading the contents of the file
          content = file.read()
          #print file contents
          print(content)