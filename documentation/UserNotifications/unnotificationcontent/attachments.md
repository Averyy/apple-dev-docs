# attachments

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The visual and audio attachments to display alongside the notification’s main content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var attachments: [UNNotificationAttachment] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<UNNotificationAttachment *> * attachments;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<UNNotificationAttachment *> * attachments;
```

## Discussion

Use this property to retrieve the images, movies, and audio files associated with your notification’s content. A notification content app extension might use these values to add the associated content to its view controller.

## See Also

### Accessing supplementary content
- [var userInfo: [AnyHashable : Any]](./userinfo.md)
  The custom data to associate with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/attachments)*