import unittest
import math


def transformX(Ox, r, deg):
    return Ox + r * math.cos(2 * math.pi * deg / 360 + math.pi / 2)


def transformY(Oy, r, deg):
    return Oy + r * math.sin(2 * math.pi * deg / 360 + math.pi / 2)


def flipY(y):
    return HEIGHT - y  # NOT cartesian because y-axis is inverted


def pointOnLineX(x1, x2, p):
    return x1 + p * (x2 - x1)


def pointOnLineY(y1, y2, p):
    return y1 + p * (y2 - y1)


class ElementeSvg:
    def __init__(self, dr, bg_hit, bg_fail, bg_none, stroke, stroke_width):
        self.dr = dr
        self.bg_hit = bg_hit
        self.bg_fail = bg_fail
        self.bg_none = bg_none
        self.stroke = stroke
        self.stroke_width = stroke_width

    def stil(self, rezultat):
        if rezultat is None:
            bgc = self.bg_none
        elif rezultat:
            bgc = self.bg_hit
        else:
            bgc = self.bg_fail
        return f"stroke: #{self.stroke}; stroke-width: {self.stroke_width}; fill: #{bgc}"


class Petala:
    def __init__(self, nr_total, nr_petala, nr_student, rezultat):
        self.nr_total = nr_total
        self.nr_petala = nr_petala
        self.nr_student = nr_student
        self.rezultat = rezultat

    def __str__(self):
        return f"{self.nr_petala}:{self.nr_total} pt {self.nr_student} cu {self.rezultat}"

    def svg(self, center_x, center_y, raza_ext, stil_svg):
        svgc = [f"M{center_x},{center_y}"]
        deschidere = 2 * math.pi / self.nr_total
        unghi_start = math.pi / 2 - (self.nr_petala - 1) * deschidere
        unghi_sfarsit = unghi_start - deschidere
        raza_a = raza_ext - stil_svg.dr / 2
        x_a = center_x + raza_a * math.cos(unghi_start)
        y_a = center_y - raza_a * math.sin(unghi_start)
        svgc.append(f"L{x_a},{y_a}")
        x_a_control = center_x + raza_ext * math.cos(unghi_start)
        y_a_control = center_y - raza_ext * math.sin(unghi_start)
        svgc.append(f"Q{x_a_control},{y_a_control}")
        unghi_delta = (5 / 360) * 2 * math.pi
        unghi_b = unghi_start - unghi_delta
        x_b = center_x + raza_ext * math.cos(unghi_b)
        y_b = center_y - raza_ext * math.sin(unghi_b)
        svgc.append(f"{x_b},{y_b}")
        unghi_c = unghi_sfarsit + unghi_delta
        x_c = center_x + raza_ext * math.cos(unghi_c)
        y_c = center_y - raza_ext * math.sin(unghi_c)
        svgc.append(f"A{raza_ext},{raza_ext} 0 0,1 {x_c},{y_c}")
        x_d_control = center_x + raza_ext * math.cos(unghi_sfarsit)
        y_d_control = center_y - raza_ext * math.sin(unghi_sfarsit)
        svgc.append(f"Q{x_d_control},{y_d_control}")
        x_d = center_x + raza_a * math.cos(unghi_sfarsit)
        y_d = center_y - raza_a * math.sin(unghi_sfarsit)
        svgc.append(f"{x_d},{y_d}")
        svgc.append("Z")
        return f"<path d=\"{' '.join(svgc)}\" style=\"{stil_svg.stil(self.rezultat)}\" />"

    __repr__ = __str__


class TesteUnitare(unittest.TestCase):
    def test1(self):
        p = Petala(10, 2, 1, True)
        self.assertEqual("2:10 pt 1 cu True", str(p))

    def test2(self):
        p1 = Petala(3, 1, 1, False)
        p2 = Petala(3, 1, 1, False)
        self.assertEqual(str(p1), str(p2))


if __name__ == "__main__":
    # unittest.main()

    print('-- GENEREZ SVG')
    svgs = ElementeSvg(20, "FFFFFF", "000000", "AAAAAA", "000000", "2")
    p1 = Petala(3, 1, 1, True)
    with open("./comenzi_petala.svg", "w") as f:
        print(f"FILE: {f}")
        print('<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">', file=f)
        print(p1.svg(300, 300, 100, svgs), file=f)
        print('</svg>', file=f)
