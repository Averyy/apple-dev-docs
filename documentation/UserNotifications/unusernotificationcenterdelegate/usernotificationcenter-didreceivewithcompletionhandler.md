# userNotificationCenter(_:didReceive:withCompletionHandler:)

**Framework**: User Notifications  
**Kind**: method

Asks the delegate to process the user’s response to a delivered notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse) async
```

## Mentions

- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md)
- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to process the user’s response to a notification. If the user selected one of your app’s custom actions, the `response` parameter contains the identifier for that action. (The response can also indicate that the user dismissed the notification interface, or launched your app, without selecting a custom action.) At the end of your implementation, call the `completionHandler` block to let the system know that you are done processing the user’s response. If you do not implement this method, your app never responds to custom actions.

You specify your app’s notification types at app launch using [`UNNotificationCategory`](unnotificationcategory.md) objects, and you specify the custom actions for each type using [`UNNotificationAction`](unnotificationaction.md) objects. For information, see [`Declaring your actionable notification types`](declaring-your-actionable-notification-types.md).

## Parameters

- `center`: The shared user notification center object that received the notification.
- `response`: The user’s response to the notification. This object contains the original notification and the identifier string for the selected action. If the action allowed the user to provide a textual response, this parameter contains a   object.
- `completionHandler`: The block to execute when you have finished processing the user’s response. You must execute this block at some point after processing the user’s response to let the system know that you are done. The block has no return value or parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/usernotificationcenter(_:didreceive:withcompletionhandler:))*