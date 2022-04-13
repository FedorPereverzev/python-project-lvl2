from diff import generate_diff


text = open("./diff/tests/fixtures/result.txt", "r")
fix1 = './diff/tests/fixtures/file1.json'
fix2 = './diff/tests/fixtures/file2.json'


def test_diff():
    assert generate_diff(fix1, fix2) == text.read()
