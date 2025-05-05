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
