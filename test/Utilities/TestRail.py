import requests
from datetime import date
from test.Profiles.ENTProfile import ENTProfile
from test.Utilities.TestCaseID import tc_id
from test.Utilities.TexasTesCaseID import texas_tc_id


# from testrail_api import TestRailAPI

# api = TestRailAPI("https://hhax.testrail.net/", "yvirani@hhaexchange.com", "yash1239@HHA")


class TestRail:

    @staticmethod
    def update_run(run_id):
        desc = "URL - " + ENTProfile.BASE_URL + "\nUsername - " + ENTProfile.USERNAME
        testrail_url = 'https://hhax.testrail.net/index.php?/api/v2/update_run/' + str(run_id)
        new_headers = {'Content-type': 'application/json',
                       'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpIaGF4QDEyMw=='}
        body = {
            'description': desc
        }

        response = requests.post(url=testrail_url,
                                 json=body,
                                 headers=new_headers)

    @staticmethod
    def create_run():

        testrail_url = 'https://hhax.testrail.net/index.php?/api/v2/add_run/16'
        new_headers = {'Content-type': 'application/json',
                       'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpIaGF4QDEyMw=='}

        if ENTProfile.TEXAS:
            env = 'Texas_'
            testcase_id = texas_tc_id
        else:
            env = 'NewSkin_'
            testcase_id = tc_id

        if 'sandbox' in ENTProfile.BASE_URL:
            env += 'Sandbox'
        elif 'cloudsb' in ENTProfile.BASE_URL:
            env += 'CloudSB'
        elif 'app' in ENTProfile.BASE_URL:
            env += 'Prod'
        elif 'cloud' in ENTProfile.BASE_URL:
            env += 'Cloud'
        else:
            env += 'QA'

        today = date.today()
        run_name = env + '_ENT_Regression_' + today.strftime("%d-%b-%Y")
        body = {'name': run_name, 'include_all': False, 'case_ids': testcase_id}

        response = requests.post(url=testrail_url,
                                 json=body,
                                 headers=new_headers)

        response_json = response.json()
        TestRail.update_run(response_json['id'])
        return response_json['id']

    @staticmethod
    def get_run(run_id):
        testrail_url = 'https://hhax.testrail.net/index.php?/api/v2/update_run/' + str(run_id)
        print(testrail_url)
        new_headers = {'Content-type': 'application/json',
                       'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpIaGF4QDEyMw=='}

        response = requests.post(url=testrail_url,
                                 headers=new_headers)
        print(response.json())

    @staticmethod
    def add_results_for_cases(run_id, testcase_id, testcase_status, comment):

        testrail_url = 'https://hhax.testrail.net/index.php?/api/v2/add_results_for_cases/' + run_id
        new_headers = {'Content-type': 'application/json',
                       'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpIaGF4QDEyMw=='}
        body = {
            "results": [
                {
                    "case_id": testcase_id,
                    "status_id": testcase_status,
                    "comment": comment,
                }]
        }

        response = requests.post(url=testrail_url,
                                 json=body,
                                 headers=new_headers)
