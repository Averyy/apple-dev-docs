# didReceive(_:completionHandler:)

**Framework**: User Notifications UI  
**Kind**: method

Handles a notification action selected by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func didReceive(_ response: UNNotificationResponse) async -> UNNotificationContentExtensionResponseOption
```

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func didReceive(_ response: UNNotificationResponse) async -> UNNotificationContentExtensionResponseOption
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func didReceive(_ response: UNNotificationResponse) async -> UNNotificationContentExtensionResponseOption
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Implement this method when you want your view controller to handle actions selected by the user. Use your implementation to perform the associated task and then execute the `completion` block. If you implement this method, you must handle all actions defined in all categories managed by your Notification Content app extension. If you don’t implement this method, the system notifies your app when the user selects an action.

## Parameters

- `response`: The response object that identifies the user-selected action.   Use this object to get information about the notification and the user’s   response.
- `completion`: The block to execute when you are finished performing the   action. You must call this block at some point during your implementation.   The block has no return value and takes the following parameter:

## See Also

- [enum UNNotificationContentExtensionResponseOption](unnotificationcontentextensionresponseoption.md)
  Constants indicating the preferred response to a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/didreceive(_:completionhandler:))*