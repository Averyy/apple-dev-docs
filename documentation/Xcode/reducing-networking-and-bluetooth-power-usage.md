# Reducing networking and Bluetooth power usage

**Framework**: Xcode  
**Role**: Article

Schedule requests strategically and minimize background network activity to decrease your app’s energy use.

## Overview

Decrease the power your app consumes in communication-related tasks by choosing the correct networking technology, batching connections, and waiting for appropriate networking conditions before making requests.

### Choose an appropriate networking framework

Your choice of networking framework directly impacts your app’s energy consumption. Use [`URLSession`](../Foundation/urlsession.md) to send HTTP requests, because it includes built-in power optimizations like connection pooling and intelligent scheduling. For lower-level networking access, use the [Network](../Network/Network.md) framework, which provides energy-efficient protocols and gives you control over connection timing.

Both `URLSession` and the Network framework take advantage of system-level power optimizations.

### Schedule requests efficiently

Minimize energy consumption by being strategic about when and how your app accesses the network. Use a single [`URLSession`](../Foundation/urlsession.md) instance (rather than multiple instances) so you can re-use connections wherever possible.

Batch multiple requests together and compress payloads to reduce the total time network interfaces remain active.

Manage expensive network requests through [`URLSession`](../Foundation/urlsession.md), and set properties on [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) to handle different network conditions. Set [`waitsForConnectivity`](../Foundation/urlsessionconfiguration/waitsforconnectivity.md) to `true` to avoid wasteful connection attempts when the network is unavailable.

To prevent network tasks from using an expensive network, set [`allowsExpensiveNetworkAccess`](../Foundation/urlsessionconfiguration/allowsexpensivenetworkaccess.md) to `false`. Postpone nonessential tasks until a nonexpensive network, such as Wi-Fi, becomes available. Limit your app’s use of constrained network access by setting [`allowsConstrainedNetworkAccess`](../Foundation/urlsessionconfiguration/allowsconstrainednetworkaccess.md) to `false` for discretionary requests, and defer these tasks until a nonconstrained interface becomes available.

### Schedule network requests in the background

Use [`background(withIdentifier:)`](../Foundation/urlsessionconfiguration/background%28withidentifier%29.md) to configure a [`URLSessionDownloadTask`](../Foundation/urlsessiondownloadtask.md) to run in the background. The system schedules background download tasks when energy conditions are optional. Set [`isDiscretionary`](../Foundation/urlsessionconfiguration/isdiscretionary.md) to `true` to tell the system to use intelligent scheduling, which defers the download until the device is charging or connected to Wi-Fi.

The system automatically coalesces background downloads from multiple apps, keeping the networking hardware active for shorter periods and reducing the energy overhead associated with each app.

For more information, see [Downloading files in the background](../Foundation/downloading-files-in-the-background.md).

### Refresh app state in the background

Use [`BGAppRefreshTask`](../BackgroundTasks/bgapprefreshtask.md) strategically to keep your app’s state updated, while minimizing unnecessary network activity. Schedule background refresh tasks only when essential data updates are needed, and always check network conditions before initiating requests.

Set an appropriate value for your request’s [`earliestBeginDate`](../BackgroundTasks/bgtaskrequest/earliestbegindate.md) to avoid frequent wake-ups, using exponential backoff for failed attempts to prevent energy-draining retry loops. For example, if your first refresh task fails, set the `earliestBeginDate` on the first retry 5 minutes later. If that fails, wait 10 minutes before retrying, then 20 minutes, and so on.

Call [`setTaskCompleted(success:)`](../BackgroundTasks/bgtask/settaskcompleted%28success%29.md) promptly when your task succeeds or fails to allow the system to return to sleep. Gracefully handle situations where the system expires your task after a timeout in your implementation of [`expirationHandler`](../BackgroundTasks/bgtask/expirationhandler.md).

If your app uses too many resources in the background, the system might stop it, which increases your app’s energy use because the system needs to launch your app instead of bringing it to the foreground the next time someone tries to use it.

### Minimize your app’s Bluetooth use

Keep connections to Bluetooth accessories open only when your app is communicating with the accessory. Discover and configure accessories using [AccessorySetupKit](../AccessorySetupKit/AccessorySetupKit.md), which efficiently maintains the Bluetooth connection for you.

## See Also

### Networking and location
- [Accessing the device’s location efficiently](./accessing-the-device-s-location-efficiently.md)
  Use Core Location features to manage energy use, receive updates, and minimize location update frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-networking-and-bluetooth-power-usage)*