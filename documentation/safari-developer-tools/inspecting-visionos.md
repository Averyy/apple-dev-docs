# Inspecting visionOS

**Framework**: Safari Developer Features

Inspect webpages, service workers, extensions, and content inside apps in visionOS from a Mac on the same network.

#### Overview

Web content in visionOS is inspectable when you connect the device to a Mac. You can also use simulators on a Mac with Apple silicon to test your webpages and apps without a physical device. To learn more about device simulators, see [`Installing Xcode and Simulators`](installing-xcode-and-simulators.md).

#### Enable Inspecting Your Device From a Mac on the Same Network

To inspect web content on a visionOS device, you must enable Web Inspector.

1. On your visionOS device, open the  app.
2. Go to  > .
3. Scroll down to .
4. Enable the  toggle.

To allow inspecting without a physical wired connection to your Mac, you can pair your visionOS device over the network:

1. Make sure both your Mac and device are connected to the same network. The Wi-Fi network must be compatible with Bonjour.
2. On your visionOS device, open , then choose  > . While this screen is visible, your device is available for pairing from any Mac on the network.
3. On your Mac, go to the  menu in Safari and find your device in the list.
4. From the device’s submenu, choose .
5. Enter the six-digit PIN code shown on the device into the PIN field shown on your Mac.

Once paired, you can inspect content on the visionOS device like any other device. In Safari, the device appears in the [`Develop menu`](develop-menu.md).

Alternatively, you can also [`pair with the device using Xcode`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devbc48d1bad).

##### Visionos Simulators

Simulators come with  already enabled. The Develop menu lists currently booted simulators just like connected devices.

#### Inspect Webpages

Webpages you open in Safari in visionOS appear in a submenu for the connected device of the  menu of Safari on a connected Mac. Safari groups webpages and other content by app, making finding the webpage you want to inspect easier.

Find the webpage you want to inspect, then select it to open a new Web Inspector window. This window continues inspecting the tab you started inspecting, including across navigations. If you close the tab in visionOS, the Web Inspector window disappears.

For webpages, some additional options are available only while inspecting a connected device or a simulator to allow you to override the user agent, disable cross-origin restrictions, disable site-specific quirks, and more. See [`Device Settings`](https://developer.apple.comhttps://webkit.org/web-inspector/device-settings/).

#### Inspect Service Workers

[`Service workers`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) are shared between webpages and don’t necessarily belong to any individual webpage. For this reason, they are inspectable separately from webpages in Safari.

You can only inspect service workers that are currently running. To inspect service workers, open the  menu, find the menu item for the visionOS device you want to inspect and select them from the  section near the bottom of the menu. This section doesn’t appear if there aren’t any service workers currently running.

#### Inspect Extensions

Extensions can run scripts or create webpages in several places, and how you inspect them varies depending on the content. [`Learn more about debugging web extensions…`](https://developer.apple.comhttps://developer.apple.com/documentation/safariservices/safari_web_extensions/troubleshooting_your_safari_web_extension#3734523)

##### Content Scripts

To debug the scripts that web extensions inject into webpages, first [`inspect the webpage`](https://developer.apple.com#Inspect-webpages). Open Web Inspector, then click the Sources tab and select your content script file from the Extension Scripts folder at the lower left. Select your extension’s execution context using the selector in the lower-right corner of the inspector. Set breakpoints by clicking the gutter with line numbers in the source view. Inspect other source files for your extension, such as style sheets, in the Sources area at the lower left.

##### Background Scripts

To debug background scripts, open the  menu, find the menu item for the device you want to inspect, and then find the item with the name of the extension, “”, and the filename of the background script.

##### Toolbar Pop Up

To debug your extension’s pop-up, open your pop-up on the device. From the  menu, find the menu item for the device you want to inspect, and then find the item with the name of the extension, “”, and the filename of the pop-up’s HTML.

#### Inspect Javascript and Webpages in Apps

You can make [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView)s and [`JSContext`](https://developer.apple.com/documentation/JavaScriptCore/JSContext)s in apps inspectable, allowing anyone who enables  on the device to inspect them. Content you can inspect appears in a submenu for the connected device of the  menu of Safari on a connected Mac. Safari separates webpages and JavaScript contexts by app, making finding the content you want to inspect easier.

Learn more about [`Enabling inspecting content in your apps`](enabling-inspecting-content-in-your-apps.md).

## See Also

- [Inspecting Safari on macOS](inspecting-safari-macos.md)
  Inspect webpages, service workers, and extensions in Safari on macOS.
- [Inspecting iOS and iPadOS](inspecting-ios.md)
  Inspect webpages, service workers, Home Screen web apps, extensions, and content inside apps on iOS and iPadOS devices and simulators from a connected Mac.
- [Inspecting tvOS](inspecting-tvos.md)
  Inspect JavaScript and TVML content on tvOS from a Mac on the same network.
- [Enabling inspecting content in your apps](enabling-inspecting-content-in-your-apps.md)
  Enable the inspection of webpages and JavaScript in apps you develop when inspected from a connected Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/inspecting-visionos)*