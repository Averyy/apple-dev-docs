# Testing with WebDriver in Safari

**Framework**: WebKit

Enable WebDriver and run a test.

#### Overview

This article walks you through the process of setting up WebDriver and running a test written in Python. When a test calls a command, the command is executed in the following steps:

1. The client library translates each command into a REST API command.
2. The REST API command sends the corresponding HTTP request to a local web server hosted by Safari’s driver.
3. The driver validates the HTTP request’s contents and forwards the command to the appropriate browser instance.
4. When a command has finished executing, the driver sends an HTTP response for the REST API command. The client library interprets the HTTP response and returns the result to the test code.

##### Make Sure You Have Safaris Webdriver

Safari and Safari Technology Preview each provide their own `safaridriver` executable. Make sure you already have the executable on your device:

- Safari’s executable is located at `/usr/bin/safaridriver`.
- Safari Technology Preview’s executable is part of the application bundle’s contents.

Each `safaridriver` is capable of launching only the Safari version it’s associated with, and the two can run simultaneously. Although you can launch `safaridriver` manually by running a `safaridriver` executable, most Selenium libraries launch the driver automatically. See the documentation for your preferred client library to learn how to specify which browser to use.

##### Get the Correct Selenium Library Version

Grab a recent release of the [`Selenium`](https://developer.apple.comhttps://www.seleniumhq.org/download/) open source project. Selenium’s Java and Python client libraries offer support for Safari’s native driver implementation starting in the 3.0.0-beta1 release.

> ❗ **Important**:  Don’t use the old SafariDriver implementation, which is no longer supported by the Selenium project. The Apple-developed driver is a replacement for the legacy SafariDriver formerly maintained by the Selenium project.

##### Configure Safari to Enable Webdriver Support

Safari’s WebDriver support for developers is turned off by default. How you enable it depends on your operating system.

Run `safaridriver --enable` once. (If you’re upgrading from a previous macOS release, you may need to use `sudo`.)

1. If you haven’t already done so, make the Develop menu available. Choose Safari > Preferences, and on the Advanced tab, select “Show Develop menu in menu bar.” For details, see [`Safari Help`](https://developer.apple.comhttps://support.apple.com/guide/safari/welcome).
2. Choose Develop > Allow Remote Automation.
3. Authorize `safaridriver` to launch the XPC service that hosts the local web server. To permit this, manually run `/usr/bin/safaridriver` once and follow the authentication prompt.

##### Write a Webdriver Testing Suite

Once you’ve obtained a client library, you can write a WebDriver test and run it against Safari. The example below uses using Python WebDriver to test important functionality of the [`WebKit Feature Status`](https://developer.apple.comhttps://webkit.org/status/) page.

> **Note**:  In the Python WebDriver library, each method call synchronously blocks processes until the operation completes. Other WebDriver libraries may provide an asynchronous API.

```python
#coding: utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time

def setup_module(module):
    WebKitFeatureStatusTest.driver = webdriver.Safari()

def teardown_module(module):
    WebKitFeatureStatusTest.driver.quit()


class WebKitFeatureStatusTest(unittest.TestCase):
    
    def test_feature_status_page_search(self):
        self.driver.get("https://webkit.org/status/")
            
        # Enter "CSS" into the search box.
        # Ensures that at least one result appears in search
        search_box = self.driver.find_element_by_id("search")
        search_box.send_keys("CSS")
        value = search_box.get_attribute("value")
        self.assertTrue(len(value) > 0)
        search_box.submit()
        time.sleep(1)
        # Count the visible results when filters are applied
        # so one result shows up in at most one filter
        feature_count = self.shown_feature_count()
        self.assertTrue(feature_count > 0)
        
    def test_feature_status_page_filters(self):
        self.driver.get("https://webkit.org/status/")
            
        time.sleep(1)
        filters = self.driver.execute_script("return document.querySelectorAll('.filter-toggle')")
        self.assertTrue(len(filters) is 7)
        
        # Make sure every filter is turned off.
        for checked_filter in filter(lambda f: f.is_selected(), filters):
            checked_filter.click()
        
        # Make sure you can select every filter.
        for filt in filters:
            filt.click()
            self.assertTrue(filt.is_selected())
            filt.click()
    
    def shown_feature_count(self):
                return len(self.driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))


if __name__ == "__main__":
    unittest.main()
```

##### Run Your Test

Copy and save the test code above as `test_webkit.py` and run the following:

```bash
python test_webkit.py
```

## See Also

- [macOS WebDriver Commands for Safari 11.1 and earlier](macos-webdriver-commands-for-safari-11-1-and-earlier.md)
  Test your web content using the WebDriver commands supported by Safari 11.1 and earlier.
- [macOS WebDriver Commands for Safari 12 and later](macos-webdriver-commands-for-safari-12-and-later.md)
  Test your web content using the WebDriver commands supported by Safari 12 and later.
- [About WebDriver for Safari](about-webdriver-for-safari.md)
  Enhance testing of your web content using Safari’s enhancements to WebDriver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/testing-with-webdriver-in-safari)*