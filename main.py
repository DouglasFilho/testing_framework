from test_case_test import TestCaseTest
from test_spy_test import TestSpyTest
from test_result import TestResult

print("🚀 Executando todos os testes...\n")

result = TestResult()

test_case_tests = [
    "test_result_success_run",
    "test_result_failure_run",
    "test_result_error_run",
    "test_result_multiple_run"
]

test_spy_tests = [
    "test_was_set_up",
    "test_was_run",
    "test_was_tear_down",
    "test_template_method"
]

for test_name in test_case_tests:
    TestCaseTest(test_name).run(result)

for test_name in test_spy_tests:
    TestSpyTest(test_name).run(result)

print("\n✅ Resumo final:")
print(result.summary())
