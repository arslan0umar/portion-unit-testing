import csv
from pathlib import Path
import pytest
import portion as p

def load():
    path = Path(__file__).resolve().parents[2] / "data" / "talha_data.csv"
    data = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((
                row["lower"],
                row["upper"],
                row["value"],
                row["expected contains"],
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

def flag(val):
    return val.strip().lower() == "true"

@pytest.mark.order(1)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,val,exp", rows)
def test_contains_csv_in(low, up, val, exp):
    inv = p.closed(parse(low), parse(up))
    res = parse(val) in inv
    assert res is flag(exp)

@pytest.mark.order(2)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,val,exp", rows)
def test_contains_csv_method(low, up, val, exp):
    inv = p.closed(parse(low), parse(up))
    res = inv.contains(parse(val))
    assert res is flag(exp)

@pytest.mark.order(3)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,val,exp", rows)
def test_contains_csv_singleton(low, up, val, exp):
    inv = p.closed(parse(low), parse(up))
    sub = p.singleton(parse(val))
    res = sub in inv
    assert res is flag(exp)

@pytest.mark.order(4)
@pytest.mark.csv
@pytest.mark.parametrize("low,up,val,exp", rows)
def test_contains_csv_intersection(low, up, val, exp):
    inv = p.closed(parse(low), parse(up))
    sub = p.singleton(parse(val))
    res = not (inv & sub).empty
    assert res is flag(exp)
