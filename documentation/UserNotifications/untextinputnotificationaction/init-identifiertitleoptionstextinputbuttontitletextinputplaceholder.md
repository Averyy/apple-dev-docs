# init(identifier:title:options:textInputButtonTitle:textInputPlaceholder:)

**Framework**: User Notifications  
**Kind**: init

Creates an action object that accepts text input from the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(identifier: String, title: String, options: UNNotificationActionOptions = [], textInputButtonTitle: String, textInputPlaceholder: String)
```

#### Return Value

A new text input action object.

## Parameters

- `identifier`: The string that you use internally to identify the action. This string must be unique among all of your app’s supported actions. When the user selects the action, the system passes this string to your app and asks you to perform the related task. This parameter must not be   or an empty string.
- `title`: The localized string the system displays to the user. The system displays this string as the title of a button, which the system adds to the notification interface. This parameter must not be  .
- `options`: Additional options describing how the action behaves. Include options when you need the related behavior. For a list of possible values, see  .
- `textInputButtonTitle`: The localized title of the text input button that’s displayed to the user.
- `textInputPlaceholder`: The localized placeholder text the system displays in the text input field.

## See Also

- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions, icon: UNNotificationActionIcon?, textInputButtonTitle: String, textInputPlaceholder: String)](untextinputnotificationaction/init(identifier:title:options:icon:textinputbuttontitle:textinputplaceholder:).md)
  Creates an action object with an icon that accepts text input from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction/init(identifier:title:options:textinputbuttontitle:textinputplaceholder:))*