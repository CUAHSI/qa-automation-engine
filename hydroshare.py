""" Runs various smoke tests for the hydroshare.org """
import unittest
import argparse
import sys
import os
import time
from modes import setup_mode
from selenium import webdriver
from hydroshare_elements import *

# Test case parameters
MODE_SELECTION = 'demo'
SLEEP_TIME = setup_mode(MODE_SELECTION)
BASE_URL = "http://www.hydroshare.org" # Default

# Test cases definition
class HydroshareTestCase(unittest.TestCase):
    """ Python unittest setup for smoke tests """

    def setUp(self):
        """ Setup driver for use in automation tests """
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "CUAHSI-QA-Selenium")
        global driver
        if infrastructure == 'grid':
            driver = webdriver.Remote(command_executor='http://' + \
                                      grid_hub_ip + ':4444/wd/hub',
                                      desired_capabilities={'browserName': 'firefox'})
        else:
            driver = webdriver.Firefox(profile)
        driver.get(BASE_URL)
        driver.implicitly_wait(10)

    def tearDown(self):
        """ Tear down test environment after execution """
        driver.quit()

    def test_B_000003(self):
        """ Confirms Beaver Divide Air Temperature resource
        landing page is online via navigation and title check,
        then downloads the BagIt archive and confirms
        """
        def oracle():
            """ The Beaver Divide BagIt zip file
            matches expected file size
            """
            self.assertTrue(file_size == 512000)
        # Pulls up discover search page through site header
        HomePage.discover_tab.click(driver, SLEEP_TIME)
        # Filters by subject of iUTAH in left panel
        DiscoverPage.filter_iutah_subject.click(driver, SLEEP_TIME)
        # Filters by resouce type of Generic in left panel
        DiscoverPage.filter_generic_resource.click(driver, SLEEP_TIME)
        # Filters by availability of Discoverable or Public
        DiscoverPage.filter_is_discoverable.click(driver, SLEEP_TIME)
        DiscoverPage.filter_is_public.click(driver, SLEEP_TIME)
        # Clicks specific resourse - Beaver Divide Air Temperaure
        DiscoverPage.beaver_divide.click(driver, SLEEP_TIME)
        # Checks download button exists with text for "Download" and "BagIt"
        download_href = ResourceLanding.download_bagit.get_href(driver, BASE_URL)
        # Download the BagIt zip file
        os.system('wget ' + download_href)
        # Get the files size of the downloaded BagIt zip file
        download_file = download_href.split('/')[-1]
        file_size = os.stat(download_file).st_size
        # Confirm the downloaded file size matches expectation
        oracle()

    def todo_test_B_000004(self):
        """ Confirms date filtering functionality, as well as
        map view functionality
        """
        def oracle():
            """ Confirms valid page returned after navigation """
            self.assertTrue('HydroShare' in driver.title)
        # Pulls up discover search page through site header
        HomePage.discover_tab.click(driver, SLEEP_TIME)
        DiscoverPage.start_date.inject_text(driver, "01/01/2014", SLEEP_TIME)
        DiscoverPage.end_date.inject_text(driver, "12/31/2014", SLEEP_TIME)
        # TODO fix element identification issue
        DiscoverPage.map_tab.click(driver, SLEEP_TIME)
        DiscoverPage.map_search.inject_text(driver, "Salt Lake City", SLEEP_TIME)
        DiscoverPage.map_submit.click(driver, SLEEP_TIME)
        DiscoverPage.list_tab.click(driver, SLEEP_TIME)
        time.sleep(5)
        oracle()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--grid')
    parser.add_argument('unittest_args', nargs='*')
    
    args = parser.parse_args()
    if args.grid is None:
        infrastructure = 'standalone'
    else:
        infrastructure = 'grid'
        grid_hub_ip = args.grid
        
    # Set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main(verbosity=2)
