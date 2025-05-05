from testcase import TestCase
from test_result import TestResult

class WasRun(TestCase):
    def set_up(self):
        self.log = "set_up "

    def test_method(self):
        self.log += "test_method "

    def tear_down(self):
        self.log += "tear_down"

class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        result = TestResult()
        test.run(result)
        expected = "set_up test_method tear_down"
        if test.log != expected:
            raise Exception(f"Esperado: '{expected}', mas obteve: '{test.log}'")
        print("Teste passou!")

if __name__ == "__main__":
    print("Rodando TestCaseTest...")
    test = TestCaseTest("test_template_method")
    result = TestResult()
    test.run(result)
    print(result.summary())  # Adiciona saída do resumo real
