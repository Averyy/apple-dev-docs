# notificationResponse

**Framework**: UIKit  
**Kind**: property

A person’s response to one of your app’s notifications.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var notificationResponse: UNNotificationResponse? { get }
```

#### Discussion

When UIKit connects a scene in order to process a notification, it puts the response object in this property. Use the information in this object to configure your scene. If a person selected one of the notification’s actions, perform that action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/notificationresponse)*