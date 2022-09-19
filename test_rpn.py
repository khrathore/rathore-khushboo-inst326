import rpn
import math as mt

def test_happy_paths():
    assert rpn.evaluate("2 3 +") == 5
    assert rpn.evaluate("2 3 -") == -1
    assert rpn.evaluate("2 3 *") == 6
    floatev = rpn.evaluate("2 3 /")
    assert mt.isclose(floatev, .6666666666666)
    assert rpn.evaluate("7 5 1 + -") == 1
    assert rpn.evaluate("7 5 + 1 -") == 11
    
def test_edge_cases():
    assert rpn.evaluate("8") == 8
    floatans = rpn.evaluate(".6666666666666")
    assert mt.isclose(floatans, .6666666666666)
    assert rpn.evaluate("-5 6 +") == 1
    assert rpn.evaluate("12 7 -") == 5