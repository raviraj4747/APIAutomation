import time
from result import CommonActions


testcase_name = "C3931394"

class TestSearchPatient():

    def test_C3931394(self):
            time.sleep(20000)
            try:
                a = 10
                b = 20
                assert a == b
            except:
                CommonActions.mark_fail()
                print("fail")
            else:
                CommonActions.mark_pass()
                print("pass")


