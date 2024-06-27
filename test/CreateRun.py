from test.Utilities.TestRail import TestRail


class TestCreateRun:

    def test_create_run(self):
        run_id = TestRail.create_run()
        print(run_id)
        f = open("run", "w")
        f.write(str(run_id))
        f.close()
