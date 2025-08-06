from source.Exercise4 import fahr_to_celsius, temp_classifier


def test_fahr_to_celsius():
    result = fahr_to_celsius(450)
    assert round(result) == 232


def test_temp_classifier():
    testCases = [(-18, 0), (-2, 1), (1, 1), (2, 2), (14, 2), (15, 3), (18, 3)]
    for temp, expected in testCases:
        assert temp_classifier(temp) == expected
