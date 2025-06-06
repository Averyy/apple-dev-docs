# Inspecting Safari on macOS

**Framework**: Safari Developer Features

Inspect webpages, Service Workers, and extensions in Safari on macOS.

#### Overview

Safari supports inspecting all webpages, Service Workers, and extensions. The way in which you inspect content depends on the type of content.

#### Inspecting a Webpage

In Safari, there are two ways to begin inspecting a webpage.

The first is via the [`Develop menu`](develop-menu.md). With the webpage you wish to inspect frontmost in Safari, go to the  menu and choose  (⌥⌘I). [`Web Inspector`](web-inspector.md) will then appear, and will be inspecting the webpage.

The second was to show Web Inspector is to right click on the webpage and choose  from the context menu. Web Inspector will then appear, and will have automatically highlighted the element you clicked on on the webpage.

Once opened, Web Inspector will continue to inspect the tab for which it was opened, even as you navigate to other pages in that tab.

#### Inspecting a Service Worker

[`Service Workers`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) are shared between webpages and don’t necessarily belong to any individual webpage. For this reason, they are inspectable separately from webpages in Safari.

When a service worker is running, you can inspect it by going to the  menu, selecting , and then choosing the service worker you wish to inspect.

#### Inspecting Extensions

Extensions can run script or create webpages in several places, and how you inspect them varies depending on what the content is. [`Learn more about debugging web extensions…`](https://developer.apple.comhttps://developer.apple.com/documentation/safariservices/safari_web_extensions/troubleshooting_your_safari_web_extension#3734523)

##### Content Scripts

To debug the scripts that web extensions have injected into webpages, first [`inspect the webpage`](https://developer.apple.com#Inspectingawebpage). Once Web Inspector is opened, click the Sources tab, and select your content script file from the Extension Scripts folder at the lower left. Then select your extension’s execution context by using the selector in the lower-right corner of the inspector. Set breakpoints by clicking the gutter with line numbers in the source view. Inspect other source files for your extension, such as style sheets, in the Sources area at the lower left.

##### Background Scripts

To debug background scripts, open the  menu and go to the  submenu. From there, select background script for the extension you wish to inspect.

##### Toolbar Pop Up

To debug your extension’s pop-up, click the button for your extension in the Safari toolbar to display the pop-up. Control-click the pop-up and select  to open Web Inspector for the pop-up.

## See Also

- [Inspecting iOS and iPadOS](inspecting-ios.md)
  Inspect webpages, Service Workers, Home Screen web apps, extensions, and content inside apps on iOS and iPadOS devices and simulators from a connected Mac.
- [Inspecting visionOS](inspecting-visionos.md)
  Inspect webpages, service workers, extensions, and content inside apps in visionOS from a Mac on the same network.
- [Inspecting tvOS](inspecting-tvos.md)
  Inspect JavaScript and TVML content on tvOS from a Mac on the same network.
- [Enabling inspecting content in your apps](enabling-inspecting-content-in-your-apps.md)
  Enable the inspection of webpages and JavaScript in apps you develop when inspected from a connected Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/inspecting-safari-macos)*