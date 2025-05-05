class TestCase:
    def __init__(self, method_name):
        self.method_name = method_name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.method_name)
            method()
        except AssertionError:
            result.add_failure(self.method_name)
        except Exception:
            result.add_error(self.method_name)
        self.tear_down()

    def assert_equals(self, expected, actual):
        if expected != actual:
            raise AssertionError(f"Esperado: {expected}, mas recebeu: {actual}")

    def assert_true(self, condition):
        if not condition:
            raise AssertionError(f"Esperava condição verdadeira, mas recebeu False.")

    def assert_false(self, condition):
        if condition:
            raise AssertionError(f"Esperava condição falsa, mas recebeu True.")