def describe_pet(pet_name="Harper", animal_type="Cat"):
    """Display imformation about a pet."""
    return "My " + animal_type + "'s name is " + pet_name.title() + "."
print(describe_pet("Harper", "Cat")) 
