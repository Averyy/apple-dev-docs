# getPendingNotificationRequests(completionHandler:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

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
func getPendingNotificationRequests(completionHandler: @escaping @Sendable ([UNNotificationRequest]) -> Void)
```

```swift
func pendingNotificationRequests() async -> [UNNotificationRequest]
```

```objc
- (void) getPendingNotificationRequestsWithCompletionHandler:(void (^)(NSArray<UNNotificationRequest *> *requests)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func pendingNotificationRequests() async -> [UNNotificationRequest]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Here’s an example that obtains the pending notification requests.

```swift
let center = UNUserNotificationCenter.current()
let requests = await center.pendingNotificationRequests()
```

## Parameters

- `completionHandler`: A block for processing notification requests. This block may be executed on a background thread. The block has no return value and takes a single parameter.

  - **requests**: An array of [`UNNotificationRequest`](../unnotificationrequest.md) objects representing the scheduled notification requests. If there are no scheduled requests, this array is empty.

## See Also

### Scheduling notifications
- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](./add%28_,withcompletionhandler%29.md)
  Schedules the delivery of a local notification.
- [func removePendingNotificationRequests(withIdentifiers: [String])](./removependingnotificationrequests%28withidentifiers%29.md)
  Removes your app’s local notifications that are pending and match the specified identifiers.
- [func removeAllPendingNotificationRequests()](./removeallpendingnotificationrequests%28%29.md)
  Removes all of your app’s pending local notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getpendingnotificationrequests(completionhandler:))*