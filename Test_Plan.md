
## Pre requisites: ##
You need software build to run the tests.Please find test environment details here.

https://github.com/smcostareisHopin/Hopin-Exam-QE/blob/main/TestEnvironment.md

## Assumptions: ##
For UI tests only Chrome browser has been used for testing.


# TEST PLAN 


Test environment:
OS : macOS Big Sur
Browser: Chrome

## Test Setup

1. Get software build image and install/start the session - https://github.com/smcostareisHopin/Hopin-Exam-QE 


## UI Tests

This test plan consists of two parts viz. UI Tests and API tests.

### UI tests 1 

Test submit button without adding value in name field.

EXPECT:

1. Should get alert on browser.


### UI tests 2

1. Enter name value
2. Press submit button

EXPECT:

1. Successfully navigates to next UI 
2. On UI we should see customer list table

### UI tests 3

1. Enter name value
2. Press submit button
3. Click on any single row
3. Go to next screen and should see all details including conact details.

EXPECT:

1. Successfully navigates to next UI 
2. On UI we should see customer list table
3. Go to next screen and should see all details including conact details.

### UI tests 4

1. Enter name value
2. Press submit button
3. Click on any row.
4. Go to next screen and should see all details including conact details.
5. Hit back button
6. Repeat step 3 and 4

EXPECT:

1. Successfully navigates to next UI 
2. On UI we should see customer list table
3. Go to next screen and should see all details including conact details for each customer.

### UI tests 4

1. Enter name value
2. Press submit button
3. Click on any row.
4. Go to next screen and should see all details including conact details.
5. Hit back button
6. Repeat step 3 and 4

EXPECT:

1. Successfully navigates to next UI 
2. On UI we should see customer list table
3. Go to next screen and should see all details including conact details for each customer.


## API Tests

### API tests 1 

1. Check whether you receive successful API response for post method.

EXPECT:

1. Should receive API response with all customer details.

### API tests 2

1. Check whether each customer has contact info

EXPECT:

1. Contact info should be present for each customer.

### API tests 3

1. Check whether size has been assigned correctly based on Employees count.
Condition : customer size is: Small, when # of employees is <= 10; Medium when it is <= 1000; Big otherwise.
    def test_api_response_size(self):

EXPECT:

1.  customer size should be: Small, when # of employees is <= 10; Medium when it is <= 1000; Big otherwise.



