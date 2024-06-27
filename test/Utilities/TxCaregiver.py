import random
import string

import requests
from test.Profiles.ENTProfile import ENTProfile
from test.Testdata import Caregiver_Data


class CaregiverAPI:
    base_url = 'https://' + ENTProfile.ENV + '.hhaexchange.com/'

    ssn1 = ''.join(random.choices(string.digits, k=3))
    ssn2 = ''.join(random.choices(string.digits, k=2))
    ssn3 = ''.join(random.choices(string.digits, k=4))
    ssn = ssn1 + "-" + ssn2 + "-" + ssn3

    if ENTProfile.ENV == 'sandbox1':
        userId = 153208
        providerId = 7640
        #    officeId = 14992  # Texas - 14992, texas 1 - 15008
        genderId = 10379
    elif ENTProfile.ENV == 'cloud':
        # for cloud
        userId = 1049485
        providerId = 500940
        #    officeId = 5002196  # Texas - 5002196 texas 1 -5002197
        genderId = 42102

    @staticmethod
    def authorization():
        body = {
            "client_id": "HHAExchange.ENT.APP",
            "client_secret": "Md@Z#9eS8EW!lkkd1YhL29mZg114enhxWo",
            "grant_type": "client_credentials",
            "scope": "all:read"
        }
        url = CaregiverAPI.base_url + 'identity/connect/token'
        response = requests.post(url, body)
        token = response.json().get('access_token')
        return "Bearer " + token

    @staticmethod
    def create_skill_caregiver(caregiver_data):
        url = CaregiverAPI.base_url + ENTProfile.VERSION + '/api/Caregiver/CreateCaregiver'

        header = {
            "Content-Type": "application/json-patch+json",
            "Authorization": CaregiverAPI.authorization()
        }

        if ENTProfile.ENV == 'sandbox1' and caregiver_data['OfficeId'] == '5002197':
            caregiver_data['OfficeId'] = '15008'
        elif ENTProfile.ENV == 'sandbox1' and caregiver_data['OfficeId'] == '5002196':
            caregiver_data['OfficeId'] = '14992'

        data = {
            "userId": CaregiverAPI.userId,
            "providerId": CaregiverAPI.providerId,
            "offices": [
                {
                    "officeId": caregiver_data['OfficeId'],
                    "primary": True
                }
            ],
            "firstName": caregiver_data['FirstName'],
            "middleName": "",
            "lastName": caregiver_data['LastName'],
            "gender": {
                "id": CaregiverAPI.genderId,
                "value": "Male"
            },
            "dateOfBirth": "1994-04-04T00:00:00",
            "dependents": "",
            "alternateCode": "",
            "ssn": CaregiverAPI.ssn,
            "ethnicityId": -1,
            "mobileDetail": {
                "uniqueId": "",
                "type": 0,
                "deviceId": None
            },
            "rehireDate": "2018-01-01",
            "maritalStatus": -1,
            "countryOfBirth": "",
            "referralSource": None,
            "employmentType": [
                "RN",
                "Other (Skilled)"
            ],
            "referralPerson": "",
            "applicationDate": "2018-01-01T00:00:00",
            "hireDate": None,
            "type": 2,
            "caregiverStatus": {
                "status": 1,
                "reason": None,
                "notes": "",
                "changeDate": None,
                "terminationDate": None,
                "send105": False
            },
            "employeeId": "",
            "payrollAgreement": {
                "signed": False,
                "signedDate": None
            },
            "stateRegistry": {
                "number": None,
                "date": None
            },
            "profLicenseNumber": "",
            "npiNumber": "",
            "nycRegistryReferences": {
                "checkedOn": False,
                "checkedDate": None
            },
            "teamId": 0,
            "locationId": 0,
            "branchId": 0,
            "payers": None,
            "address": {
                "line1": "",
                "line2": "",
                "city": "NEW YORK",
                "state": "NY",
                "zipCode": "10001",
                "zip4": "1000",
                "phone1": "",
                "phone2": "",
                "phone3": ""
            },
            "emergencyContacts": [
                {
                    "name": "",
                    "relationshipId": None,
                    "address": "",
                    "phone1": "",
                    "phone2": "",
                    "relationshipOther": None
                }
            ],
            "notificationPreferences": {
                "contactMethod": None,
                "email": "",
                "textMessageNumber": "",
                "voiceMessageNumber": "",
                "excludeFromOpenShiftBroadcast": False,
                "carePathAlertEmail": {
                    "receiveAlertEmail": False,
                    "alertPriorities": [
                        {
                            "id": None,
                            "value": "undefined"
                        }
                    ]
                }
            },
            "updateStatus": None,
            "chatEnabled": None,
            "configureChatService": None,
            "enableMobileAppBioMatricTwoFactorAuthentication": None,
            "allowCommunityVisit": None,
            "transportationMethod": None,
            "oldFirstName": None,
            "oldLastName": None,
            "oldDateOfBirth": None,
            "oldSSN": None,
            "activationCode": None,
            "isMobileAppAccess": None,
            "externalSource": None,
            "externalID": None,
        }
        response = requests.post(url, headers=header, json=data)
        cg_id = response.json().get('caregiverId')

        # get cg-code
        cg_details_url = CaregiverAPI.base_url + ENTProfile.VERSION + '/api/Caregiver/GetCaregiverDetails'

        body = {
            "caregiverIds": [
                cg_id
            ]
        }

        cg_details_response = requests.post(cg_details_url, headers=header, json=body)
        cg_details = cg_details_response.json()
        cg_code = cg_details[0].get('caregiverCode')
        return cg_code

    @staticmethod
    def create_non_skill_caregiver(caregiver_data):
        url = CaregiverAPI.base_url + ENTProfile.VERSION + '/api/Caregiver/CreateCaregiver'

        if ENTProfile.ENV == 'sandbox1' and caregiver_data['OfficeId'] == '5002197':
            caregiver_data['OfficeId'] = '15008'
        elif ENTProfile.ENV == 'sandbox1' and caregiver_data['OfficeId'] == '5002196':
            caregiver_data['OfficeId'] = '14992'

        header = {
            "Content-Type": "application/json-patch+json",
            "Authorization": CaregiverAPI.authorization()
        }
        data = {
            "userId": CaregiverAPI.userId,
            "providerId": CaregiverAPI.providerId,
            "offices": [
                {
                    "officeId": caregiver_data['OfficeId'],
                    "primary": True
                }
            ],
            "firstName": caregiver_data['FirstName'],
            "middleName": "",
            "lastName": caregiver_data['LastName'],
            "gender": {
                "id": CaregiverAPI.genderId,
                "value": "Male"
            },
            "dateOfBirth": "1994-04-04T00:00:00",
            "dependents": "",
            "alternateCode": "",
            "ssn": CaregiverAPI.ssn,
            "ethnicityId": -1,
            "mobileDetail": {
                "uniqueId": "",
                "type": 0,
                "deviceId": None
            },
            "rehireDate": "2018-01-01",
            "maritalStatus": -1,
            "countryOfBirth": "",
            "referralSource": None,
            "employmentType": [
                "HHA", "PCA",
                "Other (Non Skilled)"
            ],
            "referralPerson": "",
            "applicationDate": "2018-01-01T00:00:00",
            "hireDate": None,
            "type": 2,
            "caregiverStatus": {
                "status": 1,
                "reason": None,
                "notes": "",
                "changeDate": None,
                "terminationDate": None,
                "send105": False
            },
            "employeeId": "",
            "payrollAgreement": {
                "signed": False,
                "signedDate": None
            },
            "stateRegistry": {
                "number": None,
                "date": None
            },
            "profLicenseNumber": "",
            "npiNumber": "",
            "nycRegistryReferences": {
                "checkedOn": False,
                "checkedDate": None
            },
            "teamId": 0,
            "locationId": 0,
            "branchId": 0,
            "payers": None,
            "address": {
                "line1": "",
                "line2": "",
                "city": "NEW YORK",
                "state": "NY",
                "zipCode": "10001",
                "zip4": "1000",
                "phone1": "",
                "phone2": "",
                "phone3": ""
            },
            "emergencyContacts": [
                {
                    "name": "",
                    "relationshipId": None,
                    "address": "",
                    "phone1": "",
                    "phone2": "",
                    "relationshipOther": None
                }
            ],
            "notificationPreferences": {
                "contactMethod": None,
                "email": "",
                "textMessageNumber": "",
                "voiceMessageNumber": "",
                "excludeFromOpenShiftBroadcast": False,
                "carePathAlertEmail": {
                    "receiveAlertEmail": False,
                    "alertPriorities": [
                        {
                            "id": None,
                            "value": "undefined"
                        }
                    ]
                }
            },
            "updateStatus": None,
            "chatEnabled": None,
            "configureChatService": None,
            "enableMobileAppBioMatricTwoFactorAuthentication": None,
            "allowCommunityVisit": None,
            "transportationMethod": None,
            "oldFirstName": None,
            "oldLastName": None,
            "oldDateOfBirth": None,
            "oldSSN": None,
            "activationCode": None,
            "isMobileAppAccess": None,
            "externalSource": None,
            "externalID": None,
        }
        response = requests.post(url, headers=header, json=data)
        cg_id = response.json().get('caregiverId')

        cg_details_url = CaregiverAPI.base_url + ENTProfile.VERSION + '/api/Caregiver/GetCaregiverDetails'

        body = {
            "caregiverIds": [
                cg_id
            ]
        }

        cg_details_response = requests.post(cg_details_url, headers=header, json=body)
        cg_details = cg_details_response.json()
        cg_code = cg_details[0].get('caregiverCode')
        return cg_code
