def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        support = "packets available"
    elif unit == "grams":
        support = "grams total"
    elif unit == "area":
        support =  "square meters"
        print(seed_type.capitalize(),"seeds: covers",quantity,support)
        return
    else:
        support = "Unknown unit type"
    print(seed_type.capitalize(),"seeds:",quantity,support)
