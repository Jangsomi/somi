name = 'Somi Jang'
age = 22 # not a lie
height_cm = 171.6 # centimeters
cm_to_inch = 1.0 / 2.54
height_inch = height_cm * cm_to_inch
weight_kg = 52 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
# place holder
print "Let's talk about %s." % name
print "She's %g centimeters tall." % height_cm
print "She's %g kilograms tall." % height_inch
print "She's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
