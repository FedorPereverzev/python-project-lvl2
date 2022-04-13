from diff import generate_diff


text = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'

def test_diff():
    assert generate_diff('./diff/tests/fixtures/file1.json', './diff/tests/fixtures/file2.json') == text

    