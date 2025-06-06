# UNNotificationAction

**Framework**: Usernotifications  
**Kind**: class

A task your app performs in response to a notification that the system delivers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNNotificationAction
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Overview

Use [`UNNotificationAction`](unnotificationaction.md) objects to define the actions that your app can perform in response to a delivered notification. You define the actions that your app supports. For example, a meeting app might define actions for accepting or rejecting a meeting invitation. The action object itself contains the title to display in an action button and the button’s appearance. After creating action objects, add them to a [`UNNotificationCategory`](unnotificationcategory.md) object and register your categories with the system.

> **Note**:  When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

 When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

For information on how to define actions and categories, see [`Declaring your actionable notification types`](declaring-your-actionable-notification-types.md).

##### Responding to the Selection of Actions

When the user selects one of your actions in response to a notification, the system notifies the delegate of the shared [`UNUserNotificationCenter`](unusernotificationcenter.md) object. Specifically, the system calls the [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](unusernotificationcenterdelegate/usernotificationcenter(_:didreceive:withcompletionhandler:).md) method of your delegate object. The response object passed to your delegate includes the [`identifier`](unnotificationaction/identifier.md) string of the action the user selects, which you can use to perform the corresponding task.

For information on how to handle actions, see [`Handling notifications and notification-related actions`](handling-notifications-and-notification-related-actions.md).

## Topics

### Essentials
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions)](unnotificationaction/init(identifier:title:options:).md)
  Creates an action object by using the specified title and options.
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions, icon: UNNotificationActionIcon?)](unnotificationaction/init(identifier:title:options:icon:).md)
  Creates an action object by using the specified title, options, and icon.
### Getting Information
- [var identifier: String](unnotificationaction/identifier.md)
  The unique string that your app uses to identify the action.
- [var title: String](unnotificationaction/title.md)
  The localized string to use as the title of the action.
- [var icon: UNNotificationActionIcon?](unnotificationaction/icon.md)
  The icon associated with the action.
### Getting Options
- [var options: UNNotificationActionOptions](unnotificationaction/options.md)
  The behaviors associated with the action.
- [struct UNNotificationActionOptions](unnotificationactionoptions.md)
  The behaviors you can apply to an action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UNTextInputNotificationAction](untextinputnotificationaction.md)
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
- [class UNTextInputNotificationAction](untextinputnotificationaction.md)
  An action that accepts user-typed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction)*