# Problem discription
# Santa is navigating through a building by following a set of parentheses:
# '(' means go up one floor, ')' means go down one floor.
 """
    Part 1:
    Takes a string of parentheses and returns the final floor level.
    '(' increases the floor by 1, ')' decreases the floor by 1.
    """

def finding_final_floor(filename: str) -> int:
   
    floor = 0  # Start at ground floor (0)
    for c in filename:
        if c == ")":
            floor -= 1  # Move down a floor
        elif c == "(":
            floor += 1  # Move up a floor
    return floor  # Final floor after all instructions

  """
    Part 2:
    Returns the position (1-based index) where Santa first enters the basement (floor -1).
  """
def finding_basement(filename: str) -> int:
  
    floor = 0  # Start at ground floor
    for i, c in enumerate(filename, start=1):  # Use 1-based index as required
        if c == ")":
            floor -= 1
        elif c == "(":
            floor += 1
        if floor == -1:
            return i  # First position where Santa reaches the basement
    return -1  # If basement is never reached

# Read the input from file
with open("input.txt") as file:
    content = file.read().strip()  # Read the whole content and strip any trailing newlines/spaces
