import unittest
import requests
import json
from pprint import pprint


class APITester(unittest.TestCase):
    api_payload = {
        "name": "qa_engineer_exam_app_backend"
    }

    endpoint = "http://localhost:3001"

    def test_api_response(self):
        response = requests.request("POST", self.endpoint, json=self.api_payload, timeout=10)
        self.assertRegex(str(response.status_code), "20[0-2]")
        pprint(response.text)
        pprint(response.status_code)

    def test_api_response_contact_info(self):
        response = requests.request("POST", self.endpoint, json=self.api_payload, timeout=10)
        self.assertRegex(str(response.status_code), "20[0-2]")
        pprint(response.text)
        pprint(response.status_code)
        json_data = json.loads(response.text)
        pprint(json_data)

        for customer in json_data['customers']:
            print(customer['name'])
            try:
                print(customer['contactInfo'])
            except KeyError:
                self.fail('contactInfo is missing for ' + customer['name'])

    # Specification - customer size is: Small, when # of employees is <= 10; Medium when it is <= 1000; Big otherwise.
    def test_api_response_size(self):
        response = requests.request("POST", self.endpoint, json=self.api_payload, timeout=10)
        self.assertRegex(str(response.status_code), "20[0-2]")
        pprint(response.text)
        pprint(response.status_code)
        json_data = json.loads(response.text)
        pprint(json_data)

        failed_tests = []

        for customer in json_data['customers']:
            print(customer['name'])
            print(customer['employees'])
            print(customer['size'])

            if customer['employees'] <= 10:
                if customer['size'] != 'Small':
                    failed_tests.append(customer['name'])
                #self.assertEqual('Small', customer['size'], 'Expected size is not correct for ' + customer['name'])
            elif customer['employees'] <= 1000:
                if customer['size'] != 'Medium':
                    failed_tests.append(customer['name'])
                #self.assertEqual('Medium', customer['size'], 'Expected size is not correct for ' + customer['name'])
            elif customer['employees'] > 1000:
                #self.assertEqual('Big', customer['size'], 'Expected size is not correct for ' + customer['name'])
                if customer['size'] != 'Big':
                    failed_tests.append(customer['name'])
            else:
                pass

        self.assertEqual(0, len(failed_tests), 'Size do not match spec for these ' + str(failed_tests))





