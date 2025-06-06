# UNTextInputNotificationAction

**Framework**: Usernotifications  
**Kind**: class

An action that accepts user-typed text.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNTextInputNotificationAction
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Overview

Use [`UNTextInputNotificationAction`](untextinputnotificationaction.md) objects to define an action that allows the user to provide a custom text-based response. When the user selects an action of this type, the system displays controls for the user to enter or dictate the text content. That text is then included in the response object that’s delivered to your app.

For information on how to define actions and categories, see [`Declaring your actionable notification types`](declaring-your-actionable-notification-types.md).

## Topics

### Essentials
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions, textInputButtonTitle: String, textInputPlaceholder: String)](untextinputnotificationaction/init(identifier:title:options:textinputbuttontitle:textinputplaceholder:).md)
  Creates an action object that accepts text input from the user.
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions, icon: UNNotificationActionIcon?, textInputButtonTitle: String, textInputPlaceholder: String)](untextinputnotificationaction/init(identifier:title:options:icon:textinputbuttontitle:textinputplaceholder:).md)
  Creates an action object with an icon that accepts text input from the user.
### Getting Information
- [var textInputButtonTitle: String](untextinputnotificationaction/textinputbuttontitle.md)
  The localized title of the text input button that the system displays to the user.
- [var textInputPlaceholder: String](untextinputnotificationaction/textinputplaceholder.md)
  The placeholder text that the system localizes and displays in the text input field.

## Relationships

### Inherits From
- [UNNotificationAction](unnotificationaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)
  Differentiate your notifications and add action buttons to the notification interface.
- [class UNNotificationCategory](unnotificationcategory.md)
  A type of notification your app supports and the custom actions that the system displays.
- [class UNNotificationAction](unnotificationaction.md)
  A task your app performs in response to a notification that the system delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction)*