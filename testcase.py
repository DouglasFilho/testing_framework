class TestCase:
    def __init__(self, method_name):
        self.method_name = method_name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.start_test()
        self.set_up()
        try:
            method = getattr(self, self.method_name)
            method()
            result.add_success()
        except Exception as e:
            result.add_failure()
            print(f"Erro no teste '{self.method_name}': {e}")
        self.tear_down()
