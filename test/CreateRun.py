from testrail import TestRail

class TestCreateRun:

    def test_create_run(self):
        pass
        run_id = TestRail.create_run(self)
        print(run_id)
        f = open("run", "w")
        f.write(str(run_id))
        f.close()
