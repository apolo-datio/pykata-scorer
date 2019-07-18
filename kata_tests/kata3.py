def sum_digits_pow_test(kata: callable):
    assert list(kata(1, 10)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(kata(1, 100)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    assert list(kata(10, 89)) == [89]
    assert list(kata(10, 100)) == [89]
    assert list(kata(90, 100)) == []
    assert list(kata(89, 135)) == [89, 135]

kata_test = sum_digits_pow_test