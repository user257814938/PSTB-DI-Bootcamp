from math import pi, isclose                          # importe π et isclose pour comparer des floats
from functools import total_ordering                   # génère les comparaisons à partir de __eq__ et __lt__

@total_ordering                                        # fournit __le__, __gt__, __ge__ si __eq__ et __lt__ sont définis
class Circle:
    def __init__(self, *, radius=None, diameter=None):
        # autorise l'init par radius OU diameter (au moins un des deux)
        if radius is None and diameter is None:
            raise ValueError("Provide radius or diameter")

        # si les deux sont fournis, on vérifie la cohérence
        if radius is not None and diameter is not None:
            if not isclose(diameter, 2 * radius):
                raise ValueError("Inconsistent radius/diameter")
            self._radius = float(radius)
        elif radius is not None:
            self._radius = float(radius)
        else:
            self._radius = float(diameter) / 2.0

        # validation basique
        if self._radius <= 0:
            raise ValueError("Radius must be positive")

    # --- properties: radius / diameter ---
    @property
    def radius(self):
        return self._radius                            # expose le rayon (lecture)

    @radius.setter
    def radius(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value                           # met à jour le rayon (écriture)

    @property
    def diameter(self):
        return 2 * self._radius                        # calcule le diamètre à la volée

    @diameter.setter
    def diameter(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self._radius = value / 2.0                     # mettre à jour via diamètre met à jour le rayon

    # --- API métier ---
    def area(self):
        return pi * (self._radius ** 2)                # aire du disque: πr²

    # --- dunder methods ---
    def __repr__(self):
        # représentation officielle, utile en debug et pour print()
        return f"Circle(radius={self._radius:.6g})"

    def __add__(self, other):
        # addition de deux cercles: nouveau cercle dont le rayon est la somme des rayons
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self._radius + other._radius)

    def __eq__(self, other):
        # égalité: comparaison des rayons avec tolérance pour les floats
        if not isinstance(other, Circle):
            return NotImplemented
        return isclose(self._radius, other._radius, rel_tol=1e-9, abs_tol=1e-12)

    def __lt__(self, other):
        # ordre strict: compare les rayons → permet de trier une liste de Circle
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius

# ----------------------------
# Démonstration / tests simples
# ----------------------------
if __name__ == "__main__":
    # création par radius
    c1 = Circle(radius=3)                              # rayon 3
    # création par diameter
    c2 = Circle(diameter=10)                           # rayon 5

    # properties
    print(repr(c1))                                    # >> Circle(radius=3)
    print(repr(c2))                                    # >> Circle(radius=5)
    print(c1.radius, c1.diameter)                      # >> 3 6
    print(f"{c2.area():.4f}")                          # >> aire de c2 (π*5² = 78.5398)

    # addition (nouveau cercle avec rayon = 3 + 5 = 8)
    c3 = c1 + c2
    print(repr(c3))                                    # >> Circle(radius=8)

    # comparaisons
    print(c1 == Circle(radius=3))                      # >> True
    print(c1 < c2)                                     # >> True
    print(c2 > c1)                                     # >> True

    # tri d'une liste
    circles = [c3, c1, c2, Circle(radius=1.5)]
    circles.sort()                                     # utilise __lt__
    print(circles)                                     # >> triés par rayon croissant

    # bonus Turtle (optionnel) : dessin des cercles triés
    # import turtle
    # t = turtle.Turtle()
    # t.speed("fastest")
    # x = -200
    # for c in circles:
        # t.penup()
        # t.setpos(x, 0)
        # t.pendown()
        # t.circle(c.radius * 10)                      # échelle 10 px par unité de rayon
        # x += (c.diameter * 10) + 20                  # espace entre cercles
    # turtle.done()
