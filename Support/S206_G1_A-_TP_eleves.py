#========#
# Import #
#========#
import matplotlib.pyplot as plt


#===========#
# Constants #
#===========#
BASIS_WIDTH = 2
BASIS_1_COLOR = 'b'
BASIS_2_COLOR = 'r'

POINT_MARKER = 'o'
POINT_SIZE = 6
POINT_COLOR = 'g'

SEGMENT_COLOR = 'c'
SEGMENT_WIDTH = 2


#===========#
# Utilities #
#===========#
def resizeAxis():
    plt.axis("equal")
    plt.axis([-9, 9, -9, 9])
    
def drawGrid():
    plt.grid()

def drawBasisVectors():
    points = (3.5, -2), (-3.5, -2), (1, 0), (0, 1)
    origin = (0, 0)
    plt.plot(*zip(points[0], origin), linewidth=BASIS_WIDTH, color=BASIS_2_COLOR)
    plt.plot(*zip(points[1], origin), linewidth=BASIS_WIDTH, color=BASIS_2_COLOR)
    plt.plot(*zip(points[2], origin), linewidth=BASIS_WIDTH, color=BASIS_1_COLOR)
    plt.plot(*zip(points[3], origin), linewidth=BASIS_WIDTH, color=BASIS_1_COLOR)

def initialization():
    resizeAxis()
    drawGrid()
    drawBasisVectors()

def drawPoint(point):
    plt.plot(*zip(point), marker=POINT_MARKER, markersize=POINT_SIZE, color=POINT_COLOR)

def drawLine(p1, p2, style=None):
    plt.plot(*zip(p1, p2), linestyle=style, linewidth=SEGMENT_WIDTH, color=SEGMENT_COLOR)

def drawFigure(*points):
    if len(points) != 7:
        print(f"An isometric cube has 7 points, {len(points)} given")
        return
    
    # Convert points from isometric basis to cardinal basis
    cardPoints = []
    for point in points:
        cardPoints.append(convertIso2Card(point))
    
    # Draw outern lines
    for i in range(len(cardPoints)-2):
        drawLine(cardPoints[i], cardPoints[i+1])
    drawLine(cardPoints[0], cardPoints[-2])
    
    # Draw inner lines
    for i in range(1, 6, 2):
        drawLine(cardPoints[i], cardPoints[-1])
    
    # Draw hidden lines
    for i in range(0, 7, 2):
        drawLine(cardPoints[i], cardPoints[-1], "dashed")
    
    # Draw points
    for point in cardPoints:
        drawPoint(point)

#===================#
# Basis conversions #
#===================#

# TO COMPLETE
def convertCard2Iso(point):
    ...

def convertIso2Card(point):
    ...


#==============#
# Main section #
#==============#
if __name__ == "__main__":
    
    #=====--- Create grid and basis ---=====#
    initialization()
    
    #=====--- Conversions ---=====# 
    print(convertIso2Card())
    print(convertIso2Card())
    
    #=====--- Draw a cube in plot ---=====#
    drawFigure((0,0), (0.5,0), (1,0.5), (1,1), (0.5,1), (0,0.5), (0.5,0.5))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    