# Ask your users to list a bunch of information about them: things they like,
# things they hate, names of family and friends... it's up to you how
# many and what kinds of things you pick. Keep it wacky!


# Define a function to get user input for things they like
def get_likes():
    return input("What are some things you like? ")


# Define a function to get user input for things they hate
def get_hates():
    return input("What are some things you hate? ")


# Define a function to get user input for family member names
def get_family_names():
    return input("What are the names of your family members? ")


# Define a function to get user input for friend names
def get_friend_names():
    return input("What are the names of your friends? ")


# Define a function to construct the story using the input variables
def construct_story(likes, hates, family_names, friend_names):
    story = f"Once upon a time, there was a person who liked {likes} but absolutely hated {hates}. "
    story += (
        f"They had a big family, including members with names like {family_names}. "
    )
    story += f"They also had many friends, with names like {friend_names}. "
    story += (
        "One day, something unexpected happened and their life turned upside down. "
    )
    story += "They had to rely on their likes, dislikes, family, and friends to overcome the challenges and find a happy ending. "
    story += "And they lived happily ever after."
    return story


# Call the functions to get the user inputs
likes = get_likes()
hates = get_hates()
family_names = get_family_names()
friend_names = get_friend_names()

# Call the construct_story function and print the result
story = construct_story(likes, hates, family_names, friend_names)
print(story)
