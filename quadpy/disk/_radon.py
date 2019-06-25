# -*- coding: utf-8 -*-
#
from __future__ import division

import numpy
import sympy

from ..helpers import z, untangle, article
from ._helpers import DiskScheme


_citation = article(
    authors=["J. Radon"],
    title="Zur mechanischen Kubatur",
    journal="Monatshefte für Mathematik",
    year="1948",
    volume="52",
    pages="286-300",
    issn="0026-9255",
    issne="1436-5081/e",
    url="https://eudml.org/doc/176796",
)


def radon(alpha, symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    pi = sympy.pi if symbolic else numpy.pi
    sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

    r = sqrt(frac(alpha + 4, alpha + 6))
    s = sqrt(frac(alpha + 4, 4 * (alpha + 6)))
    t = sqrt(frac(3 * (alpha + 4), 4 * (alpha + 6)))

    A = frac(4, (alpha + 4) ** 2)
    B = frac((alpha + 2) * (alpha + 6), 6 * (alpha + 4) ** 2)

    data = [
        (A, z(2)),
        (B, numpy.array([[+r, 0], [-r, 0]])),
        # Stroud is missing +- in front of t.
        (B, numpy.array([[+s, +t], [-s, +t], [+s, -t], [-s, -t]])),
    ]

    points, weights = untangle(data)
    weights *= pi
    return DiskScheme("Radon({})".format(alpha), weights, points, 5, _citation)