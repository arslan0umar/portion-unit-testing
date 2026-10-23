import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_intersection_smoke():
    a = p.closed(1, 5)
    b = p.closed(3, 7)
    res = a.intersection(b)
    assert res == p.closed(3, 5)

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 5), p.closed(3, 7), "[3,5]"),
    (p.closed(1, 3), p.closed(5, 8), "()"),
    (p.closed(1, 10), p.closed(3, 6), "[3,6]"),
    (p.closed(1, 5), p.empty(), "()"),
    (p.closed(1, 5), p.closed(1, 5), "[1,5]"),
])
def test_intersection_ecp(a, b, exp):
    res = a.intersection(b)
    assert repr(res) == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 3), p.closed(3, 5), "[3]"),
    (p.closedopen(1, 3), p.closed(3, 5), "()"),
    (p.closedopen(1, 3), p.openclosed(3, 5), "()"),
    (p.closed(-p.inf, 4), p.closed(2, p.inf), "[2,4]"),
    (p.closed(1, 2), p.closed(2.0001, 4), "()"),
])
def test_intersection_bva(a, b, exp):
    res = a.intersection(b)
    assert repr(res) == exp

@pytest.mark.order(4)
@pytest.mark.regression
@pytest.mark.parametrize("a,b,exp", [
    ((p.closed(1, 3) | p.closed(6, 9)), p.closed(2, 7), "[2,3] | [6,7]"),
    (p.open(0, 5), p.closed(2, 3), "[2,3]"),
    (p.closed(1, 4), p.closed(2, 3), "[2,3]"),
])
def test_intersection_regression(a, b, exp):
    res = a.intersection(b)
    assert res == (a & b)
    assert repr(res) == exp

@pytest.mark.order(5)
@pytest.mark.smoke
def test_union_smoke():
    a = p.closed(1, 5)
    b = p.closed(3, 7)
    res = a.union(b)
    assert res == p.closed(1, 7)

@pytest.mark.order(6)
@pytest.mark.ecp
@pytest.mark.parametrize("a,b,exp", [
    (p.closed(1, 5), p.closed(3, 8), "[1,8]"),
    (p.closed(1, 3), p.closed(6, 9), "[1,3] | [6,9]"),
    (p.closed(1, 10), p.closed(3, 6), "[1,10]"),
    (p.closed(2, 6), p.empty(), "[2,6]"),
    (p.closed(2, 6), p.closed(2, 6), "[2,6]"),
])
def test_union_ecp(a, b, exp):
    res = a.union(b)
    assert repr(res) == exp

@pytest.mark.order(7)
@pytest.mark.bva
@pytest.mark.parametrize("a,b,exp", [
    (p.closedopen(1, 3), p.closed(3, 5), "[1,5]"),
    (p.closed(1, 3), p.openclosed(3, 5), "[1,5]"),
    (p.closedopen(1, 3), p.openclosed(3, 5), "[1,3) | (3,5]"),
    (p.closed(1, 4), p.closed(4, 7), "[1,7]"),
    (p.closed(-p.inf, 0), p.closed(0, p.inf), "(-inf,+inf)"),
])
def test_union_bva(a, b, exp):
    res = a.union(b)
    assert repr(res) == exp

@pytest.mark.order(8)
@pytest.mark.regression
@pytest.mark.parametrize("a,b,exp", [
    (p.empty(), p.empty(), "()"),
    ((p.closed(1, 2) | p.closed(5, 6)), p.closed(2, 5), "[1,6]"),
    (p.open(1, 2), p.open(2, 3), "(1,2) | (2,3)"),
])
def test_union_regression(a, b, exp):
    res = a.union(b)
    assert res == (a | b)
    assert repr(res) == exp
