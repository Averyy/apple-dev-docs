# setBadgeCount(_:withCompletionHandler:)

**Framework**: Usernotifications  
**Kind**: method

Updates the badge count for your app’s icon.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setBadgeCount(_ newBadgeCount: Int) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setBadgeCount(_ newBadgeCount: Int) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setBadgeCount(_ newBadgeCount: Int) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Here’s an example that sets the badge count to a specific number.

```swift
let center = UNUserNotificationCenter.current()
do {
     // Set the badge count to 3.
     try await center.setBadgeCount(3)
} catch {
     // Handle any errors.
}
```

## Parameters

- `newBadgeCount`: The new value to display.
- `completionHandler`: The handler to execute after the update finishes. If the update fails, the system provides an error that contains additional information about the failure.

## See Also

- [class func current() -> UNUserNotificationCenter](unusernotificationcenter/current.md)
  Returns your app’s notification center.
- [func getNotificationSettings(completionHandler: (UNNotificationSettings) -> Void)](unusernotificationcenter/getnotificationsettings(completionhandler:).md)
  Retrieves the authorization and feature-related settings for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/setbadgecount(_:withcompletionhandler:))*