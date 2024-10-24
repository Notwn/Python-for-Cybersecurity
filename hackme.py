#create a function to collect user information
def create_user_info():
    user_info = {
        "name": input("What is your name? "),
        "favorite_color": input("What is your favorite color? "),
        "first_pet_name": input("What was your first pet's name? "),
        "mother_maiden_name": input("What is your mother's maiden name? "),
        "elementary_school": input("What elementary school did you attend? ")
    }
    return user_info

#Saving user information to a file by creating a function
def save_user_info(user_info):
    with open("hackme.txt", "w") as file:
        for key, value in user_info.items():
            file.write(f"{key.upper().replace('_', ' ')}: {value.capitalize()}\n")

# Main program
def main():
    user_info = create_user_info()
    save_user_info(user_info)

if __name__ == "__main__":
    main()