import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_setitem_smoke():
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "v"
    assert d[3] == "v"
    assert d.domain() == p.closed(1, 5)

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("k,v,exp", [
    (p.closed(1, 3), "a", "[1,3]"),
    (p.open(2, 6), "b", "(2,6)"),
    (p.singleton(5), "c", "[5]"),
    (p.closed(-2, 2), "d", "[-2,2]"),
    (p.empty(), "e", "()"),
])
def test_setitem_ecp(k, v, exp):
    d = p.IntervalDict()
    d[k] = v
    assert repr(d.domain()) == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("k1,v1,k2,v2,exp", [
    (p.closedopen(1, 3), "a", p.closed(3, 5), "a", "[1,5]"),
    (p.closed(1, 5), "a", p.closed(5, 8), "a", "[1,8]"),
    (p.closed(1, 5), "a", 5, "b", "[1,5]"),
    (p.closed(1, 5), "a", p.closed(0, 6), "b", "[0,6]"),
    (p.closed(1, 3), "a", p.closed(4, 6), "b", "[1,3] | [4,6]"),
])
def test_setitem_bva(k1, v1, k2, v2, exp):
    d = p.IntervalDict()
    d[k1] = v1
    d[k2] = v2
    assert repr(d.domain()) == exp

@pytest.mark.order(4)
@pytest.mark.regression
@pytest.mark.parametrize("k,v", [
    (10, "x"),
    (-5, "y"),
    (0, "z"),
])
def test_setitem_regression(k, v):
    d = p.IntervalDict()
    d[k] = v
    assert d[k] == v
    assert d.domain() == p.singleton(k)

@pytest.mark.order(5)
@pytest.mark.smoke
def test_getitem_smoke():
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "v"
    assert d[3] == "v"
    sub = d[p.closed(2, 4)]
    assert sub.domain() == p.closed(2, 4)

@pytest.mark.order(6)
@pytest.mark.ecp
@pytest.mark.parametrize("k,exp", [
    (1, "a"),
    (2, "a"),
    (3, "a"),
    (4, "a"),
    (5, "a"),
])
def test_getitem_ecp(k, exp):
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "a"
    assert d[k] == exp

@pytest.mark.order(7)
@pytest.mark.bva
@pytest.mark.parametrize("inv,pt,valid", [
    (p.closed(1, 5), 1, True),
    (p.open(1, 5), 1, False),
    (p.closed(1, 5), 5, True),
    (p.closedopen(1, 5), 5, False),
    (p.closed(1, 5), 5.0001, False),
])
def test_getitem_bva(inv, pt, valid):
    d = p.IntervalDict()
    d[inv] = "val"
    if valid:
        assert d[pt] == "val"
    else:
        with pytest.raises(KeyError):
            d[pt]

@pytest.mark.order(8)
@pytest.mark.regression
@pytest.mark.parametrize("query,exp", [
    (p.closed(2, 3), "[2,3]"),
    (p.closed(10, 20), "()"),
    (p.empty(), "()"),
])
def test_getitem_regression(query, exp):
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "a"
    sub = d[query]
    assert repr(sub.domain()) == exp
