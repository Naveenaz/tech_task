
Pre requisites:

Download and install Python 3.x.

Either install via Homebrew : https://docs.python-guide.org/starting/install3/osx/

Or download via https://www.python.org/downloads/

Once installed check the version number : python3 --version It should return 3.x


##############
Steps to do set up


Install all dependencies. Navigate to the project root folder and do the following:

pip3 install -r requirements.txt --user

Install ChromeDriver from brew (make sure chromedriver supports your version of chrome)

brew install chromedriver

or

https://chromedriver.chromium.org/downloads

###
Running tests:

To run individual test:

python3 -m pytest -s api_tests.py::APITester::test_api_response_contact_info


To run suites:

python3 -m pytest -s api_tests.py

Please see sample output in output/output.txt.