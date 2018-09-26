def detect_cell(xLines, yLines, pixelOrigin, targetPoint):
    """
    This method returns the GroundGrid coordinates of the grid cell containing the targetPoint
    Inputs:
        xLines - List of pairs of points lying on x-axis grid lines e.g. [ ( [0,0], [10,0] ) , ([0,10] , [10,10]) ]
        yLines - Same as above but for y-axis
        pixelOrigin - Origin of the real grid in pixel coordinate
        TargetPoint - The laser dot (in pixel coordinates) that needs to be located within grid
    Outputs:
        CellCoordinates - The x,y position of the real world grid where the point lies
    """
    x = 0
    y = 0
    return [x, y]
