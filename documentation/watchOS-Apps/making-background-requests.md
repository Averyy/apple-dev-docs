# Making background requests

**Framework**: watchOS apps  
**Role**: Article

Send requests from your app when it’s running in the background.

## Overview

Use background requests when your app is running in the background or about to become inactive.

To create a background session:

1. Create a background configuration by calling the [`backgroundSessionConfiguration(_:)`](../Foundation/urlsessionconfiguration/backgroundsessionconfiguration%28_%29.md) method on the [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) class.
2. Create a background session by calling the [`URLSession`](../Foundation/urlsession.md) class’s [`init(configuration:delegate:delegateQueue:)`](../Foundation/urlsession/init%28configuration,delegate,delegatequeue%29.md) initializer, passing both the background configuration and a session delegate. Background sessions must have a session delegate.
3. Create a task to download data by calling the session object’s [`downloadTask(with:)`](../Foundation/urlsession/downloadtask%28with%29-1onj.md) method.
4. Start the task by calling its [`resume()`](../Foundation/urlsessiontask/resume%28%29.md) method.
5. Implement your WatchKit extension delegate’s [`handle(_:)`](../WatchKit/wkextensiondelegate/handle%28_%29-92ulv.md) method to respond to (and complete) the WatchKit background task. For more information, see [`WKURLSessionRefreshBackgroundTask`](../WatchKit/wkurlsessionrefreshbackgroundtask.md).
6. Implement the session delegate’s methods to receive data and notifications from the session. For more information, see [`URLSessionDelegate`](../Foundation/urlsessiondelegate.md).

Unlike default and ephemeral sessions, a background session persists even if your watchOS app closes. If your app is still the frontmost app, the system wakes your app as soon as it receives a response. Otherwise, the system may defer delivering the response to your app, based on system resources. If the response hasn’t been delivered yet, it’s delivered the next time your app becomes active.

Background sessions may be deferred based on the system’s state, network connectivity, and other issues. When making a background request, smaller transfers are better.

For more information on working with WatchKit background tasks, see [Background execution](../WatchKit/background-execution.md).

## See Also

### Network requests
- [Making default and ephemeral requests](./making-default-and-ephemeral-requests.md)
  Send requests from your app when it’s running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/making-background-requests)*