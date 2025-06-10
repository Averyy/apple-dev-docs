# userInfo

**Framework**: User Notifications  
**Kind**: property

The custom data to associate with the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any] { get set }
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Discussion

Use this property to associate custom information with the notification. The contents of the dictionary aren’t seen by the user, but are accessible to your app or to any notification-related app extensions.

The keys in this dictionary must be types that can be serialized into the property-list format. For information about property-list types, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

- [var attachments: [UNNotificationAttachment]](unmutablenotificationcontent/attachments.md)
  The visual and audio attachments to display alongside the notification’s main content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/userinfo)*