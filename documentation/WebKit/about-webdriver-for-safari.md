# About WebDriver for Safari

**Framework**: WebKit

Enhance testing of your web content using Safari’s enhancements to WebDriver.

#### Overview

WebDriver, [`Selenium`](https://developer.apple.comhttps://github.com/seleniumhq/selenium)’s cross-platform, cross-browser API, automates testing of web content interactions on all major platforms and browsers, without requiring browser-specific code. Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver. Safari’s driver is called `safaridriver` and has a preset available in most Selenium client libraries. You can write tests in Python, Java, PHP, JavaScript, and any other language whose library is compatible with the W3C WebDriver protocol.

WebDriver is a REST API. It hosts a local web server that accepts REST-style HTTP requests, so it can accept automation commands from a wide variety of test setups.

To support WebDriver without sacrificing a user’s privacy or security, Safari’s driver provides extra safeguards to ensure that test execution is isolated from normal browsing data and from other test runs. The driver is available in Safari 10 or later.

##### Isolated Automation Windows

Test execution is confined to special automation windows that are isolated from normal browsing windows, user settings, and preferences. You can recognize these windows by their orange Smart Search field. Like a private browsing session, an automation session always starts from a clean slate. It can’t access Safari’s browsing history, AutoFill data, or other sensitive information available in a normal browsing session. These isolated sessions also help to ensure that tests are unaffected by a previous test session’s persistent state.

![Screenshot of an automation window with an orange Smart Search field. ](https://docs-assets.developer.apple.com/published/7851ca0bd577ad0b59391f86ed6d62c5/media-2957225%402x.png)

##### Glass Panes

To prevent any attempts to interact with the window or web content during a test, Safari installs a transparent “glass pane” over the automation windows while the browser is being used for WebDriver testing. This pane catches any stray interactions (mouse, keyboard, resizing, and so on) that could affect the automation window. If a running test gets stuck, you can interrupt it by “breaking” the glass pane and stopping the session. When an automation session is interrupted, the test’s connection to the browser is permanently severed, and the automation window remains open for further inspection, until closed manually.

![Screenshot of the dialog that appears when you try to break the glass pane. The dialog presents three buttons: Turn Off All Automation, Stop Session, and Continue Session](https://docs-assets.developer.apple.com/published/52ae8d370de587d6419aae6277ed4c3a/media-2957221%402x.png)

##### Web Inspector and Webdriver

You can use Web Inspector during and after the execution of a WebDriver test. Web Inspector features such as console logging, the Elements tab, and the script debugger are fully functional when running WebDriver tests. Choose the Develop > Show Web Inspector menu item (shortcut: ⌥⌘I) to launch Web Inspector while a test is running.

##### Webdriver Commands for Debugging

You can specify some WebDriver capabilities in a New Session request to assist debugging:

- `safari:automaticInspection`—When passed the `safari:automaticInspection` capability in a New Session request, `safaridriver` preloads the Web Inspector and JavaScript debugger in the background. To pause test execution and bring up Web Inspector’s Debugger tab, evaluate a `debugger;` statement in the test page.
- `safari:automaticProfiling`—When passed the `safari:automaticProfiling` capability in a New Session request, `safaridriver` preloads Web Inspector and starts a timeline recording in the background. Open the Timelines tab in Web Inspector to see the captured timeline recording in its entirety.

##### One Session at a Time to Mimic User Interaction

Only one Safari browser instance can be active at any given time, and only one WebDriver session at a time can be attached to the browser instance. These constraints ensure that the  simulated behavior (mouse, keyboard, touch, and so forth) accurately reflects what a user can do in a macOS windowing environment and prevents tests from competing with each other for window and keyboard focus.

## See Also

- [macOS WebDriver Commands for Safari 11.1 and earlier](macos-webdriver-commands-for-safari-11-1-and-earlier.md)
  Test your web content using the WebDriver commands supported by Safari 11.1 and earlier.
- [macOS WebDriver Commands for Safari 12 and later](macos-webdriver-commands-for-safari-12-and-later.md)
  Test your web content using the WebDriver commands supported by Safari 12 and later.
- [Testing with WebDriver in Safari](testing-with-webdriver-in-safari.md)
  Enable WebDriver and run a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/about-webdriver-for-safari)*