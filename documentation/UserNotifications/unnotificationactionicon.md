# UNNotificationActionIcon

**Framework**: User Notifications  
**Kind**: class  
**Role**: Class

An icon associated with an action.

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
class UNNotificationActionIcon
```

```objc
@interface UNNotificationActionIcon : NSObject
```

## Topics

### Essentials
- [convenience init(systemImageName: String)](./unnotificationactionicon/init%28systemimagename%29.md)
  Creates an action icon by using a system symbol image.
- [convenience init(templateImageName: String)](./unnotificationactionicon/init%28templateimagename%29.md)
  Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.
### Initializers
- [init?(coder: NSCoder)](./unnotificationactionicon/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Notification content
- [Implementing communication notifications](./implementing-communication-notifications.md)
  Configure and display your app’s communication notifications by using intents.
- [protocol UNNotificationContentProviding](./unnotificationcontentproviding.md)
  A protocol the system uses to provide context relevant to user notifications.
- [class UNMutableNotificationContent](./unmutablenotificationcontent.md)
  The editable content for a notification.
- [class UNNotificationContent](./unnotificationcontent.md)
  The uneditable content of a notification.
- [class UNNotificationAttachment](./unnotificationattachment.md)
  A media file associated with a notification.
- [class UNNotificationSound](./unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](./unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionicon)*