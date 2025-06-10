# getPendingNotificationRequests(completionHandler:)

**Framework**: User Notifications  
**Kind**: method

Fetches all of your app’s local notifications that are pending delivery.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func pendingNotificationRequests() async -> [UNNotificationRequest]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func pendingNotificationRequests() async -> [UNNotificationRequest]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Here’s an example that obtains the pending notification requests.

```swift
let center = UNUserNotificationCenter.current()
let requests = await center.pendingNotificationRequests()
```

## Parameters

- `completionHandler`: A block for processing notification requests. This block may be executed on a background thread. The block has no return value and takes a single parameter.

## See Also

- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/add(_:withcompletionhandler:).md)
  Schedules the delivery of a local notification.
- [func removePendingNotificationRequests(withIdentifiers: [String])](unusernotificationcenter/removependingnotificationrequests(withidentifiers:).md)
  Removes your app’s local notifications that are pending and match the specified identifiers.
- [func removeAllPendingNotificationRequests()](unusernotificationcenter/removeallpendingnotificationrequests.md)
  Removes all of your app’s pending local notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getpendingnotificationrequests(completionhandler:))*