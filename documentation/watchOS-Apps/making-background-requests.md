# Making background requests

**Framework**: Watchos Apps

Send requests from your app when it’s running in the background.

#### Overview

Use background requests when your app is running in the background or about to become inactive.

To create a background session:

1. Create a background configuration by calling the [`backgroundSessionConfiguration(_:)`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411521-backgroundsessionconfiguration) method on the [`URLSessionConfiguration`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration) class.
2. Create a background session by calling the [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) class’s [`init(configuration:delegate:delegateQueue:)`](https://developer.apple.com/documentation/foundation/urlsession/1411597-init) initializer, passing both the background configuration and a session delegate. Background sessions must have a session delegate.
3. Create a task to download data by calling the session object’s [`downloadTask(with:)`](https://developer.apple.com/documentation/foundation/urlsession/1411482-downloadtask) method.
4. Start the task by calling its [`resume()`](https://developer.apple.com/documentation/foundation/urlsessiontask/1411121-resume) method.
5. Implement your WatchKit extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method to respond to (and complete) the WatchKit background task. For more information, see [`WKURLSessionRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKURLSessionRefreshBackgroundTask).
6. Implement the session delegate’s methods to receive data and notifications from the session. For more information, see [`URLSessionDelegate`](https://developer.apple.com/documentation/Foundation/URLSessionDelegate).

Unlike default and ephemeral sessions, a background session persists even if your watchOS app closes. If your app is still the frontmost app, the system wakes your app as soon as it receives a response. Otherwise, the system may defer delivering the response to your app, based on system resources. If the response hasn’t been delivered yet, it’s delivered the next time your app becomes active.

Background sessions may be deferred based on the system’s state, network connectivity, and other issues. When making a background request, smaller transfers are better.

For more information on working with WatchKit background tasks, see [`Background execution`](https://developer.apple.com/documentation/WatchKit/background-execution).

## See Also

- [Making default and ephemeral requests](making-default-and-ephemeral-requests.md)
  Send requests from your app when it’s running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/making-background-requests)*