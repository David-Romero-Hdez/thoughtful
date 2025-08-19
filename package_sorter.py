def is_bulky(width, height, length):
    volume = width * height * length
    large_dimension = max(width, height, length) >= 150
    large_volume = volume >= 1_000_000
    
    return large_volume or large_dimension


def is_heavy(mass):
    return mass >= 20


def sort(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"