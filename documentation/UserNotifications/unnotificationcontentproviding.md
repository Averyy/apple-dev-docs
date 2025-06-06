# UNNotificationContentProviding

**Framework**: Usernotifications  
**Kind**: protocol

A protocol the system uses to provide context relevant to user notifications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol UNNotificationContentProviding : NSObjectProtocol
```

#### Overview

The system allows only objects in the Apple SDK that conform to `UNNotificationContentProviding`. The system ignores objects outside of the Apple SDK that your app conforms to `UNNotificationContentProviding`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UNNotificationAttributedMessageContext](unnotificationattributedmessagecontext.md)

## See Also

- [Implementing communication notifications](implementing-communication-notifications.md)
  Configure and display your app’s communication notifications by using intents.
- [class UNNotificationActionIcon](unnotificationactionicon.md)
  An icon associated with an action.
- [class UNMutableNotificationContent](unmutablenotificationcontent.md)
  The editable content for a notification.
- [class UNNotificationContent](unnotificationcontent.md)
  The uneditable content of a notification.
- [class UNNotificationAttachment](unnotificationattachment.md)
  A media file associated with a notification.
- [class UNNotificationSound](unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding)*