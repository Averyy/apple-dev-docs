# WebDriver

**Framework**: Safari Developer Features

Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver, including Safari.

#### Overview

WebDriver is a cross-browser API for automating testing of web content interactions on all major platforms and browsers, without requiring browser-specific code. Safari’s driver is called `safaridriver` and has a preset available in most Selenium client libraries. You can write tests in Python, Java, PHP, JavaScript, and any other language whose library is compatible with the W3C WebDriver protocol.

WebDriver is a REST API. It hosts a local web server that accepts REST-style HTTP requests, so it can accept automation commands from a wide variety of test setups.

To support WebDriver without sacrificing a user’s privacy or security, Safari’s driver provides extra safeguards to ensure that test execution is isolated from normal browsing data and from other test runs.

#### Isolated Automation Windows

Test execution is confined to special automation windows that are isolated from normal browsing windows, user settings, and preferences. You can recognize these windows by their orange Smart Search field. Like a private browsing session, an automation session starts from a clean slate. It can’t access Safari’s browsing history, AutoFill data, or other sensitive information available in a normal browsing session. These isolated sessions also help to ensure that tests are unaffected by a previous test session’s persistent state.

#### Glass Panes

To prevent any attempts to interact with the window or web content during a test, Safari installs a transparent “glass pane” over the automation windows while the browser is being used for WebDriver testing. This pane catches any stray interactions (mouse, keyboard, resizing, and so on) that could affect the automation window. If a running test gets stuck, you can interrupt it by “breaking” the glass pane and stopping the session. When an automation session is interrupted, the test’s connection to the browser is permanently severed, and the automation window remains open for further inspection, until closed manually.

#### One Session at a Time to Mimic User Interaction

Only one Safari browser instance can be active at any given time, and only one WebDriver session at a time can be attached to the browser instance. These constraints ensure that the simulated behavior (mouse, keyboard, touch, and so forth) accurately reflects what a user can do in a macOS windowing environment and prevents tests from competing with each other for window and keyboard focus.

## Topics

### Enabling WebDriver
- [Enable WebDriver on macOS](macos-enabling-webdriver.md)
  Enable WebDriver to automate testing of Safari on macOS.
- [Enable WebDriver on iOS and iPadOS](ios-enabling-webdriver.md)
  Enable WebDriver to automate testing of Safari on iOS and iPadOS using a connected Mac.

## See Also

- [Develop menu](develop-menu.md)
  Access tools for debugging webpages in Safari, as well as tools for debugging web content in other apps and on other devices.
- [Web Inspector](web-inspector.md)
  Use Web Inspector to inspect and debug your HTML, CSS, and JavaScript.
- [Responsive Design Mode](responsive-design-mode.md)
  Use Responsive Design Mode to test your `media` queries and other dynamic styles to ensure your webpages look great on any screen.
- [Inspect Apps and Devices](inspect-apps-and-devices.md)
  Discover all inspectable web content in Safari and other apps on your Mac and on connected devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/webdriver)*