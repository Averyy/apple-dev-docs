# getNotificationCategories(completionHandler:)

**Framework**: User Notifications  
**Kind**: method

Fetches your app’s registered notification categories.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func notificationCategories() async -> Set<UNNotificationCategory>
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func notificationCategories() async -> Set<UNNotificationCategory>
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to retrieve your app’s currently registered notification types. You might use this method when you want to augment the current set of categories with new categories later on. Simply merge the returned set with any new category objects and register the updated set.

```swift
let center = UNUserNotificationCenter.current()
let categories = await center.notificationCategories()
```

## Parameters

- `completionHandler`: The block to execute asynchronously with the results. This block may be executed on a background thread. The block has no return value and takes the following parameter:

## See Also

- [func setNotificationCategories(Set<UNNotificationCategory>)](unusernotificationcenter/setnotificationcategories(_:).md)
  Registers the notification categories that your app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getnotificationcategories(completionhandler:))*