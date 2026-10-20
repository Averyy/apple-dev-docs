# Making default and ephemeral requests

**Framework**: watchOS apps  
**Role**: Article

Send requests from your app when it’s running in the foreground.

#### Overview

Use default and ephemeral requests when your app is running in the foreground. These requests only continue as long as your app runs in the foreground. Because watchOS apps typically only run for short periods of time, you need to monitor all URL requests, and cancel or replace them with background requests when your app transitions to the background.

##### Request time-sensitive information

To request time-sensitive information:

1. Access the shared, default URL session object using the [`URLSession`](../Foundation/urlsession.md) class’s [`shared`](../Foundation/urlsession/shared.md) property.
2. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](../Foundation/urlsession/datatask%28with,completionhandler%29-52wk8.md) method.
3. Start the task by calling its [`resume()`](../Foundation/urlsessiontask/resume%28%29.md) method.

The task returns the requested data (or any errors) to your completion handler.

You can further customize your request by providing [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) or [`NSURLRequest`](../Foundation/nsurlrequest.md) objects, or by requesting a different type of task (for example, a download or upload task). Whenever possible, use a single, shared session for all your requests. Creating and invalidating sessions adds unnecessary overhead.

##### Request sensitive or private information

Ephemeral sessions are similar to default URL sessions; however, ephemeral sessions don’t store caches, credential stores, or any session-related data to disk. Because an ephemeral session doesn’t save potentially sensitive data, it’s ideal for private browsing or other privacy-related tasks. For more information, see [`ephemeral`](../Foundation/urlsessionconfiguration/ephemeral.md).

To request sensitive or private information:

1. Access an ephemeral configuration using the [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) class’s [`ephemeral`](../Foundation/urlsessionconfiguration/ephemeral.md) property.
2. Create an ephemeral session by calling the [`URLSession`](../Foundation/urlsession.md) class’s [`init(configuration:)`](../Foundation/urlsession/init%28configuration%29.md) initializer, and passing the ephemeral configuration.
3. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](../Foundation/urlsession/datatask%28with,completionhandler%29-52wk8.md) method.
4. Start the task by calling its [`resume()`](../Foundation/urlsessiontask/resume%28%29.md) method.

The task returns the requested data (or any errors) to your completion handler.

##### Indicate when requests can be deferred

By default, URL session tasks fail immediately whenever connectivity is unavailable. The system returns an error, such as [`NSURLErrorNotConnectedToInternet`](../Foundation/nsurlerrornotconnectedtointernet-swift.var.md).

Setting the [`waitsForConnectivity`](../Foundation/urlsessionconfiguration/waitsforconnectivity.md) property to [`true`](../Swift/true.md) tells the system to wait for connectivity before starting the task. This prevents the requests from failing if the watch can’t currently connect to the network. You can use the [`urlSession(_:taskIsWaitingForConnectivity:)`](../Foundation/urlsessiontaskdelegate/urlsession%28_,taskiswaitingforconnectivity%29.md) delegate method to learn when a request is deferred.

To create a deferrable request:

1. Access a default configuration using the [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) class’s [`default`](../Foundation/urlsessionconfiguration/default.md) property.
2. Set the configuration’s [`waitsForConnectivity`](../Foundation/urlsessionconfiguration/waitsforconnectivity.md) property to [`true`](../Swift/true.md).
3. Create a session by calling the [`URLSession`](../Foundation/urlsession.md) class’s [`init(configuration:)`](../Foundation/urlsession/init%28configuration%29.md) initializer, and passing the configuration.
4. Create a task to request the data by calling the session object’s [`dataTask(with:completionHandler:)`](../Foundation/urlsession/datatask%28with,completionhandler%29-52wk8.md) method.
5. Start the task by calling its [`resume()`](../Foundation/urlsessiontask/resume%28%29.md) method.

> ❗ **Important**: Background sessions ignore the [`waitsForConnectivity`](../Foundation/urlsessionconfiguration/waitsforconnectivity.md) property.

##### Clean up outstanding tasks

Keep track of the URL session tasks you create, and clean them up when your app goes to the background.

To clean up outstanding tasks:

1. In your extension delegate’s [`applicationWillResignActive()`](../WatchKit/wkextensiondelegate/applicationwillresignactive%28%29.md) method, cancel any outstanding tasks by calling the [`URLSessionTask`](../Foundation/urlsessiontask.md) object’s [`cancel()`](../Foundation/urlsessiontask/cancel%28%29.md) method.
2. (Optional) Use a background session to re-create and restart the task. This runs the task in the background, ensuring your app receives a response, even if the app is terminated.

## See Also

### Network requests
- [Making background requests](./making-background-requests.md)
  Send requests from your app when it’s running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/making-default-and-ephemeral-requests)*