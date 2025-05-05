from test_result import TestResult
from test_case_test import TestCaseTest
from test_stub import TestStub

print("🚀 Executando todos os testes do framework...\n")

result = TestResult()

test_case_tests = [
    "test_result_success_run",
    "test_result_failure_run",
    "test_result_error_run",
    "test_result_multiple_run"
]

for test_name in test_case_tests:
    test = TestCaseTest(test_name)
    test.run(result)

print("\n✅ Resumo dos testes:")
print(result.summary())
