from gift_shop import invalid_id, invalid_id_at_leat_twice


def test_invalid_id__return_true():
    assert invalid_id(11)
    assert invalid_id(1212)
    assert invalid_id(123123)
    assert invalid_id(12341234)
    assert invalid_id(1234512345)


def test_invalid_id__return_false():
    assert not invalid_id(1)
    assert not invalid_id(111)
    assert not invalid_id(112)
    assert not invalid_id(121212)
    assert not invalid_id(121213)
    assert not invalid_id(123123123)
    assert not invalid_id(123123125)
    assert not invalid_id(123412341234)
    assert not invalid_id(1234123412345)


def test_invalid_id_at_leat_twice__return_true():
    assert invalid_id_at_leat_twice(11)
    assert invalid_id_at_leat_twice(111)
    assert invalid_id_at_leat_twice(121212)
    assert invalid_id_at_leat_twice(123123123)
    assert invalid_id_at_leat_twice(123412341234)


def test_invalid_id_at_leat_twice__return_false():
    assert not invalid_id_at_leat_twice(1)
    assert not invalid_id_at_leat_twice(112)
    assert not invalid_id_at_leat_twice(121213)
    assert not invalid_id_at_leat_twice(123123125)
    assert not invalid_id_at_leat_twice(1234123412345)
