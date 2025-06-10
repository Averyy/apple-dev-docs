# Develop menu

**Framework**: Safari Developer Features

Access tools for debugging webpages in Safari, as well as tools for debugging web content in other apps and on other devices.

#### Overview

The  menu is home to the tools available to design and develop web content in Safari, as well as web content used by other applications on your Mac and other devices. The  menu also provides quick access to [`Changing Developer settings in Safari on macOS`](developer-settings.md) and [`Changing Feature Flag settings in Safari on macOS`](feature-flag-settings.md).

> **Note**: If you haven’t already enabled features for web developers in Safari, follow the instruction for [`Enabling features for web developers`](enabling-developer-features.md). Once enabled, the  menu will be shown in the menu bar for Safari.

![Develop menu open, with an iPad attached showing three inspectable items for the iPad, a webpage, a Home Screen web app, and a service worker.](https://docs-assets.developer.apple.com/published/8f94ecb74ec50470120bfb2bf877196c/DevelopMenu%402x.png)

#### Open Page with

The  menu shows you other apps and simulators you can open the current webpage in. Other browsers on your Mac are listed here, like Safari Technology Preview, allowing you to quickly open a page in another browser.

If you have Xcode installed, you’ll also see a list of available iOS, iPadOS, and visionOS simulators here. Select a simulator to test your page across different device sizes and OS versions. If you don’t have Xcode installed, or want to add more simulators, see [`Installing Xcode and Simulators`](installing-xcode-and-simulators.md) and [`Adding additional simulators`](adding-additional-simulators.md).

#### User Agent

Browsers send a string that identifies the browser type to servers, called the User Agent. This same string is also available via JavaScript. You can change the User Agent to ensure that your site behaves the same regardless of the reported User Agent, or to debug a webpage that uses the User Agent string to enable functionality instead of feature detection.

> ❗ **Important**: Use feature detection to enable or disable functionality instead of relying on the name or version of the browser in the User Agent string. [`Learn how to detect available features on MDN…`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Feature_detection)

#### Devices and Simulators

Safari in macOS can inspect web content running in other applications in macOS, as well as inspect Safari, Home Screen web apps, Service Workers, and other apps in iOS, iPadOS ([`Inspecting iOS and iPadOS`](inspecting-ios.md)), and visionOS ([`Inspecting visionOS`](inspecting-visionos.md)) and JavaScript and TVML in tvOS ([`Inspecting tvOS`](inspecting-tvos.md)).

The Develop menu displays your Mac here and shows Mac web apps and other apps that have enabled inspection of their web content (see [`Enabling inspecting content in your apps`](enabling-inspecting-content-in-your-apps.md)). The Develop menu lists each inspectable device or simulator with their name and OS version to make it easier to find the specific device you want to inspect.

Each device (including the Mac you are using) and simulator has its own menu that lists the inspectable content on that device, as well as device-specific options. Not all options are available for all devices, and each option only applies to a specific device or simulator, not all of them.

#### Service Workers

[`Service Workers`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) are shared between webpages and don’t necessarily belong to any individual webpage. For this reason, they are inspectable separately from webpages in Safari.

When a service worker is running it will appear in the  menu.

#### Web Extension Background Content

Web Extension Background Content includes background pages and service workers which are scripts that run separately from webpages for each extension. These scripts, housing the core logic of a web extension, are responsible for preserving the extension’s state and reacting to extension-specific events. [`Learn more about debugging web extensions…`](https://developer.apple.comhttps://developer.apple.com/documentation/safariservices/safari_web_extensions/troubleshooting_your_safari_web_extension#3734523)

#### Responsive Design Mode

The  item allows you to use [`Responsive Design Mode`](responsive-design-mode.md) to test how your webpage adapts to various viewport sizes, as well as different display pixel ratios. While in Responsive Design Mode you can exit it using the  item.

#### Web Inspector

[`Web Inspector`](web-inspector.md) allows you to inspect and debug your HTML, CSS, and JavaScript. These menu items allow you to open Web Inspector into various tasks.

#### Empty Caches

Delete all caches stored by the browser. This is useful when a server is causing content you are developing to be cached, preventing you from seeing changes locally.

#### Settings

At the bottom of the  menu, there are quick links to both [`Changing Developer settings in Safari on macOS`](developer-settings.md) as well as [`Changing Feature Flag settings in Safari on macOS`](feature-flag-settings.md) to go directly to those specific Settings panes.

## See Also

- [Web Inspector](web-inspector.md)
  Use Web Inspector to inspect and debug your HTML, CSS, and JavaScript.
- [Responsive Design Mode](responsive-design-mode.md)
  Use Responsive Design Mode to test your `media` queries and other dynamic styles to ensure your webpages look great on any screen.
- [WebDriver](webdriver.md)
  Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver, including Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/develop-menu)*