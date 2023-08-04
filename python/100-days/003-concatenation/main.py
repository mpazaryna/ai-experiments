def get_user_input(prompt):
    user_input = input(prompt)
    return user_input


def generate_recipe():
    food = get_user_input("Name a food: ")
    plant = get_user_input("Name a plant: ")
    cooking_method = get_user_input("Name a cooking method: ")
    burned_food = get_user_input("Describe a burnt food: ")
    household_item = get_user_input("Name a household item: ")

    recipe = f"{cooking_method} {food} with burned {plant} on a bed of {household_item}"
    return recipe


def main():
    print("=== Recipe ===")
    recipe = generate_recipe()
    print(recipe)


if __name__ == "__main__":
    main()
