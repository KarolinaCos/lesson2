import ephem
def give_me_planets:
    list_planet_all = ephem._libastro.builtin_planets()
    list_planet_only = []
    for p_tuple in list_planet_all:
        if p_tuple[1] == "Planet":
            list_planet_only.append(p_tuple[2]) 
    return list_planet_only     







