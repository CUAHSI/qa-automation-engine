""" Contains the general, non-page specific utilities for test case
 execution.  Unlike hc_macros or hs_macros, these methods interact
directly with the Selenium driver
"""
import time

from modes import setup_mode

# General testing parameters
MODE_SELECTION = 'safe-demo'  # quick, watch, demo, or safe-demo
global SLEEP_TIME
SLEEP_TIME = setup_mode(MODE_SELECTION)


class External:
    """ Utilities for handling new tabs/windows """
    def switch_new_page(self, driver):
        win_handle = driver.window_handles[-1]
        driver.switch_to.window(win_handle)
        time.sleep(SLEEP_TIME)

    def switch_old_page(self, driver):
        win_handle = driver.window_handles[-2]
        driver.switch_to.window(win_handle)
        time.sleep(SLEEP_TIME)

    def close_new_page(self, driver):
        orig_handle = driver.current_window_handle
        new_handle = driver.window_handles[-1]
        driver.switch_to.window(new_handle)
        time.sleep(SLEEP_TIME/2)
        driver.close()
        driver.switch_to.window(orig_handle)
        time.sleep(SLEEP_TIME/2)

    def source_new_page(self, driver):
        orig_handle = driver.current_window_handle
        new_handle = driver.window_handles[-1]
        driver.switch_to.window(new_handle)
        time.sleep(SLEEP_TIME/2)
        source = driver.page_source
        driver.switch_to.window(orig_handle)
        time.sleep(SLEEP_TIME/2)
        return source


class TestSystem:
    """ General utilities for Hydroclient test case creation """
    def title(self, driver):
        return driver.title

    def wait(self, seconds=3):
        time.sleep(seconds)

    def page_source(self, driver):
        return driver.page_source

    def back(self, driver, count=1):
        driver.execute_script("window.history.go(-{})".format(count))


External = External()
TestSystem = TestSystem()
