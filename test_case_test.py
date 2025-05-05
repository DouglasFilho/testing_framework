from testcase import TestCase

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
        result = DummyResult()
        test.run(result)
        expected = "set_up test_method tear_down"
        if test.log != expected:
            raise Exception(f"Esperado: '{expected}', mas obteve: '{test.log}'")
        print("Teste passou!")

class DummyResult:
    def start_test(self): print("Iniciando teste...")
    def add_success(self): print("Teste bem-sucedido.")
    def add_failure(self): print("Teste falhou.")

if __name__ == "__main__":
    print("Rodando TestCaseTest...")
    test = TestCaseTest("test_template_method")
    result = DummyResult()
    test.run(result)
