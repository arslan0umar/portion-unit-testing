import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_lower_smoke():
    res = p.closed(1, 5).lower
    assert res == 1

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.closed(1, 5), 1),
    (p.open(-10, -2), -10),
    (p.openclosed(-p.inf, 5), -p.inf),
    (p.singleton(42), 42),
    (p.closed(1, 2) | p.closed(4, 5), 1),
])
def test_lower_ecp(inv, exp):
    assert inv.lower == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), p.inf),
    (p.singleton(0), 0),
    (p.closed(0.0001, 2.5), 0.0001),
    (p.open(-p.inf, 0), -p.inf),
    (p.open(0, 1) | p.open(2, 3), 0),
])
def test_lower_bva(inv, exp):
    assert inv.lower == exp

@pytest.mark.order(4)
@pytest.mark.smoke
def test_upper_smoke():
    res = p.closed(1, 5).upper
    assert res == 5

@pytest.mark.order(5)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.closed(1, 5), 5),
    (p.open(-10, -2), -2),
    (p.closedopen(0, p.inf), p.inf),
    (p.singleton(42), 42),
    (p.closed(1, 2) | p.closed(4, 8), 8),
])
def test_upper_ecp(inv, exp):
    assert inv.upper == exp

@pytest.mark.order(6)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), -p.inf),
    (p.singleton(0), 0),
    (p.closed(0, 1.0001), 1.0001),
    (p.open(-10, p.inf), p.inf),
    (p.closed(-5, -1) | p.closed(0, 9), 9),
])
def test_upper_bva(inv, exp):
    assert inv.upper == exp

@pytest.mark.order(7)
@pytest.mark.smoke
def test_left_smoke():
    res = p.closed(1, 5).left
    assert res == p.CLOSED

@pytest.mark.order(8)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.closed(1, 5), p.CLOSED),
    (p.openclosed(1, 5), p.OPEN),
    (p.singleton(7), p.CLOSED),
    (p.closed(1, 2) | p.open(4, 5), p.CLOSED),
    (p.open(1, 2) | p.closed(4, 5), p.OPEN),
])
def test_left_ecp(inv, exp):
    assert inv.left == exp

@pytest.mark.order(9)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), p.OPEN),
    (p.openclosed(-p.inf, 2), p.OPEN),
    (p.singleton(0), p.CLOSED),
    (p.openclosed(0, 1), p.OPEN),
    (p.closed(1.5, 3.5), p.CLOSED),
])
def test_left_bva(inv, exp):
    assert inv.left == exp

@pytest.mark.order(10)
@pytest.mark.smoke
def test_right_smoke():
    res = p.closed(1, 5).right
    assert res == p.CLOSED

@pytest.mark.order(11)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.closed(1, 5), p.CLOSED),
    (p.closedopen(1, 5), p.OPEN),
    (p.singleton(9), p.CLOSED),
    (p.open(1, 2) | p.closed(4, 6), p.CLOSED),
    (p.closed(1, 2) | p.open(4, 6), p.OPEN),
])
def test_right_ecp(inv, exp):
    assert inv.right == exp

@pytest.mark.order(12)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), p.OPEN),
    (p.closedopen(-1, p.inf), p.OPEN),
    (p.singleton(0), p.CLOSED),
    (p.closedopen(-1, 0), p.OPEN),
    (p.closed(0.1, 0.9), p.CLOSED),
])
def test_right_bva(inv, exp):
    assert inv.right == exp

@pytest.mark.order(13)
@pytest.mark.smoke
def test_atomic_smoke():
    res = p.closed(1, 5).atomic
    assert res is True

@pytest.mark.order(14)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), True),
    (p.closed(1, 5), True),
    (p.open(2, 8), True),
    (p.singleton(3), True),
    (p.open(-p.inf, p.inf), True),
    (p.closed(1, 2) | p.closed(4, 5), False),
])
def test_atomic_ecp(inv, exp):
    assert inv.atomic is exp

@pytest.mark.order(15)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), True),
    (p.open(1, 2) | p.open(2, 3), False),
    (p.closed(1, 2) | p.openclosed(2, 3), True),
    (p.closed(1, 2) | p.closed(4, 5) | p.closed(7, 8), False),
    (p.closed(1, 4) | p.closed(3, 6), True),
])
def test_atomic_bva(inv, exp):
    assert inv.atomic is exp

@pytest.mark.order(16)
@pytest.mark.smoke
def test_empty_smoke():
    res = p.empty().empty
    assert res is True

@pytest.mark.order(17)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), True),
    (p.closed(5, 1), True),
    (p.open(3, 3), True),
    (p.closedopen(2, 2), True),
    (p.closed(1, 5), False),
    (p.singleton(0), False),
])
def test_empty_ecp(inv, exp):
    assert inv.empty is exp

@pytest.mark.order(18)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.open(4, 4), True),
    (p.closed(4, 4), False),
    (p.closed(1, 2) & p.closed(3, 4), True),
    (p.closedopen(1, 3) & p.closed(3, 5), True),
    (p.closed(1.0, 1.00001), False),
])
def test_empty_bva(inv, exp):
    assert inv.empty is exp
