from datetime import date
import requests
import base64

class TestRail:

    def create_run(self):
        testrail_url = 'https://asahigroupholdingsqa.testrail.io/index.php?/api/v2/add_run/1'
        username = 'ravirajsinh.solanki@asahigroup-holdings.com'
        password = 'Raviraj#9822'
        auth = base64.b64encode(f'{username}:{password}'.encode()).decode()
        new_headers = {
            'Content-type': 'application/json',
            'Authorization': f'Basic {auth}'
        }

        today = date.today()
        run_name = 'WADRUN' + '_WAD_' + today.strftime("%d-%b-%Y")
        body = {
            'name': run_name,
            'include_all': False,
            'case_ids': [1]  # case_ids should be a list of integers, not strings
        }

        response = requests.post(url=testrail_url, json=body, headers=new_headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_json = response.json()
        return response_json['id']


    @staticmethod
    def add_results_for_cases(run_id, testcase_id, testcase_status, comment):

        username = 'ravirajsinh.solanki@asahigroup-holdings.com'
        password = 'Raviraj#9822'
        auth = base64.b64encode(f'{username}:{password}'.encode()).decode()
        new_headers = {
            'Content-type': 'application/json',
            'Authorization': f'Basic {auth}'
        }
        testrail_url = 'https://asahigroupholdingsqa.testrail.io/index.php?/api/v2/add_results_for_cases/' + run_id
       # new_headers = {'Content-type': 'application/json', 'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpIaGF4QDEyMw=='}
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