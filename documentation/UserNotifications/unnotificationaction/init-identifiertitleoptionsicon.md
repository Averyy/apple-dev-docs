# init(identifier:title:options:icon:)

**Framework**: User Notifications  
**Kind**: init

Creates an action object by using the specified title, options, and icon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(identifier: String, title: String, options: UNNotificationActionOptions = [], icon: UNNotificationActionIcon?)
```

#### Return Value

An action object that the system initializes.

## Parameters

- `identifier`: The string that you use internally to identify the action. This string must be unique among your app’s supported actions. When the user selects the action, the system passes this string to your app and asks the user to perform the related task. This parameter must not be   or an empty string.
- `title`: The localized string the system displays to the user. The system displays this string as the title of a button, which the system adds to the notification interface. This parameter must not be  .
- `options`: Additional options that describe how the action behaves. Include options when you need the related behavior. For a list of possible values, see  .
- `icon`: The icon that the system displays to the user.

## See Also

- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions)](unnotificationaction/init(identifier:title:options:).md)
  Creates an action object by using the specified title and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction/init(identifier:title:options:icon:))*