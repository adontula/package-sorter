import argparse

BULKY_VOLUME_LIMIT=1000000 # cm^3
BULKY_DIMENSION_LIMIT=150 # cm
HEAVY_LIMIT=20 # kg

def calculate_volume(width, length, height) -> float:
    return width * length * height

def sort(width:float, length:float, height:float, mass:float) -> str:
    # Validate input args
    try:
        # First verify all inputs are numeric
        width = float(width)
        length = float(length)
        height = float(height)
        mass = float(mass)

        # Then verify all inputs are positive - we can't have negative/zero dimensions or mass
        if width <= 0 or length <= 0 or height <= 0 or mass <= 0:
            raise ValueError
    except ValueError as e:
        raise ValueError(f"Invalid input. Please enter positive numbers for width, length, height and mass. Your inputs were as follows:\n\
                         width:{width} of type:{type(width)}\n\
                         length:{length} of type:{type(length)}\n\
                         height:{height} of type:{type(height)}\n\
                         mass:{mass} of type:{type(mass)}") from e


    volume = calculate_volume(width, length, height)

    bulky = volume >= BULKY_VOLUME_LIMIT or width >= BULKY_DIMENSION_LIMIT or length >= BULKY_DIMENSION_LIMIT or height >= BULKY_DIMENSION_LIMIT
    
    heavy = mass >= HEAVY_LIMIT
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort package based on mass and volume")
    parser.add_argument("width", type=float, help="Width of package in cm")
    parser.add_argument("length", type=float, help="Length of package in cm")
    parser.add_argument("height", type=float, help="Height of package in cm")
    parser.add_argument("mass", type=float, help="Mass of package in kg")

    args = parser.parse_args()

    print(sort(args.width, args.length, args.height, args.mass))
