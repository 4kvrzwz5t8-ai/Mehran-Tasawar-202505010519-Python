from food_order import calculate_total as food_order

def test_order1():
    assert food_order(10, 2) == 20

def test_order2():
    assert food_order(10, 3) == 30

def test_order3():
    assert food_order(20, 5) == 100

def test_order4():
    assert food_order(5, 2) == 10

def test_invalid_price():
    assert food_order(-10, 2) == "invalid price"

def test_invalid_quantity():
    assert food_order(10, -2) == "invalid quantity"