# UNNotificationContent

**Framework**: Usernotifications  
**Kind**: class

The uneditable content of a notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNNotificationContent
```

## Mentions

- [Generating a remote notification](generating-a-remote-notification.md)

#### Overview

A [`UNNotificationContent`](unnotificationcontent.md) object contains the data associated with a notification. When your app receives a notification, the associated [`UNNotificationRequest`](unnotificationrequest.md) object contains an object of this type with the content that your app received. Use the content object to get the details of the notification, including the type of notification that the system delivered, any custom data you stored in the [`userInfo`](unnotificationcontent/userinfo.md) dictionary before scheduling the notification, and any attachments.

Don’t create instances of this class directly. For remote notifications, the system derives the contents of this object from the JSON payload that your server sends to the APNS server. For local notifications, create a [`UNMutableNotificationContent`](unmutablenotificationcontent.md) object, and configure the contents of that object instead.

## Topics

### Accessing the primary content
- [var title: String](unnotificationcontent/title.md)
  The localized text that provides the notification’s primary description.
- [var subtitle: String](unnotificationcontent/subtitle.md)
  The localized text that provides the notification’s secondary description.
- [var body: String](unnotificationcontent/body.md)
  The localized text that provides the notification’s main content.
### Accessing supplementary content
- [var attachments: [UNNotificationAttachment]](unnotificationcontent/attachments.md)
  The visual and audio attachments to display alongside the notification’s main content.
- [var userInfo: [AnyHashable : Any]](unnotificationcontent/userinfo.md)
  The custom data to associate with the notification.
### Reading app configuration
- [var launchImageName: String](unnotificationcontent/launchimagename.md)
  The name of the image or storyboard to use when your app launches because of the notification.
- [var badge: NSNumber?](unnotificationcontent/badge.md)
  The number that your app’s icon displays.
- [var targetContentIdentifier: String?](unnotificationcontent/targetcontentidentifier.md)
  The value your app uses to determine which scene to display to handle the notification.
### Reading system configuration
- [var sound: UNNotificationSound?](unnotificationcontent/sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](unnotificationcontent/interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](unnotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](unnotificationcontent/filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.
### Retrieving group information
- [var threadIdentifier: String](unnotificationcontent/threadidentifier.md)
  The identifier that groups related notifications.
- [var categoryIdentifier: String](unnotificationcontent/categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgument: String](unnotificationcontent/summaryargument.md)
  The text the system adds to the notification summary to provide additional context.
- [var summaryArgumentCount: Int](unnotificationcontent/summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.
### Updating the notification’s content
- [func updating(from: any UNNotificationContentProviding) throws -> UNNotificationContent](unnotificationcontent/updating(from:).md)
  Returns a copy of the notification that includes content from the specified provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UNMutableNotificationContent](unmutablenotificationcontent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Implementing communication notifications](implementing-communication-notifications.md)
  Configure and display your app’s communication notifications by using intents.
- [protocol UNNotificationContentProviding](unnotificationcontentproviding.md)
  A protocol the system uses to provide context relevant to user notifications.
- [class UNNotificationActionIcon](unnotificationactionicon.md)
  An icon associated with an action.
- [class UNMutableNotificationContent](unmutablenotificationcontent.md)
  The editable content for a notification.
- [class UNNotificationAttachment](unnotificationattachment.md)
  A media file associated with a notification.
- [class UNNotificationSound](unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent)*