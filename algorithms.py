import math

def CalculateAngle(blades):
  angle = 360/blades
  return angle
  
def CalculateArchWidth(length, viaducts):
  width = length/viaducts
  return width
  
def CalculatePercentSlope(delta_x, delta_h):
  percentslope = (delta_h/delta_x) * 100
  return percentslope
  
def CalculateArcLength(length, height):
  radius = (height/2) + ((length ** 2)/(8 * height))
  theta = 2 * math.degrees(math.asin(length/(2 * radius)))
  arclength = 2 * math.pi * radius * (theta/360)
  return arclength