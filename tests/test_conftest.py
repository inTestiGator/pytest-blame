""" Tests the conftest.py plugin for pytest """


# def test_conftest(testdir, capsys):
#     """Make sure that our plugin works."""
#     testdir.makepyfile(
#         """
# def add(a, b):
#     return a + b
#
# def test_add():
#     assert add(1, 1) == 2
#     assert add(0, 1) != 2
# """
#     )
#     testdir.runpytest("--track")
#     standard_out, standard_err = capsys.readouterr()
#     assert "Cannot find the last passing commit" in standard_out
#     assert standard_err == ""
