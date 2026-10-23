import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_complement_smoke():
    res = p.closed(1, 5).complement()
    assert res == (p.open(-p.inf, 1) | p.open(5, p.inf))

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), "(-inf,+inf)"),
    (p.open(-p.inf, p.inf), "()"),
    (p.closed(1, 5), "(-inf,1) | (5,+inf)"),
    (p.open(1, 5), "(-inf,1] | [5,+inf)"),
    (p.closedopen(0, p.inf), "(-inf,0)"),
    (p.closed(1, 2) | p.closed(4, 5), "(-inf,1) | (2,4) | (5,+inf)"),
])
def test_complement_ecp(inv, exp):
    res = inv.complement()
    assert repr(res) == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.singleton(0), "(-inf,0) | (0,+inf)"),
    (p.openclosed(-p.inf, 2), "(2,+inf)"),
    (p.open(-p.inf, 2), "[2,+inf)"),
    (p.closed(-1, 1), "(-inf,-1) | (1,+inf)"),
    (p.closedopen(0, 1), "(-inf,0) | [1,+inf)"),
])
def test_complement_bva(inv, exp):
    res = inv.complement()
    assert repr(res) == exp

@pytest.mark.order(4)
@pytest.mark.regression
@pytest.mark.parametrize("inv,exp", [
    (p.closed(2, 4), "[2,4]"),
    (p.open(0, 3), "(0,3)"),
    (p.empty(), "()"),
])
def test_complement_regression(inv, exp):
    res = ~inv
    assert res == inv.complement()
    assert repr(~res) == exp

@pytest.mark.order(5)
@pytest.mark.smoke
def test_difference_smoke():
    a = p.closed(1, 5)
    b = p.closed(3, 7)
    res = a.difference(b)
    assert res == p.closedopen(1, 3)

@pytest.mark.order(6)
@pytest.mark.ecp
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 5), p.closed(3, 7), "[1,3)"),
    (p.closed(1, 3), p.closed(5, 8), "[1,3]"),
    (p.closed(1, 10), p.closed(3, 7), "[1,3) | (7,10]"),
    (p.closed(3, 5), p.closed(1, 10), "()"),
    (p.closed(1, 5), p.closed(1, 5), "()"),
    (p.closed(1, 5), p.empty(), "[1,5]"),
])
def test_difference_ecp(a, b, exp):
    res = a.difference(b)
    assert repr(res) == exp

@pytest.mark.order(7)
@pytest.mark.bva
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 4), p.closed(4, 8), "[1,4)"),
    (p.closedopen(1, 4), p.closed(4, 8), "[1,4)"),
    (p.closed(1, 5), p.singleton(5), "[1,5)"),
    (p.empty(), p.closed(1, 5), "()"),
    (p.closed(-5, 5), p.closedopen(0, p.inf), "[-5,0)"),
])
def test_difference_bva(a, b, exp):
    res = a.difference(b)
    assert repr(res) == exp

@pytest.mark.order(8)
@pytest.mark.regression
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 2) | p.closed(4, 6), p.closed(1.5, 5), "[1,1.5) | (5,6]"),
    (p.open(0, 5), p.closed(1, 2), "(0,1) | (2,5)"),
    (p.closed(0, 2), p.empty(), "[0,2]"),
])
def test_difference_regression(a, b, exp):
    res = a - b
    assert res == a.difference(b)
    assert repr(res) == exp

@pytest.mark.order(9)
@pytest.mark.smoke
def test_overlaps_smoke():
    a = p.closed(1, 5)
    b = p.closed(3, 7)
    res = a.overlaps(b)
    assert res is True

@pytest.mark.order(10)
@pytest.mark.ecp
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 5), p.closed(3, 7), True),
    (p.closed(1, 3), p.closed(5, 8), False),
    (p.closed(1, 10), p.closed(3, 6), True),
    (p.closed(1, 5), p.empty(), False),
    (p.empty(), p.empty(), False),
    (p.closed(2, 6), p.closed(2, 6), True),
])
def test_overlaps_ecp(a, b, exp):
    res = a.overlaps(b)
    assert res is exp

@pytest.mark.order(11)
@pytest.mark.bva
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 4), p.closed(4, 8), True),
    (p.closedopen(1, 4), p.closed(4, 8), False),
    (p.closedopen(1, 4), p.openclosed(4, 8), False),
    (p.closed(1, 2), p.closed(2.0001, 5), False),
    (p.openclosed(-p.inf, 0), p.closedopen(0, p.inf), True),
])
def test_overlaps_bva(a, b, exp):
    res = a.overlaps(b)
    assert res is exp

@pytest.mark.order(12)
@pytest.mark.regression
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 2) | p.closed(4, 5), p.closed(2.5, 3.5), False),
    (p.closed(1, 2) | p.closed(4, 5), p.closed(3, 6), True),
    (p.singleton(5), p.closed(0, 10), True),
])
def test_overlaps_regression(a, b, exp):
    assert a.overlaps(b) is exp
    assert b.overlaps(a) is exp

@pytest.mark.order(13)
@pytest.mark.smoke
def test_adjacent_smoke():
    a = p.closedopen(1, 3)
    b = p.closed(3, 5)
    res = a.adjacent(b)
    assert res is True

@pytest.mark.order(14)
@pytest.mark.ecp
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 3), p.openclosed(3, 5), True),
    (p.closedopen(1, 3), p.closed(3, 5), True),
    (p.closed(1, 2), p.closed(4, 5), False),
    (p.closed(1, 4), p.closed(3, 6), False),
    (p.empty(), p.closed(1, 5), True),
    (p.empty(), p.empty(), True),
])
def test_adjacent_ecp(a, b, exp):
    res = a.adjacent(b)
    assert res is exp

@pytest.mark.order(15)
@pytest.mark.bva
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 3), p.closed(3, 5), False),
    (p.closedopen(1, 3), p.openclosed(3, 5), False),
    (p.openclosed(-p.inf, 0), p.open(0, p.inf), True),
    (p.closedopen(0.0, 1.5), p.closed(1.5, 3.0), True),
    (p.empty(), p.closed(1, 2) | p.closed(4, 5), False),
])
def test_adjacent_bva(a, b, exp):
    res = a.adjacent(b)
    assert res is exp

@pytest.mark.order(16)
@pytest.mark.regression
@pytest.mark.parametrize("a,b,exp", [
    (p.closedopen(0, 2), p.closed(2, 4), True),
    (p.singleton(2), p.open(2, 5), True),
    (p.open(0, 2), p.singleton(2), True),
])
def test_adjacent_regression(a, b, exp):
    assert a.adjacent(b) is exp
    assert b.adjacent(a) is exp

@pytest.mark.order(17)
@pytest.mark.smoke
def test_contains_smoke():
    inv = p.closed(1, 5)
    res = 3 in inv
    assert res is True

@pytest.mark.order(18)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,item,exp", [
    (p.closed(1, 5), 3, True),
    (p.closed(1, 5), 8, False),
    (p.closed(1, 5), p.closed(2, 4), True),
    (p.closed(1, 5), p.closed(3, 7), False),
    (p.closed(1, 5), p.empty(), True),
    (p.closed(1, 2) | p.closed(4, 6), 4, True),
])
def test_contains_ecp(inv, item, exp):
    res = item in inv
    assert res is exp

@pytest.mark.order(19)
@pytest.mark.bva
@pytest.mark.parametrize("inv,item,exp", [
    (p.closed(1, 5), 1, True),
    (p.openclosed(1, 5), 1, False),
    (p.closed(1, 5), 5, True),
    (p.closedopen(1, 5), 5, False),
    (p.closed(1, 5), 5.0001, False),
])
def test_contains_bva(inv, item, exp):
    res = item in inv
    assert res is exp

@pytest.mark.order(20)
@pytest.mark.regression
@pytest.mark.parametrize("inv,item,exp", [
    (p.empty(), 0, False),
    (p.empty(), p.empty(), True),
    (p.closed(1, 5), p.singleton(3), True),
])
def test_contains_regression(inv, item, exp):
    res = inv.contains(item)
    assert (item in inv) is exp
    assert res is exp
