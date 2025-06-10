# Inspecting iOS and iPadOS

**Framework**: Safari Developer Features

Inspect webpages, Service Workers, Home Screen web apps, extensions, and content inside apps on iOS and iPadOS devices and simulators from a connected Mac.

#### Overview

Web content on iOS and iPadOS is inspectable when you connect the device to your Mac. You can also use simulators on macOS to test your webpages and apps without a physical device. To learn more about device simulators, see [`Installing Xcode and Simulators`](installing-xcode-and-simulators.md).

#### Enabling Inspecting Your Device From a Connected Mac

Before you can connect your device to a Mac to inspect it, you must allow the device to be inspected.

1. Open the  app.
2. Go to  > .
3. Scroll down to .
4. Enable the  toggle.

Now, connect the device to your Mac using a cable. In Safari, the device will appear in the [`Develop menu`](develop-menu.md).

> ❗ **Important**: You may need to trust the Mac you connect your device to when the device prompts you before it appears in the  menu on your Mac.

##### Connecting Over the Network

In addition to being able to inspect devices over a wired connection, you can also connect to your device over Wi-Fi or another network connection. To enable connecting over the network, you must first have enabled  on your device and connected it to your Mac using a cable. Then, you can enable  from the device’s submenu in the  menu. Alternatively, you can also [`connect to the device using Xcode`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devbc48d1bad).

##### Ios and Ipados Simulators

 is always enabled for simulators, and currently booted simulators will appear in the  menu just like connected devices.

#### Inspecting a Webpage

Webpages you open in Safari in iOS and iPadOS appear in a submenu for the connected device of the  menu of Safari on a connected Mac. Safari groups webpages and other content by app, making it easier to find the webpage you want to inspect.

Find the webpage you want to inspect, then select it to open a new Web Inspector window. This window continues inspecting the tab you started inspecting, including across navigations. If you close the tab in iOS or iPadOS, the Web Inspector window disappears.

For webpages, some additional options are available only while inspecting a connected device or a simulator to allow you to override the user agent, disable cross-origin restrictions, disable site-specific quirks, and more. See [`Device Settings`](https://developer.apple.comhttps://webkit.org/web-inspector/device-settings/).

#### Inspecting a Service Worker

[`Service Workers`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) are shared between webpages and don’t necessarily belong to any individual webpage. For this reason, they are inspectable separately from webpages in Safari.

You can only inspect service workers that are currently running. To inspect service workers, open the  menu, find the menu item for the visionOS device you want to inspect, and select them from the  section near the bottom of the menu. This section doesn’t appear if there aren’t any service workers currently running.

#### Inspecting Home Screen Web Apps

When a [`Home Screen web app`](https://developer.apple.comhttps://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios) is in the foreground, you can inspect it from the  menu. Find the menu item for the iOS or iPadOS device you wish to inspect, and then find the web app’s URL in the  section near the bottom of the menu.

#### Inspecting Extensions

Extensions can run scripts or create webpages in several places, and how you inspect them varies depending on the content. [`Learn more about debugging web extensions…`](https://developer.apple.comhttps://developer.apple.com/documentation/safariservices/safari_web_extensions/troubleshooting_your_safari_web_extension#3734523)

##### Content Scripts

To debug the scripts that web extensions inject into webpages, first [`inspect the webpage`](https://developer.apple.com#Inspecting-a-webpage). Open Web Inspector, then click the Sources tab and select your content script file from the Extension Scripts folder at the lower left. Select your extension’s execution context using the selector in the lower-right corner of the inspector. Set breakpoints by clicking the gutter with line numbers in the source view. Inspect other source files for your extension, such as style sheets, in the Sources area at the lower left.

##### Background Scripts

To debug background scripts, open the  menu, find the menu item for the iOS or iPadOS device you wish to inspect, and then find the item with the name of the extension, “”, and the file name of the background script.

##### Toolbar Pop Up

To debug your extension’s pop-up, open your pop-up on the device. Now from the  menu find the menu item for the iOS or iPadOS device you wish to inspect, and then find the item with the name of the extension, “”, and the file name of the pop-up’s HTML.

#### Inspecting Javascript and Webpages in Apps

You can make [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView)s and [`JSContext`](https://developer.apple.com/documentation/JavaScriptCore/JSContext)s in apps inspectable, allowing anyone who enables  on the device to inspect them. Content you can inspect appears in a submenu for the connected device of the  menu of Safari on a connected Mac. Safari separates webpages and JavaScript contexts by app, making finding the content you want to inspect easier.

Learn more about [`Enabling inspecting content in your apps`](enabling-inspecting-content-in-your-apps.md).

## See Also

- [Inspecting Safari on macOS](inspecting-safari-macos.md)
  Inspect webpages, Service Workers, and extensions in Safari on macOS.
- [Inspecting visionOS](inspecting-visionos.md)
  Inspect webpages, service workers, extensions, and content inside apps in visionOS from a Mac on the same network.
- [Inspecting tvOS](inspecting-tvos.md)
  Inspect JavaScript and TVML content on tvOS from a Mac on the same network.
- [Enabling inspecting content in your apps](enabling-inspecting-content-in-your-apps.md)
  Enable the inspection of webpages and JavaScript in apps you develop when inspected from a connected Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/inspecting-ios)*