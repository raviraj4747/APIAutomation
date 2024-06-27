import traceback
from test.Profiles.ENTProfile import ENTProfile
from test.Utilities.TestRail import TestRail


# f = open("run", "r")
# run_id = f.read()
# run_id = '21382'


class CommonActions:

    @staticmethod
    def mark_pass(driver, testcase_name):
        testcase_id = int(testcase_name[1:])
        traceback_info = 'Testcase Passed Successfully'
        driver.save_screenshot('Pass_' + testcase_name + '.png')

    # if ENTProfile.PUSH_TO_RESULT:
    #     TestRail.add_results_for_cases(run_id, testcase_id, 1, traceback_info)

    @staticmethod
    def mark_fail(driver, testcase_name):
        testcase_id = int(testcase_name[1:])
        traceback_info = traceback.format_exc()
        driver.save_screenshot('Fail_' + testcase_name + '.png')
        # if ENTProfile.PUSH_TO_RESULT:
        #    TestRail.add_results_for_cases(run_id, testcase_id, 5, traceback_info)
        assert False
