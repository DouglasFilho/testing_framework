from test_loader import TestLoader
from test_result import TestResult

class TestRunner:
    def run(self, *test_classes):
        loader = TestLoader()
        result = TestResult()

        for test_class in test_classes:
            suite = loader.load_tests_from_class(test_class)
            suite.run(result)

        print("\n✅ Resultado dos testes:")
        print(result.summary())
