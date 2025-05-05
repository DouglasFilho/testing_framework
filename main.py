from test_runner import TestRunner
from test_case_test import TestCaseTest
from test_spy_test import TestSpyTest
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest

print("🚀 Executando testes com TestRunner...\n")

runner = TestRunner()
runner.run(
    TestCaseTest,
    TestSpyTest,
    TestSuiteTest,
    TestLoaderTest
)
