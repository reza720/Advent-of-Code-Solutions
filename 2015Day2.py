"""Part One: Wrapping Paper Calculation
Each present is a box in the format LxWxH (length, width, height).
You need to calculate how much wrapping paper is needed for each box.
Formula:
Surface area = 2*l*w + 2*w*h + 2*h*l
Extra slack = area of the smallest side
Total = surface area + slack
"""
def calculate_total_paper(filename):
    total_paper = 0 

    with open(filename, encoding='utf-8-sig') as file:
        for line in file:
            l, w, h= list(map(int,line.strip().split('x')))

            surface_area = 2 * l * w + 2 * w * h + 2 * h * l
            side_areas = [l * w, w * h, h * l]
            slack = min(side_areas)
            total_paper += surface_area + slack 
    
    return total_paper

"""Part Two: Ribbon Calculation
Formula for Ribbon required: Smallest perimeter of any one face (smallest two sides): 2*(a + b) Plus ribbon for the bow: volume = l*w*h
Total = perimeter + volume"""
def total_ribbon_required(filename: str)->int:
    total_ribbon = 0
    with open (filename,  encoding='utf-8-sig') as file:
        for line in file:
            l,w,h=list(map(int,line.strip().split("x")))
            
            sides=sorted([l,w,h])
            perimeter = 2 * (sides[0] + sides[1])
            volume = l * w * h
            total_ribbon += perimeter + volume
    
    return total_ribbon

