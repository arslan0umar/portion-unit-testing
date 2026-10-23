import pytest
import portion as p

@pytest.mark.order(1)
@pytest.mark.smoke
def test_get_smoke():
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "v"
    assert d.get(3) == "v"
    assert d.get(10) is None

@pytest.mark.order(2)
@pytest.mark.ecp
@pytest.mark.parametrize("k,exp", [
    (1, "a"),
    (3, "a"),
    (5, "a"),
    (6, "miss"),
    (p.closed(2, 4), "{[2,4]: 'a'}"),
    (p.empty(), "{}"),
])
def test_get_ecp(k, exp):
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "a"
    if isinstance(k, p.Interval):
        res = d.get(k)
        assert repr(res) == exp
    else:
        res = d.get(k, "miss")
        assert res == exp

@pytest.mark.order(3)
@pytest.mark.bva
@pytest.mark.parametrize("inv,pt,exp", [
    (p.closed(1, 5), 1, "v"),
    (p.open(1, 5), 1, "def"),
    (p.closed(1, 5), 5, "v"),
    (p.closedopen(1, 5), 5, "def"),
    (p.closed(1, 5), 5.0001, "def"),
])
def test_get_bva(inv, pt, exp):
    d = p.IntervalDict()
    d[inv] = "v"
    res = d.get(pt, "def")
    assert res == exp

@pytest.mark.order(4)
@pytest.mark.regression
@pytest.mark.parametrize("query,exp", [
    (p.closed(0, 2), "{[0,1): 'x', [1,2]: 'v'}"),
    (p.closed(4, 6), "{[4,5]: 'v', (5,6]: 'x'}"),
    (p.closed(8, 10), "{[8,10]: 'x'}"),
])
def test_get_regression(query, exp):
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "v"
    res = d.get(query, "x")
    assert repr(res) == exp

@pytest.mark.order(5)
@pytest.mark.smoke
def test_domain_smoke():
    d = p.IntervalDict()
    d[p.closed(1, 5)] = "v"
    assert d.domain() == p.closed(1, 5)

@pytest.mark.order(6)
@pytest.mark.ecp
@pytest.mark.parametrize("k,v,exp", [
    (p.empty(), "x", "()"),
    (p.closed(1, 5), "a", "[1,5]"),
    (p.open(-2, 2), "b", "(-2,2)"),
    (p.singleton(7), "c", "[7]"),
    (p.closedopen(0, p.inf), "d", "[0,+inf)"),
])
def test_domain_ecp(k, v, exp):
    d = p.IntervalDict()
    d[k] = v
    assert repr(d.domain()) == exp

@pytest.mark.order(7)
@pytest.mark.bva
@pytest.mark.parametrize("fst,snd,exp", [
    (p.closed(1, 3), p.closed(4, 6), "[1,3] | [4,6]"),
    (p.closedopen(1, 3), p.closed(3, 5), "[1,5]"),
    (p.closed(1, 5), p.closed(2, 4), "[1,5]"),
    (p.closed(2, 4), p.closed(1, 5), "[1,5]"),
    (p.empty(), p.empty(), "()"),
])
def test_domain_bva(fst, snd, exp):
    d = p.IntervalDict()
    d[fst] = "a"
    d[snd] = "b"
    assert repr(d.domain()) == exp

@pytest.mark.order(8)
@pytest.mark.regression
@pytest.mark.parametrize("inv,cut,exp", [
    (p.closed(1, 5), p.closed(1, 2), "(2,5]"),
    (p.closed(1, 5), p.closed(4, 5), "[1,4)"),
    (p.closed(1, 5), p.closed(1, 5), "()"),
])
def test_domain_regression(inv, cut, exp):
    d = p.IntervalDict()
    d[inv] = "val"
    del d[cut]
    assert repr(d.domain()) == exp

@pytest.mark.order(9)
@pytest.mark.smoke
def test_to_string_smoke():
    res = p.to_string(p.closed(1, 5))
    assert res == "[1,5]"

@pytest.mark.order(10)
@pytest.mark.ecp
@pytest.mark.parametrize("inv,exp", [
    (p.empty(), "()"),
    (p.closed(1, 5), "[1,5]"),
    (p.open(1, 5), "(1,5)"),
    (p.closedopen(1, 5), "[1,5)"),
    (p.openclosed(-p.inf, 0), "(-inf,0]"),
    (p.closed(1, 2) | p.closed(4, 5), "[1,2] | [4,5]"),
])
def test_to_string_ecp(inv, exp):
    res = p.to_string(inv)
    assert res == exp

@pytest.mark.order(11)
@pytest.mark.bva
@pytest.mark.parametrize("inv,exp", [
    (p.singleton(3), "[3]"),
    (p.open(-p.inf, p.inf), "(-inf,+inf)"),
    (p.closed(1.5, 3.5), "[1.5,3.5]"),
    (p.closed(0, 0), "[0]"),
    (p.closedopen(0, p.inf), "[0,+inf)"),
])
def test_to_string_bva(inv, exp):
    res = p.to_string(inv)
    assert res == exp

@pytest.mark.order(12)
@pytest.mark.regression
@pytest.mark.parametrize("inv,sep,exp", [
    (p.closed(1, 5), "..", "[1..5]"),
    (p.closed(2, 8), ";", "[2;8]"),
    (p.closed(-3, 3), ":", "[-3:3]"),
])
def test_to_string_regression(inv, sep, exp):
    res = p.to_string(inv, sep=sep)
    assert res == exp

@pytest.mark.order(13)
@pytest.mark.smoke
def test_from_string_smoke():
    res = p.from_string("[1,5]", int)
    assert res == p.closed(1, 5)

@pytest.mark.order(14)
@pytest.mark.ecp
@pytest.mark.parametrize("txt,exp", [
    ("[1,5]", "[1,5]"),
    ("(1,5)", "(1,5)"),
    ("[1,5)", "[1,5)"),
    ("(1,5]", "(1,5]"),
    ("[3]", "[3]"),
    ("()", "()"),
])
def test_from_string_ecp(txt, exp):
    res = p.from_string(txt, int)
    assert repr(res) == exp

@pytest.mark.order(15)
@pytest.mark.bva
@pytest.mark.parametrize("txt,exp", [
    ("(-inf,0]", "(-inf,0]"),
    ("[0,+inf)", "[0,+inf)"),
    ("(-inf,+inf)", "(-inf,+inf)"),
    ("[1,2] | [4,5]", "[1,2] | [4,5]"),
    ("[1.5,4.5]", "[1.5,4.5]"),
])
def test_from_string_bva(txt, exp):
    if "." in txt:
        res = p.from_string(txt, float)
    else:
        res = p.from_string(txt, int)
    assert repr(res) == exp

@pytest.mark.order(16)
@pytest.mark.regression
@pytest.mark.parametrize("inv", [
    p.closed(1, 5),
    p.open(2, 6),
    p.closed(1, 2) | p.closed(4, 5),
])
def test_from_string_regression(inv):
    txt = p.to_string(inv)
    res = p.from_string(txt, int)
    assert res == inv
