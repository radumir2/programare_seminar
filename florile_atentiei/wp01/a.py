import math

def transformX(Ox, r, deg):
    return Ox + r*math.cos(2 * math.pi * deg/360)

def transformY(Oy, r, deg):
    return 100 - (Oy + r*math.sin(2 * math.pi * deg/360)) # NOT cartesian because y-axis is inverted


print('<svg width="100" height="100">');
print("<!-- a whole world -->");
print('<circle cx="50" cy="50" r="40" fill="none" stroke="#000" />');
Ox = 50
Oy = 50
r = 40

deg = 0
print('<circle cx="' + str(transformX(Ox, r, deg)) + '" cy="' + str(transformY(Oy, r, deg)) + '" r="1" fill="red" />');
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transformX(Ox, r, deg), transformY(Oy, r, deg)));

deg = 30
print('<circle cx="' + str(transformX(Ox, r, deg)) + '" cy="' + str(transformY(Oy, r, deg)) + '" r="1" fill="red" />');

print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transformX(Ox, r, deg), transformY(Oy, r, deg)));

print(
'<path d="' +
'M {} {}'.format(transformX(Ox, r, 0), transformY(Oy, r, 0)) +
'A {} {} {} {} {} {} {}'.format(r, r, 0, 0, 0, transformX(Ox, r, 30), transformY(Oy, r, 30)) +
'" stroke="#FFF" fill="none"/>'
);


deg = 60
print('<circle cx="' + str(transformX(Ox, r, deg)) + '" cy="' + str(transformY(Oy, r, deg)) + '" r="1" fill="red" />');
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transformX(Ox, r, deg), transformY(Oy, r, deg)));

print(
'<path d="' +
'M {} {}'.format(Ox,Oy) +
'L {} {}'.format(transformX(Ox, r, 30), transformY(Oy, r, 30)) +
'A {} {} {} {} {} {} {}'.format(r, r, 0, 0, 0, transformX(Ox, r, 60), transformY(Oy, r, 60)) +
'L {} {}'.format(Ox, Oy) +
'" stroke="green" fill="blue"/>'
);

deg = 90
print('<circle cx="' + str(transformX(Ox, r, deg)) + '" cy="' + str(transformY(Oy, r, deg)) + '" r="1" fill="red" />');
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transformX(Ox, r, deg), transformY(Oy, r, deg)));

def pointOnLineX(x1, x2, p):
    return x1 + p *(x2 - x1);
    
def pointOnLineY(y1, y2, p):
    return y1 + p* (y2 - y1);

print(
'<circle cx="{}" cy="{}" r="1" stroke="red" />'.format(pointOnLineX(Ox, transformX(Ox, r, 60), 0.5), pointOnLineY(Oy, transformY(Oy, r, 60), 0.5))
);

print(
'<path d="' +
'M {} {}'.format(Ox,Oy) +
'L {} {}'.format(pointOnLineX(Ox, transformX(Ox, r, 60), 0.5), pointOnLineY(Oy, transformY(Oy, r, 60), 0.5)) +
'Q {} {} {} {}'.format(transformX(Ox,r, 60), transformY(Oy, r, 60), transformX(Ox,r, 75), transformY(Oy, r, 75) ) +
'Q {} {} {} {}'.format(transformX(Ox,r, 90), transformY(Oy, r, 90), pointOnLineX(Ox, transformX(Ox, r, 90), 0.5), pointOnLineY(Oy, transformY(Oy, r, 90), 0.5) ) +
'L {} {}'.format(Ox, Oy) +
'" stroke="yellow" fill="none" />'
);

print('</svg>')
