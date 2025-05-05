from testcase import TestCase

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False  # vai gerar um AssertionError

    def test_error(self):
        raise Exception("Erro inesperado")  # vai gerar um erro
