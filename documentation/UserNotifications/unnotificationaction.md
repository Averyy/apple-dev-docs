# UNNotificationAction

**Framework**: User Notifications  
**Kind**: class  
**Role**: Class

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

```objc
@interface UNNotificationAction : NSObject
```

## Mentions

- [Declaring your actionable notification types](./declaring-your-actionable-notification-types.md)

## Overview

Use [`UNNotificationAction`](./unnotificationaction.md) objects to define the actions that your app can perform in response to a delivered notification. You define the actions that your app supports. For example, a meeting app might define actions for accepting or rejecting a meeting invitation. The action object itself contains the title to display in an action button and the button’s appearance. After creating action objects, add them to a [`UNNotificationCategory`](./unnotificationcategory.md) object and register your categories with the system.

> **Note**:  When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](./unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

For information on how to define actions and categories, see [Declaring your actionable notification types](./declaring-your-actionable-notification-types.md).

### Responding to the Selection of Actions

When the user selects one of your actions in response to a notification, the system notifies the delegate of the shared [`UNUserNotificationCenter`](./unusernotificationcenter.md) object. Specifically, the system calls the [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](./unusernotificationcenterdelegate/usernotificationcenter%28_,didreceive,withcompletionhandler%29.md) method of your delegate object. The response object passed to your delegate includes the [`identifier`](./unnotificationaction/identifier.md) string of the action the user selects, which you can use to perform the corresponding task.

For information on how to handle actions, see [Handling notifications and notification-related actions](./handling-notifications-and-notification-related-actions.md).

## Topics

### Essentials
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions)](./unnotificationaction/init%28identifier,title,options%29.md)
  Creates an action object by using the specified title and options.
- [convenience init(identifier: String, title: String, options: UNNotificationActionOptions, icon: UNNotificationActionIcon?)](./unnotificationaction/init%28identifier,title,options,icon%29.md)
  Creates an action object by using the specified title, options, and icon.
### Getting Information
- [var identifier: String](./unnotificationaction/identifier.md)
  The unique string that your app uses to identify the action.
- [var title: String](./unnotificationaction/title.md)
  The localized string to use as the title of the action.
- [var icon: UNNotificationActionIcon?](./unnotificationaction/icon.md)
  The icon associated with the action.
### Getting Options
- [var options: UNNotificationActionOptions](./unnotificationaction/options.md)
  The behaviors associated with the action.
- [struct UNNotificationActionOptions](./unnotificationactionoptions.md)
  The behaviors you can apply to an action.
- [UNNotificationActionOptionNone](./unnotificationactionoptionnone.md)
  The action has the default behavior.
### Initializers
- [init?(coder: NSCoder)](./unnotificationaction/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UNTextInputNotificationAction](./untextinputnotificationaction.md)
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

### Notification categories and user actions
- [Declaring your actionable notification types](./declaring-your-actionable-notification-types.md)
  Differentiate your notifications and add action buttons to the notification interface.
- [class UNNotificationCategory](./unnotificationcategory.md)
  A type of notification your app supports and the custom actions that the system displays.
- [class UNTextInputNotificationAction](./untextinputnotificationaction.md)
  An action that accepts user-typed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction)*