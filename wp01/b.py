import math

WIDTH = 1000
HEIGHT = 1000
Cx = 500
Cy = 500
R = 50
DR = 50

results = [[True, False, True], [False, True]]

def transformX(Ox, r, deg):
    return Ox + r*math.cos(2 * math.pi * deg/360 + math.pi/2)

def transformY(Oy, r, deg):
    return Oy + r*math.sin(2 * math.pi * deg/360 + math.pi/2)
    
def flipY(y):
    return HEIGHT - y # NOT cartesian because y-axis is inverted

def pointOnLineX(x1, x2, p):
    return x1 + p *(x2 - x1)
    
def pointOnLineY(y1, y2, p):
    return y1 + p* (y2 - y1)

def petal(i, j, k, color1, color2):
	"""
	i numarul studentului
	j numarul petalei (de la 0 la k - 1)
	k numarul total de petale
	color1 culoare contur
	color2 culoare fundal
	"""
	r = R + i*DR
	incdeg = 360/k
	deg = -j*incdeg
	degprim = -(j + 1)*incdeg

	# line segment midpoint quadratic bezier midpoint arc quadratic bezier line segment midpoint

	PEG = 0.5

	print(
	'<path d="' +
	'M {},{}'.format(Cx,Cy) +
	'L {},{}'.format(pointOnLineX(Cx, transformX(Cx, r, deg), PEG), flipY(pointOnLineY(Cy, transformY(Cy, r, deg), PEG))) +
	'Q {},{} {},{}'.format(transformX(Cx,r, deg), flipY(transformY(Cy, r, deg)), transformX(Cx,r, (deg + degprim)/2), flipY(transformY(Cy, r, (deg + degprim)/2 ))) +
	'Q {},{} {},{}'.format(transformX(Cx,r, degprim), flipY(transformY(Cy, r, degprim)), pointOnLineX(Cx, transformX(Cx, r, degprim), PEG), flipY( pointOnLineY(Cy, transformY(Cy, r, degprim), PEG) ) ) +
	'L {},{}'.format(Cx, Cy) +
	'" stroke="{}" fill="{}" />'.format(color1,color2)
	)
#main
print('<svg width="{}" height="{}">'.format(WIDTH, HEIGHT))
print("<!-- a whole world -->")

print('<circle cx="{}" cy="{}" r="{}" fill="none" stroke="#000" />'.format(Cx, Cy, R))

for i in range(len(results)):   
    print('<circle cx="{}" cy="{}" r="{}" fill="none" stroke="#000" />'.format(Cx, Cy, R + (i + 1)*DR))
    for j in range(len(results[i])):
        #print('Student {} with result {} of {}'.format(i, j, len(results[i])))
        #print(petal(i + 1, j + 1, len((results[i]))) )
        pass

i = 2
j = 0
k = 2
petal(i,j,k,"yellow","red")
i = 1
j = 0
k = 3
petal(i,j,k,"blue","pink")

print('</svg>')
