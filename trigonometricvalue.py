# lesson 15 trigonomatric project
import math

def calculate_trig_values(angle_degrees):

    angle_radians = math.radians(angle_degrees)

    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    
    return sin_value, cos_value, tan_value

try:
    angle = float(input("Enter an angle in degrees: "))
    
    sin, cos, tan = calculate_trig_values(angle)
    
    print(f"\nTrigonometric values for {angle}°:")
    print(f"Sine: {sin:.4f}")
    print(f"Cosine: {cos:.4f}")
    print(f"Tangent: {tan:.4f}")
    
    if angle % 90 == 0 and angle % 180 != 0:
        print("Note: Tangent is undefined for this angle (approaches infinity)")

except ValueError:
    print("Please enter a valid number for the angle.")