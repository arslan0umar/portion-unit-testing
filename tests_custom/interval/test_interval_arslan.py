import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_closed_smoke():
    res = p.closed(1, 5)
    assert res.lower == 1
    assert res.upper == 5
    assert res.left == p.CLOSED
    assert res.right == p.CLOSED

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("low,up,exp", [
    (1, 5, "[1,5]"),
    (-5, -1, "[-5,-1]"),
    (3, 3, "[3]"),
    (-p.inf, 0, "(-inf,0]"),
    (0, p.inf, "[0,+inf)"),
])
def test_closed_ecp(low, up, exp):
    res = p.closed(low, up)
    assert repr(res) == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("low,up,exp", [
    (2, 2, "[2]"),
    (3, 2, "()"),
    (-p.inf, p.inf, "(-inf,+inf)"),
    (-1, 1, "[-1,1]"),
    (1.0, 1.0001, "[1.0,1.0001]"),
])
def test_closed_bva(low, up, exp):
    res = p.closed(low, up)
    assert repr(res) == exp

@pytest.mark.order(4)
@pytest.mark.smoke
def test_open_smoke():
    res = p.open(1, 5)
    assert res.lower == 1
    assert res.upper == 5
    assert res.left == p.OPEN
    assert res.right == p.OPEN

@pytest.mark.order(5)
@pytest.mark.ecp
@pytest.mark.parametrize("low,up,exp", [
    (1, 5, "(1,5)"),
    (-6, -2, "(-6,-2)"),
    (-p.inf, 2, "(-inf,2)"),
    (2, p.inf, "(2,+inf)"),
    (-p.inf, p.inf, "(-inf,+inf)"),
])
def test_open_ecp(low, up, exp):
    res = p.open(low, up)
    assert repr(res) == exp

@pytest.mark.order(6)
@pytest.mark.bva
@pytest.mark.parametrize("low,up,exp", [
    (4, 4, "()"),
    (5, 2, "()"),
    (1, 2, "(1,2)"),
    (-2, 0, "(-2,0)"),
    (0.0, 0.001, "(0.0,0.001)"),
])
def test_open_bva(low, up, exp):
    res = p.open(low, up)
    assert repr(res) == exp

@pytest.mark.order(7)
@pytest.mark.smoke
def test_openclosed_smoke():
    res = p.openclosed(1, 5)
    assert res.left == p.OPEN
    assert res.right == p.CLOSED
    assert res.lower == 1
    assert res.upper == 5

@pytest.mark.order(8)
@pytest.mark.ecp
@pytest.mark.parametrize("low,up,exp", [
    (1, 5, "(1,5]"),
    (-4, -1, "(-4,-1]"),
    (-p.inf, 3, "(-inf,3]"),
    (1, p.inf, "(1,+inf)"),
    (2, 2, "()"),
])
def test_openclosed_ecp(low, up, exp):
    res = p.openclosed(low, up)
    assert repr(res) == exp

@pytest.mark.order(9)
@pytest.mark.bva
@pytest.mark.parametrize("low,up,exp", [
    (0, 0, "()"),
    (0, 1, "(0,1]"),
    (-5, -4, "(-5,-4]"),
    (3, 1, "()"),
    (1.0001, 1.0, "()"),
])
def test_openclosed_bva(low, up, exp):
    res = p.openclosed(low, up)
    assert repr(res) == exp

@pytest.mark.order(10)
@pytest.mark.smoke
def test_closedopen_smoke():
    res = p.closedopen(1, 5)
    assert res.left == p.CLOSED
    assert res.right == p.OPEN
    assert res.lower == 1
    assert res.upper == 5

@pytest.mark.order(11)
@pytest.mark.ecp
@pytest.mark.parametrize("low,up,exp", [
    (1, 5, "[1,5)"),
    (-5, -2, "[-5,-2)"),
    (-p.inf, 4, "(-inf,4)"),
    (0, p.inf, "[0,+inf)"),
    (3, 3, "()"),
])
def test_closedopen_ecp(low, up, exp):
    res = p.closedopen(low, up)
    assert repr(res) == exp

@pytest.mark.order(12)
@pytest.mark.bva
@pytest.mark.parametrize("low,up,exp", [
    (7, 7, "()"),
    (3, 4, "[3,4)"),
    (-1, 1, "[-1,1)"),
    (5, 2, "()"),
    (2.0, 2.0001, "[2.0,2.0001)"),
])
def test_closedopen_bva(low, up, exp):
    res = p.closedopen(low, up)
    assert repr(res) == exp

@pytest.mark.order(13)
@pytest.mark.smoke
def test_singleton_smoke():
    res = p.singleton(5)
    assert res.lower == 5
    assert res.upper == 5
    assert res.left == p.CLOSED
    assert res.right == p.CLOSED

@pytest.mark.order(14)
@pytest.mark.ecp
@pytest.mark.parametrize("val,exp", [
    (5, "[5]"),
    (-10, "[-10]"),
    (0, "[0]"),
    (2.5, "[2.5]"),
    ("a", "['a']"),
])
def test_singleton_ecp(val, exp):
    res = p.singleton(val)
    assert repr(res) == exp

@pytest.mark.order(15)
@pytest.mark.bva
@pytest.mark.parametrize("val,exp", [
    (0, "[0]"),
    (p.inf, "()"),
    (-p.inf, "()"),
    (1e-9, "[1e-09]"),
    (1000000, "[1000000]"),
])
def test_singleton_bva(val, exp):
    res = p.singleton(val)
    assert repr(res) == exp

@pytest.mark.order(16)
@pytest.mark.smoke
def test_empty_smoke():
    res = p.empty()
    assert res.empty is True
    assert len(res) == 0

@pytest.mark.order(17)
@pytest.mark.ecp
@pytest.mark.parametrize("prop,exp", [
    ("empty", True),
    ("atomic", True),
    ("lower", p.inf),
    ("upper", -p.inf),
    ("left", p.OPEN),
])
def test_empty_ecp(prop, exp):
    res = p.empty()
    assert getattr(res, prop) == exp

@pytest.mark.order(18)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.closed(1, 2), "()"),
    (p.open(3, 4), "()"),
    (p.singleton(0), "()"),
    (p.empty(), "()"),
])
def test_empty_bva(inv, exp):
    res = p.empty() & inv
    assert repr(res) == exp

@pytest.mark.order(19)
@pytest.mark.smoke
def test_replace_smoke():
    inv = p.closed(1, 5)
    res = inv.replace(lower=2)
    assert res == p.closed(2, 5)

@pytest.mark.order(20)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,low,up,exp", [
    (p.closed(1, 5), 2, None, "[2,5]"),
    (p.closed(1, 5), None, 8, "[1,8]"),
    (p.closed(1, 5), -2, 7, "[-2,7]"),
    (p.open(1, 5), 0, None, "(0,5)"),
    (p.closed(1, 2) | p.closed(4, 5), 0, None, "[0,2] | [4,5]"),
])
def test_replace_ecp(inv, low, up, exp):
    res = inv.replace(lower=low, upper=up)
    assert repr(res) == exp

@pytest.mark.order(21)
@pytest.mark.bva
@pytest.mark.parametrize("inv,low,up,exp", [
    (p.closed(1, 5), 5, None, "[5]"),
    (p.closed(1, 5), 10, None, "()"),
    (p.closed(1, 5), None, 1, "[1]"),
    (p.closed(1, 5), None, -1, "()"),
    (p.open(1, 5), 5, None, "()"),
])
def test_replace_bva(inv, low, up, exp):
    res = inv.replace(lower=low, upper=up)
    assert repr(res) == exp
