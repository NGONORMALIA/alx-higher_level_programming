#!/usr/bin/python3
"""Module to mutiply two matrix"""


def matrix_mul(m_a, m_b):
    """Mutiplication of two matrix
    Args:
        m_a : the first matrix(list of list)
        m_b : the second matrix(list of list)

    Raises:
        TypeError:if matrix is not a list of list of int
        ValueError: if matrix is empty
    """
    mul = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not (isinstance(rowa, list) for rowa in m_a):
        raise TypeError("m_a must be a list of lists")
    if not (isinstance(rowb, list) for rowb in m_b):
        raise TypeError("m_b must be a list of lists")
    if (m_a == [] or m_a == [[]] or len(m_a) == 0 or m_a is None):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]] or len(m_b) == 0 or m_b is None):
        raise ValueError("m_b can't be empty")
    if not all((isinstance(itema, int) or
                isinstance(itema, float))
               for itema in [rowaa for b in m_a for rowaa in b]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(itemb, int) or
                isinstance(itemb, float))
               for itemb in [rowab for b in m_b for rowab in b]):
        raise TypeError("m_b should contain only integers or floats")
    if (not all(len(rowaaa) == len(m_a[0]) for rowaaa in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if (not all(len(rowaab) == len(m_b[0]) for rowaab in m_b)):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for row in m_a:
        b = []
        for i in range(len(m_b)):
            a = 0
            for j in range(len(row)):
                a = a + row[j] * m_b[j][i]
            b.append(a)
        mul.append(b)
    return mul
