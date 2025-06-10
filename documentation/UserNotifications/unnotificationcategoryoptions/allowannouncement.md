# allowAnnouncement

**Framework**: User Notifications  
**Kind**: property

An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var allowAnnouncement: UNNotificationCategoryOptions { get }
```

#### Discussion

When Siri reads an incoming message to the user, Siri reads the message locally on the userʼs device. Siri doesn’t send the message’s contents or sender to Apple servers. For more information about Siri’s on-device processing, visit [`Apple’s Privacy Page`](https://developer.apple.comhttps://www.apple.com/privacy/features/).

## See Also

- [static var allowInCarPlay: UNNotificationCategoryOptions](unnotificationcategoryoptions/allowincarplay.md)
  Allow CarPlay to display notifications of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/allowannouncement)*