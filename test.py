import solution  # Asenda vastava failinimega

# ----------------------------
# students_study tests
# ----------------------------

def test_students_study_daytime():
    # Hommik ja lõuna (5..17)
    for t in [5, 10, 17]:
        assert solution.students_study(t, True) is True
        assert solution.students_study(t, False) is False

def test_students_study_evening_night():
    # Õhtu ja öö (18..24)
    for t in [18, 20, 24]:
        assert solution.students_study(t, True) is True
        assert solution.students_study(t, False) is True

def test_students_study_sleeping():
    # Magamise aeg (1..4)
    for t in [1, 2, 3, 4]:
        assert solution.students_study(t, True) is False
        assert solution.students_study(t, False) is False

# ----------------------------
# lottery tests
# ----------------------------

def test_lottery_all_fives():
    assert solution.lottery(5, 5, 5) == 10

def test_lottery_all_same_not_five():
    for x in [0, 1, -3, 7]:
        assert solution.lottery(x, x, x) == 5

def test_lottery_both_diff_from_a():
    # b ja c erinevad a-st
    assert solution.lottery(2, 3, 4) == 1

def test_lottery_one_same_as_a():
    # b või c võrdub a-ga
    assert solution.lottery(2, 2, 3) == 0
    assert solution.lottery(2, 3, 2) == 0
    assert solution.lottery(5, 5, 1) == 0

# ----------------------------
# fruit_order tests
# ----------------------------

def test_fruit_order_exact_small_only():
    assert solution.fruit_order(4, 0, 4) == 4
    assert solution.fruit_order(5, 0, 3) == 3
    assert solution.fruit_order(2, 0, 5) == -1

def test_fruit_order_exact_big_only():
    assert solution.fruit_order(0, 3, 15) == 0
    assert solution.fruit_order(0, 2, 10) == 0
    assert solution.fruit_order(0, 1, 10) == -1

def test_fruit_order_mix_small_big():
    assert solution.fruit_order(4, 1, 9) == 4
    assert solution.fruit_order(6, 2, 16) == 6
    assert solution.fruit_order(10, 3, 17) == 2

def test_fruit_order_not_enough():
    assert solution.fruit_order(1, 1, 10) == -1
    assert solution.fruit_order(2, 3, 20) == -1

def test_fruit_order_zero_order():
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(4, 5, 0) == 0
