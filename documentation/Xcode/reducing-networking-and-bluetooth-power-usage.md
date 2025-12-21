# Reducing networking and Bluetooth power usage

**Framework**: Xcode

Schedule requests strategically and minimize background network activity to decrease your app’s energy use.

#### Overview

Decrease the power your app consumes in communication-related tasks by choosing the correct networking technology, batching connections, and waiting for appropriate networking conditions before making requests.

##### Choose an Appropriate Networking Framework

Your choice of networking framework directly impacts your app’s energy consumption. Use [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to send HTTP requests, because it includes built-in power optimizations like connection pooling and intelligent scheduling. For lower-level networking access, use the [`Network`](https://developer.apple.com/documentation/Network) framework, which provides energy-efficient protocols and gives you control over connection timing.

Both `URLSession` and the Network framework take advantage of system-level power optimizations.

##### Schedule Requests Efficiently

Minimize energy consumption by being strategic about when and how your app accesses the network. Use a single [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) instance (rather than multiple instances) so you can re-use connections wherever possible.

Batch multiple requests together and compress payloads to reduce the total time network interfaces remain active.

Manage expensive network requests through [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), and set properties on [`URLSessionConfiguration`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration) to handle different network conditions. Set [`waitsForConnectivity`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/waitsForConnectivity) to `true` to avoid wasteful connection attempts when the network is unavailable.

To prevent network tasks from using an expensive network, set [`allowsExpensiveNetworkAccess`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/allowsExpensiveNetworkAccess) to `false`. Postpone nonessential tasks until a nonexpensive network, such as Wi-Fi, becomes available. Limit your app’s use of constrained network access by setting [`allowsConstrainedNetworkAccess`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/allowsConstrainedNetworkAccess) to `false` for discretionary requests, and defer these tasks until a nonconstrained interface becomes available.

##### Schedule Network Requests in the Background

Use [`background(withIdentifier:)`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/background(withIdentifier:)) to configure a [`URLSessionDownloadTask`](https://developer.apple.com/documentation/Foundation/URLSessionDownloadTask) to run in the background. The system schedules background download tasks when energy conditions are optional. Set [`isDiscretionary`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/isDiscretionary) to `true` to tell the system to use intelligent scheduling, which defers the download until the device is charging or connected to Wi-Fi.

The system automatically coalesces background downloads from multiple apps, keeping the networking hardware active for shorter periods and reducing the energy overhead associated with each app.

For more information, see [`Downloading files in the background`](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background).

##### Refresh App State in the Background

Use [`BGAppRefreshTask`](https://developer.apple.com/documentation/BackgroundTasks/BGAppRefreshTask) strategically to keep your app’s state updated, while minimizing unnecessary network activity. Schedule background refresh tasks only when essential data updates are needed, and always check network conditions before initiating requests.

Set an appropriate value for your request’s [`earliestBeginDate`](https://developer.apple.com/documentation/BackgroundTasks/BGTaskRequest/earliestBeginDate) to avoid frequent wake-ups, using exponential backoff for failed attempts to prevent energy-draining retry loops. For example, if your first refresh task fails, set the `earliestBeginDate` on the first retry 5 minutes later. If that fails, wait 10 minutes before retrying, then 20 minutes, and so on.

Call [`setTaskCompleted(success:)`](https://developer.apple.com/documentation/BackgroundTasks/BGTask/setTaskCompleted(success:)) promptly when your task succeeds or fails to allow the system to return to sleep. Gracefully handle situations where the system expires your task after a timeout in your implementation of [`expirationHandler`](https://developer.apple.com/documentation/BackgroundTasks/BGTask/expirationHandler).

If your app uses too many resources in the background, the system might stop it, which increases your app’s energy use because the system needs to launch your app instead of bringing it to the foreground the next time someone tries to use it.

##### Minimize Your Apps Bluetooth Use

Keep connections to Bluetooth accessories open only when your app is communicating with the accessory. Discover and configure accessories using [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit), which efficiently maintains the Bluetooth connection for you.

## See Also

- [Accessing the device’s location efficiently](accessing-the-device-s-location-efficiently.md)
  Use Core Location features to manage energy use, receive updates, and minimize location update frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-networking-and-bluetooth-power-usage)*