# Making default and ephemeral requests

**Framework**: watchOS apps

Send requests from your app when it’s running in the foreground.

#### Overview

Use default and ephemeral requests when your app is running in the foreground. These requests only continue as long as your app runs in the foreground. Because watchOS apps typically only run for short periods of time, you need to monitor all URL requests, and cancel or replace them with background requests when your app transitions to the background.

##### Request Time Sensitive Information

To request time-sensitive information:

1. Access the shared, default URL session object using the [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) class’s [`shared`](https://developer.apple.com/documentation/foundation/urlsession/shared) property.
2. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:completionhandler:)-52wk8) method.
3. Start the task by calling its [`resume()`](https://developer.apple.com/documentation/foundation/urlsessiontask/resume()) method.

The task returns the requested data (or any errors) to your completion handler.

You can further customize your request by providing [`URLSessionConfiguration`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) or [`NSURLRequest`](https://developer.apple.com/documentation/foundation/nsurlrequest) objects, or by requesting a different type of task (for example, a download or upload task). Whenever possible, use a single, shared session for all your requests. Creating and invalidating sessions adds unnecessary overhead.

##### Request Sensitive or Private Information

Ephemeral sessions are similar to default URL sessions; however, ephemeral sessions don’t store caches, credential stores, or any session-related data to disk. Because an ephemeral session doesn’t save potentially sensitive data, it’s ideal for private browsing or other privacy-related tasks. For more information, see [`ephemeral`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/ephemeral).

To request sensitive or private information:

1. Access an ephemeral configuration using the [`URLSessionConfiguration`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) class’s [`ephemeral`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/ephemeral) property.
2. Create an ephemeral session by calling the [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) class’s [`init(configuration:)`](https://developer.apple.com/documentation/foundation/urlsession/init(configuration:)) initializer, and passing the ephemeral configuration.
3. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:completionhandler:)-52wk8) method.
4. Start the task by calling its [`resume()`](https://developer.apple.com/documentation/foundation/urlsessiontask/resume()) method.

The task returns the requested data (or any errors) to your completion handler.

##### Indicate When Requests Can Be Deferred

By default, URL session tasks fail immediately whenever connectivity is unavailable. The system returns an error, such as [`NSURLErrorNotConnectedToInternet`](https://developer.apple.com/documentation/foundation/nsurlerrornotconnectedtointernet-swift.var).

Setting the [`waitsForConnectivity`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/waitsforconnectivity) property to [`true`](https://developer.apple.com/documentation/swift/true) tells the system to wait for connectivity before starting the task. This prevents the requests from failing if the watch can’t currently connect to the network. You can use the [`urlSession(_:taskIsWaitingForConnectivity:)`](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:taskiswaitingforconnectivity:)) delegate method to learn when a request is deferred.

To create a deferrable request:

1. Access a default configuration using the [`URLSessionConfiguration`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) class’s [`default`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/default) property.
2. Set the configuration’s [`waitsForConnectivity`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/waitsforconnectivity) property to [`true`](https://developer.apple.com/documentation/swift/true).
3. Create a session by calling the [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) class’s [`init(configuration:)`](https://developer.apple.com/documentation/foundation/urlsession/init(configuration:)) initializer, and passing the configuration.
4. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:completionhandler:)-52wk8) method.
5. Start the task by calling its [`resume()`](https://developer.apple.com/documentation/foundation/urlsessiontask/resume()) method.

> ❗ **Important**: Background sessions ignore the [`waitsForConnectivity`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/waitsforconnectivity) property.

##### Clean Up Outstanding Tasks

Keep track of the URL session tasks you create, and clean them up when your app goes to the background.

To clean up outstanding tasks:

1. In your extension delegate’s [`applicationWillResignActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()) method, cancel any outstanding tasks by calling the [`URLSessionTask`](https://developer.apple.com/documentation/foundation/urlsessiontask) object’s [`cancel()`](https://developer.apple.com/documentation/foundation/urlsessiontask/cancel()) method.
2. (Optional) Use a background session to re-create and restart the task. This runs the task in the background, ensuring your app receives a response, even if the app is terminated.

## See Also

- [Making background requests](making-background-requests.md)
  Send requests from your app when it’s running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/making-default-and-ephemeral-requests)*