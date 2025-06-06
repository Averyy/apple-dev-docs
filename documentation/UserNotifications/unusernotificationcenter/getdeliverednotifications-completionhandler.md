# getDeliveredNotifications(completionHandler:)

**Framework**: Usernotifications  
**Kind**: method

Fetches all of your app’s delivered notifications that are still present in Notification Center.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func deliveredNotifications() async -> [UNNotification]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func deliveredNotifications() async -> [UNNotification]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func deliveredNotifications() async -> [UNNotification]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method executes asynchronously, returning immediately and executing the provided block on a background thread when the results become available.

## Parameters

- `completionHandler`: The block to execute with the results. This block may be executed on a background thread. The block has no return value and takes the following parameter:

## See Also

- [func removeDeliveredNotifications(withIdentifiers: [String])](unusernotificationcenter/removedeliverednotifications(withidentifiers:).md)
  Removes your app’s notifications from Notification Center that match the specified identifiers.
- [func removeAllDeliveredNotifications()](unusernotificationcenter/removealldeliverednotifications.md)
  Removes all of your app’s delivered notifications from Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getdeliverednotifications(completionhandler:))*