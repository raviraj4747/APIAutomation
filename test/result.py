import traceback
from testrail import TestRail
f = open("run", "r")
run_id = f.read()

class CommonActions:

    @staticmethod
    def mark_pass():
        print("mark_pass called")
        traceback_info = 'Testcase Passed Successfully'
        TestRail.add_results_for_cases(run_id, 1, 1, traceback_info)

    @staticmethod
    def mark_fail():
        print("mark_fail called")
        traceback_info = 'Testcase failed Successfully'
        TestRail.add_results_for_cases(run_id, 1, 5, traceback_info)
