import math


def transform_x(o_x, radius, degree):
    return o_x + radius * math.cos(2 * math.pi * degree / 360)


def transform_y(o_y, radius, degree):
    return 100 - (o_y + radius * math.sin(2 * math.pi * degree / 360))  # NOT cartesian because y-axis is inverted


def point_on_line_x(x1, x2, p):
    return x1 + p * (x2 - x1)


def point_on_line_y(y1, y2, p):
    return y1 + p * (y2 - y1)


print('<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">')
print("<!-- a whole world -->")
print('<circle cx="50" cy="50" r="40" fill="none" stroke="#000" />')
Ox = 50
Oy = 50
r = 40

deg = 0
print('<circle cx="' + str(transform_x(Ox, r, deg)) + '" cy="' + str(transform_y(Oy, r, deg)) + '" r="1" fill="red" />')
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transform_x(Ox, r, deg),
                                                                      transform_y(Oy, r, deg)))

deg = 30
print('<circle cx="' + str(transform_x(Ox, r, deg)) + '" cy="' + str(transform_y(Oy, r, deg)) + '" r="1" fill="red" />')

print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transform_x(Ox, r, deg),
                                                                      transform_y(Oy, r, deg)))

print(
    '<path d="' +
    'M {} {}'.format(transform_x(Ox, r, 0), transform_y(Oy, r, 0)) +
    'A {} {} {} {} {} {} {}'.format(r, r, 0, 0, 0, transform_x(Ox, r, 30), transform_y(Oy, r, 30)) +
    '" stroke="#FFF" fill="none"/>'
)

deg = 60
print('<circle cx="' + str(transform_x(Ox, r, deg)) + '" cy="' + str(transform_y(Oy, r, deg)) + '" r="1" fill="red" />')
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transform_x(Ox, r, deg),
                                                                      transform_y(Oy, r, deg)))

print(
    '<path d="' +
    'M {} {}'.format(Ox, Oy) +
    'L {} {}'.format(transform_x(Ox, r, 30), transform_y(Oy, r, 30)) +
    'A {} {} {} {} {} {} {}'.format(r, r, 0, 0, 0, transform_x(Ox, r, 60), transform_y(Oy, r, 60)) +
    'L {} {}'.format(Ox, Oy) +
    '" stroke="green" fill="blue"/>'
)

deg = 90
print('<circle cx="' + str(transform_x(Ox, r, deg)) + '" cy="' + str(transform_y(Oy, r, deg)) + '" r="1" fill="red" />')
print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#000" />'.format(Ox, Oy, transform_x(Ox, r, deg),
                                                                      transform_y(Oy, r, deg)))

print(
    '<circle cx="{}" cy="{}" r="1" stroke="red" />'.format(point_on_line_x(Ox, transform_x(Ox, r, 60), 0.5),
                                                           point_on_line_y(Oy, transform_y(Oy, r, 60), 0.5))
)

print(
    '<path d="' +
    'M {} {}'.format(Ox, Oy) +
    'L {} {}'.format(point_on_line_x(Ox, transform_x(Ox, r, 60), 0.5),
                     point_on_line_y(Oy, transform_y(Oy, r, 60), 0.5)) +
    'Q {} {} {} {}'.format(transform_x(Ox, r, 60), transform_y(Oy, r, 60), transform_x(Ox, r, 75),
                           transform_y(Oy, r, 75)) +
    'Q {} {} {} {}'.format(transform_x(Ox, r, 90), transform_y(Oy, r, 90),
                           point_on_line_x(Ox, transform_x(Ox, r, 90), 0.5),
                           point_on_line_y(Oy, transform_y(Oy, r, 90), 0.5)) +
    'L {} {}'.format(Ox, Oy) +
    '" stroke="yellow" fill="none" />'
)

print('</svg>')
