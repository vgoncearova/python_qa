__author__ = "victoria"

# Create test files
def test_one():
    print(" >>> I'm test one!")

# Create test classes
class TestClass:

    def test_one(self):
        pass

    def test_two(self):
        pass

# Run of separate files, functions, classes
# pytest 0_pytest_intro/
# pytest 0_pytest_intro/test_pytest_intro_1.py
# pytest 0_pytest_intro/test_pytest_intro_1.py::TestClass
# pytest 0_pytest_intro/test_pytest_intro_1.py::test_one


