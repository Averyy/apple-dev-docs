# userInfo

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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
var userInfo: [AnyHashable : Any] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSDictionary * userInfo;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSDictionary * userInfo;
```

## Mentions

- [Declaring your actionable notification types](../declaring-your-actionable-notification-types.md)
- [Generating a remote notification](../generating-a-remote-notification.md)

#### Discussion

For remote notifications, this property contains the entire notification payload. For local notifications, you configure the property directly before scheduling the notification.

The keys in this dictionary must be property-list types—that’s, they must be types that can be serialized into the property-list format. For information about property-list types, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Accessing supplementary content
- [var attachments: [UNNotificationAttachment]](./attachments.md)
  The visual and audio attachments to display alongside the notification’s main content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/userinfo)*