import csv
from pathlib import Path
import pytest
import portion as p

def load():
    path = Path(__file__).resolve().parents[2] / "data" / "arslan_data.csv"
    data = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((
                row["lower"],
                row["upper"],
                row["other lower"],
                row["other upper"],
                row["expected intersection"],
            ))
    return data

rows = load()

def parse(val):
    if val == "inf":
        return p.inf
    if val == "-inf":
        return -p.inf
    if "." in val:
        return float(val)
    return int(val)

@pytest.mark.order(1)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,olow,oup,exp", rows)
def test_ops_csv_intersection(low, up, olow, oup, exp):
    a = p.closed(parse(low), parse(up))
    b = p.closed(parse(olow), parse(oup))
    res = a.intersection(b)
    assert repr(res) == exp

@pytest.mark.order(2)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,olow,oup,exp", rows)
def test_ops_csv_commutative(low, up, olow, oup, exp):
    a = p.closed(parse(low), parse(up))
    b = p.closed(parse(olow), parse(oup))
    res = b.intersection(a)
    assert repr(res) == exp

@pytest.mark.order(3)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,olow,oup,exp", rows)
def test_ops_csv_operator(low, up, olow, oup, exp):
    a = p.closed(parse(low), parse(up))
    b = p.closed(parse(olow), parse(oup))
    res = a & b
    assert repr(res) == exp

@pytest.mark.order(4)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,olow,oup,exp", rows)
def test_ops_csv_containment(low, up, olow, oup, exp):
    a = p.closed(parse(low), parse(up))
    b = p.closed(parse(olow), parse(oup))
    res = a.intersection(b)
    if not res.empty:
        assert res in a
        assert res in b
