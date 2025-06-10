# Keeping your watchOS content up to date

**Framework**: watchOS apps

Ensure that your app’s content is relevant and up to date.

#### Overview

A watchOS app rarely runs in isolation; it needs data from the outside world. You can access data directly from a web service, CloudKit, or other online resources. You can also share data from a paired iPhone, although this can’t be your app’s primary way of accessing data.

Because Apple Watch has several ways to connect to the internet, it’s important to test all of your app’s networking code over all possible routes.

##### Access Data Directly

Your watchOS app can connect directly to web services and other online sources. When making these requests, the system can send data through a paired iPhone as a proxy, over a known Wi-Fi network, or over the watch’s own cellular connection (see Test Your Update Code with Different Configurations below).

Always use a [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) object to make network requests; however, the type of session varies depending on your app’s needs:

- If your app is running in the foreground, use a default or ephemeral session to avoid any delays to your request.
- If your app is running in the background (or about to become inactive), use a background session to ensure the request completes.

Default and ephemeral sessions minimize any possible delays between making the request and receiving the response. These sessions are ideal for small exchanges of data when the user actively interacts with the app. You can also use them to update your app’s content whenever the app becomes active. For more information, see [`Making default and ephemeral requests`](making-default-and-ephemeral-requests.md).

Background sessions, on the other hand, guarantee that your app eventually receives a response, even if your app becomes inactive or terminates. However, the system may delay or defer background sessions based on available resources. For more information, see [`Making background requests`](making-background-requests.md).

To learn more about using URL sessions, see [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system).

##### Use Cloudkit to Store Data in the Cloud

CloudKit lets you save data in an iCloud container, sharing that data across all the user’s iCloud-connected devices. For example, you could use CloudKit to share your app’s settings or sync the user’s current location in a long-form audio file. CloudKit also lets you create cloud-based apps without having to set up and manage your own servers.

CloudKit offers the following advantages:

- Users can access CloudKit data based on their Apple ID without requiring in-app sign-in.
- CloudKit is ubiquitous; it’s available as a native framework on all of Apple’s platforms. Additionally, the web frameworks give users access to CloudKit on the web or on platforms that don’t have a native framework.
- CloudKit requests use [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession). This means watchOS automatically selects the best route when making the request (proxied through a paired iPhone, over Wi-Fi, or over a cellular connection).

CloudKit includes support for [`CKSubscription`](https://developer.apple.com/documentation/CloudKit/CKSubscription) and notifications in watchOS 6 and later, letting your watchOS app respond to changes from other devices. This makes CloudKit a potential replacement for Watch Connectivity for independent apps. For more information, see [`CloudKit`](https://developer.apple.com/documentation/CloudKit).

##### Share Data with the Paired Iphone

While your watchOS app can schedule periodic background tasks to update its information, these tasks are strictly limited — both in the number of times your app can wake per day, and in the amount of time it can run when it wakes. Additionally, your app isn’t guaranteed to receive background execution time. The system gives priority to apps with a complication in the active watch face and apps in the dock.

![A figure showing a watch face with several active complications.](https://docs-assets.developer.apple.com/published/68e164e2c82901f6cd8f0991f28b842f/keeping-your-watchos-app-s-content-up-to-date-1%402x.png)

![A figure showing a watch face with apps in the dock.](https://docs-assets.developer.apple.com/published/390dd10a4f948500ab0b2152f08e90d5/keeping-your-watchos-app-s-content-up-to-date-2%402x.png)

If your watchOS app has a companion iOS app installed, you can take advantage of it to update your watchOS app from its companion. For example, if the user’s iPhone and Apple Watch can communicate with each other, use the [`Watch Connectivity`](https://developer.apple.com/documentation/WatchConnectivity) framework to opportunistically send updates from iOS to watchOS.

However, WatchConnectivity isn’t always available. In watchOS 6 and later, users may not install the iOS companion for their independent watchOS apps. Also, with the release of the Apple Watch Series 3 (GPS + Cellular), even dependent apps are likely to be away from the paired iPhone for extended periods. It’s vital that your app continue to provide useful information even when it can’t connect with its companion, so you can’t rely on WatchConnectivity as your only means of updating the watchOS app. Instead, use the WatchConnectivity framework as an opportunistic optimization, rather than the primary means of supplying fresh data.

For more information on using background refresh tasks, see [`WKApplicationRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKApplicationRefreshBackgroundTask). For more on the WatchConnectivity framework, see [`WCSession`](https://developer.apple.com/documentation/WatchConnectivity/WCSession).

##### Test Your Update Code with Different Configurations

When your watchOS app connects to CloudKit or interacts with online resources using a URL session request, the system can route the request in one of three ways. While developing your app, make sure to test your network requests over all three routes. The system can route the request by:

- Proxy through iPhone
- Connecting to a known network
- Connecting using cellular data

First, the watch attempts to proxy the request through a paired iPhone. The watch communicates with the phone over Bluetooth, sharing the phone’s connection to the internet. When connected to a paired iPhone, the control center shows a green iPhone icon in the upper-left corner.

![Screenshot showing the Apple Watch control center when the watch is connected to a paired iPhone.](https://docs-assets.developer.apple.com/published/22f60abdfafa52920494f3cbda866f03/keeping-your-watchos-app-s-content-up-to-date-3%402x.png)

If the watch can’t connect to a paired iPhone but can connect to a known Wi-Fi network (a network that the user has previously logged into with their phone), then it sends the request using the Wi-Fi network. When connected to a known network, the control center shows the Wi-Fi network in the upper-left corner.

![Screenshot showing the Apple Watch control center when the watch is connected to a known Wi-Fi network. ](https://docs-assets.developer.apple.com/published/f5eca770b00dc58313ed06a6dee429b3/keeping-your-watchos-app-s-content-up-to-date-4%402x.png)

Finally, if the watch can’t connect to either a paired iPhone or a known Wi-Fi network, it sends the request using its cellular connection. This route is only available on Apple Watch Series 3 (GPS + Cellular). When using a cellular connection, the control center shows the cell connection’s signal strength as green dots in the upper-left corner.

![Screenshot showing the Apple Watch control center when the watch is using a cellular connection. ](https://docs-assets.developer.apple.com/published/139aad009b4fec2d49e69c5c0b7002f3/keeping-your-watchos-app-s-content-up-to-date-5%402x.png)

## See Also

- [Making default and ephemeral requests](making-default-and-ephemeral-requests.md)
  Send requests from your app when it’s running in the foreground.
- [Making background requests](making-background-requests.md)
  Send requests from your app when it’s running in the background.
- [URL Loading System](../Foundation/url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [class URLSession](../Foundation/URLSession.md)
  An object that coordinates a group of related, network data transfer tasks.
- [class URLSessionConfiguration](../Foundation/URLSessionConfiguration.md)
  A configuration object that defines behavior and policies for a URL session.
- [class URLSessionTask](../Foundation/URLSessionTask.md)
  A task, like downloading a specific resource, performed in a URL session.
- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Updating watchOS apps with timelines](updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [Authenticating users on Apple Watch](authenticating-users-on-apple-watch.md)
  Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/ActionButtonArticle.md)
  Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](enabling-double-tap.md)
  Customize your app’s response to the double-tap gesture on Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/keeping-your-watchos-app-s-content-up-to-date)*