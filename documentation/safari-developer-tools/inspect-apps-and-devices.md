# Inspect Apps and Devices

**Framework**: Safari Developer Features

Discover all inspectable web content in Safari and other apps on your Mac and on connected devices.

#### Overview

The  menu item from the  menu opens the  window which shows all inspectable web content in Safari, as well as web content used by other applications on your Mac, on running simulators, and on connected devices that are configured for inspection.

You can use this window to observe web content as it becomes available for inspection. This is also where you can configure automatic inspection for JSContexts.

![Apps and Devices Inspection window open, with a MacBook Pro device selected, showing Safari and Safari Technology Preview, each with an inspectable webpage, and a third-party macOS app with an inspectable JSContext.](https://docs-assets.developer.apple.com/published/4e57f4c8e09b30713c140cd57eefe2df/AppsAndDevicesInspection%402x.png)

#### Using the Apps and Devices Inspection Window

The  window sidebar shows your Mac, any connected and paired devices, such as iPhone, iPad or Apple Vision Pro, and any simulators that are currently running. Each inspectable device and simulator shows its name and OS version to make it easier to find the specific device you want to inspect.

Select a device to see inspectable web content available on that device grouped by the app it belongs to. This includes webpages, WKWebViews, JSContexts, service workers, Home Screen web apps, and Web Extension background pages. Click on a web content listing to launch [`Web Inspector`](web-inspector.md) for it.

The list of apps for a device updates automatically to show any app that is currently running inspectable web content (see [`Enabling inspecting content in your apps`](enabling-inspecting-content-in-your-apps.md)).

#### Automatic Inspection of Jscontexts

You can configure Web Inspector to automatically open for new JSContexts created in your app. Identify your app in the list of apps currently running inspectable web content and click the three-dots menu to reveal the automatic inspection settings:

If the `JSContext` you want to inspect automatically is already running, you will need to relaunch your app for automatic inspection settings to trigger the desired action.

#### Automatic Inspection of Service Workers

Service workers can be short-lived or perform their actions before you can get to manually inspect them via the Develop menu, for example, when handling a push message for a Home Screen web app.

You can configure Web Inspector to automatically open when a service worker is launched by Safari, a Home Screen web app, or any another app that runs service workers. Identify the app in the list of apps currently running inspectable web content and click the three-dots menu to reveal the automatic inspection settings:

If the service worker you want to inspect automatically is already running, you will need to cause it to relaunch for automatic inspection settings to trigger the desired action, for example, by closing and reopening the Safari tab that instantiates it.

## See Also

- [Develop menu](develop-menu.md)
  Access tools for debugging webpages in Safari, as well as tools for debugging web content in other apps and on other devices.
- [Web Inspector](web-inspector.md)
  Use Web Inspector to inspect and debug your HTML, CSS, and JavaScript.
- [Responsive Design Mode](responsive-design-mode.md)
  Use Responsive Design Mode to test your `media` queries and other dynamic styles to ensure your webpages look great on any screen.
- [WebDriver](webdriver.md)
  Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver, including Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/inspect-apps-and-devices)*