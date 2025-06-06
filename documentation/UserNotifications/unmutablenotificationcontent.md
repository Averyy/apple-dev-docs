# UNMutableNotificationContent

**Framework**: Usernotifications  
**Kind**: class

The editable content for a notification.

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
class UNMutableNotificationContent
```

## Mentions

- [Modifying content in newly delivered notifications](modifying-content-in-newly-delivered-notifications.md)
- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Overview

Create a [`UNMutableNotificationContent`](unmutablenotificationcontent.md) object when you want to specify the payload for a local notification. Specifically, use this object to specify the title and message for an alert, the sound to play, or the value to assign to your app’s badge. You might also provide details about how the system handles the notification. For example, you can specify a custom launch image and a thread identifier for visually grouping related notifications.

After creating your content object, assign it to a [`UNNotificationRequest`](unnotificationrequest.md) object, add a trigger condition, and schedule your notification. The trigger condition defines when the system delivers the notification to the user. Listing 1 shows the scheduling of a local notification that displays an alert and plays a sound after a delay of five seconds. Store the strings for the alert’s title and body in the app’s `Localizable.strings` file.

Listing 1. Creating the content for a local notification

> **Note**:  Local notifications always result in user interactions, and the system ignores any interactions for which your app isn’t authorized. For information about how to request authorization for user interactions, see [`Asking permission to use notifications`](asking-permission-to-use-notifications.md).

 Local notifications always result in user interactions, and the system ignores any interactions for which your app isn’t authorized. For information about how to request authorization for user interactions, see [`Asking permission to use notifications`](asking-permission-to-use-notifications.md).

##### Localizing the Alert Strings

Localize the strings you display in a notification alert for the current user. Although you can use the [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) macros to load strings from your app’s resource files, a better option is to specify your string using the [`localizedUserNotificationString(forKey:arguments:)`](https://developer.apple.com/documentation/foundation/nsstring/1649585-localizedusernotificationstring) method of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). The [`localizedUserNotificationString(forKey:arguments:)`](https://developer.apple.com/documentation/foundation/nsstring/1649585-localizedusernotificationstring) method delays the loading of the localized string until the system delivers the notification. If the user changes the language setting before the system delivers a notification, the system updates the alert text to the user’s current language instead of the language in use when the system scheduled the notification.

## Topics

### Providing the primary content
- [var title: String](unmutablenotificationcontent/title.md)
  The localized text that provides the notification’s primary description.
- [var subtitle: String](unmutablenotificationcontent/subtitle.md)
  The localized text that provides the notification’s secondary description.
- [var body: String](unmutablenotificationcontent/body.md)
  The localized text that provides the notification’s main content.
### Providing supplementary content
- [var attachments: [UNNotificationAttachment]](unmutablenotificationcontent/attachments.md)
  The visual and audio attachments to display alongside the notification’s main content.
- [var userInfo: [AnyHashable : Any]](unmutablenotificationcontent/userinfo.md)
  The custom data to associate with the notification.
### Configuring app behavior
- [var launchImageName: String](unmutablenotificationcontent/launchimagename.md)
  The name of the image or storyboard to use when your app launches because of the notification.
- [var badge: NSNumber?](unmutablenotificationcontent/badge.md)
  The number that your app’s icon displays.
- [var targetContentIdentifier: String?](unmutablenotificationcontent/targetcontentidentifier.md)
  The value your app uses to determine which scene to display to handle the notification.
### Integrating with the system
- [var sound: UNNotificationSound?](unmutablenotificationcontent/sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](unmutablenotificationcontent/interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](unmutablenotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](unmutablenotificationcontent/filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.
### Grouping notifications
- [var threadIdentifier: String](unmutablenotificationcontent/threadidentifier.md)
  The identifier that groups related notifications.
- [var categoryIdentifier: String](unmutablenotificationcontent/categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgument: String](unmutablenotificationcontent/summaryargument.md)
  The text the system adds to the notification summary to provide additional context.
- [var summaryArgumentCount: Int](unmutablenotificationcontent/summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.

## Relationships

### Inherits From
- [UNNotificationContent](unnotificationcontent.md)
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
- [class UNNotificationContent](unnotificationcontent.md)
  The uneditable content of a notification.
- [class UNNotificationAttachment](unnotificationattachment.md)
  A media file associated with a notification.
- [class UNNotificationSound](unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent)*