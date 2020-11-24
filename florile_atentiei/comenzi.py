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
        self.unghi_delta = (5 / 360) * 2 * math.pi

    def stil(self, rezultat):
        if rezultat is None:
            bgc = self.bg_none
        elif rezultat:
            bgc = self.bg_hit
        else:
            bgc = self.bg_fail
        return f"stroke: #{self.stroke}; stroke-width: {self.stroke_width}; fill: #{bgc}"


class Polar:
    def __init__(self, centru_x, centru_y, raza):
        self.centru_x = centru_x
        self.centru_y = centru_y
        self.raza = raza

    def punct_pe_cerc(self, unghi, dr=0):
        raza2 = self.raza + dr
        x_a = self.centru_x + raza2 * math.cos(unghi)
        y_a = self.centru_y - raza2 * math.sin(unghi)
        return f"{x_a},{y_a}"


class Petala:
    def __init__(self, nr_total, nr_petala, nr_student, rezultat):
        self.nr_total = nr_total
        self.nr_petala = nr_petala
        self.nr_student = nr_student
        self.rezultat = rezultat

    def __str__(self):
        return f"{self.nr_petala}:{self.nr_total} pt {self.nr_student} cu {self.rezultat}"

    def svg(self, center_x, center_y, raza_ext, stil_svg):
        polar = Polar(center_x, center_y, raza_ext)
        svgc = [f"M{center_x},{center_y}"]
        deschidere = 2 * math.pi / self.nr_total
        unghi_delta = min(stil_svg.unghi_delta, deschidere / 2)

        unghi_start = math.pi / 2 - (self.nr_petala - 1) * deschidere
        unghi_sfarsit = unghi_start - deschidere
        svgc.append(f"L{polar.punct_pe_cerc(unghi_start, -stil_svg.dr / 2)}")
        svgc.append(f"Q{polar.punct_pe_cerc(unghi_start)}")
        svgc.append(f"{polar.punct_pe_cerc(unghi_start - unghi_delta)}")
        svgc.append(f"A{raza_ext},{raza_ext} 0 0,1 {polar.punct_pe_cerc(unghi_sfarsit + unghi_delta)}")
        svgc.append(f"Q{polar.punct_pe_cerc(unghi_sfarsit)}")
        svgc.append(f"{polar.punct_pe_cerc(unghi_sfarsit,-stil_svg.dr/2)}")
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
    p1 = Petala(3, 1, 1, False)
    with open("./comenzi_petala.svg", "w") as f:
        print(f"FILE: {f}")
        print('<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">', file=f)
        print(p1.svg(300, 300, 100, svgs), file=f)
        print('</svg>', file=f)
