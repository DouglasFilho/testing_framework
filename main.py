from test_case_test import TestCaseTest
from test_spy_test import TestSpyTest
from test_suite_test import TestSuiteTest
from test_result import TestResult
from test_suite import TestSuite

print("🚀 Executando todos os testes com TestSuite...\n")

suite = TestSuite()

# Adiciona todos os testes da classe TestCaseTest
for name in [
    "test_result_success_run",
    "test_result_failure_run",
    "test_result_error_run",
    "test_result_multiple_run"
]:
    suite.add_test(TestCaseTest(name))

# Adiciona todos os testes da classe TestSpyTest
for name in [
    "test_was_set_up",
    "test_was_run",
    "test_was_tear_down",
    "test_template_method"
]:
    suite.add_test(TestSpyTest(name))

# Adiciona todos os testes da classe TestSuiteTest
for name in [
    "test_suite_size",
    "test_suite_success_run",
    "test_suite_multiple_run"
]:
    suite.add_test(TestSuiteTest(name))

# Executa tudo
result = TestResult()
suite.run(result)
print("\n✅ Resumo final:")
print(result.summary())
