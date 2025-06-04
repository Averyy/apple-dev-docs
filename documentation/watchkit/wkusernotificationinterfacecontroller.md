# WKUserNotificationInterfaceController

**Framework**: Watchkit  
**Kind**: class

An interface controller object that manages a dynamic user interface for a local or remote notification.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor class WKUserNotificationInterfaceController
```

## Overview

Apps that support notifications can define one or more subclasses of [`WKUserNotificationInterfaceController`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller) and use them to implement their dynamic notification interfaces. For example, you might use a dynamic interface to display custom data from the notification payload or add related graphics.

To create the custom notification interface, add a notification interface controller to your storyboard. Interface Builder provides a static interface and you can add a dynamic interface as needed. Set the class of the dynamic interface controller to the name of your [`WKUserNotificationInterfaceController`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller) subclass.

Apps can include multiple notification interfaces in their storyboard file, and associate each interface with a different category. Categories define the purpose of an incoming notification and are custom to your app. In Interface Builder, specify the category information for each of your notification interfaces using the notification category object attached to the static notification interface controller. When sending notifications to a user, add the appropriate category string to the remote notification payload or set the string in the [`categoryIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent/categoryIdentifier) property of a local notification.

After initializing your interface controller, WatchKit calls the [`didReceive(_:)`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)) method to provide you with the payload data from the notification. Your implementations of those methods should update any interface objects and call the provided completion handler as quickly as possible. If you don’t call the completion handler in a timely manner, WatchKit displays your static notification interface instead.

For each category your app supports, you can also register actions for that category. When a category has registered actions, WatchKit adds a button for each action to the corresponding static or dynamic notification interface. Because the system automatically adds the buttons, don’t manually add your own to your custom notification interface. For more information about registering actions, see [`Declaring your actionable notification types`](https://developer.apple.com/documentation/UserNotifications/declaring-your-actionable-notification-types).

When the user taps an action button, the system launches your app and calls your notification delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method. The response parameter’s [`actionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationResponse/actionIdentifier) property contains the identifier for the selected action. Implement your delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method to check this identifier, and then perform the corresponding task. For more information, see [`Handling notifications and notification-related actions`](https://developer.apple.com/documentation/UserNotifications/handling-notifications-and-notification-related-actions).

The following rules define where the system handles the action:

- The system always handles foreground actions on the device where the user selected the action. For example, if you send a remote notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it on the watch.
- The system always handles background actions on the device that was the notification’s target. For example, if you send a notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it in the background on their iPhone.

Xcode lets you configure information about your notification interface controller in your storyboard file. A notification interface controller supports almost all of the attributes associated with its parent class plus those in the following table.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Attribute'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Description'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Has Dynamic Interface'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'A checkbox indicating whether the app supports a dynamic interface for notifications of this type. WatchKit displays dynamic interfaces whenever possible, but WatchKit may fall back to using your static interface because of power restrictions or when your WatchKit extension doesn’t respond in a timely manner. '}, {'type': 'image', 'identifier': 'spacer'}, {'type': 'text', 'text': ' Apple Watch always displays the static interface in Notification Center.'}], 'type': 'paragraph'}] |

The notification category object associated with your notification interface controllers also contains configurable attributes. The following table lists the attributes of the notification category object and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Attribute', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Name', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The name of the category that this interface supports. For local notifications, this value corresponds to the string in the ', 'type': 'text'}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.documentation/documentation/UserNotifications/UNNotificationContent/categoryIdentifier'}, {'text': ' property of the ', 'type': 'text'}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.documentation/documentation/UserNotifications/UNNotificationContent'}, {'text': ' object. For remote notifications, it’s the string in the ', 'type': 'text'}, {'code': 'category', 'type': 'codeVoice'}, {'text': ' key in the payload. When a notification arrives, WatchKit uses the category string in the notification to decide which of your interface controllers to display.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Sash Color', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The color to apply to the sash at the top of the long-look notification interface.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Wants Sash Blur', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A checkbox indicating whether the sash includes a blur effect over the background.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Title Color', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The color to apply to the text displayed in the sash.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the ', 'type': 'text'}, {'code': '%d', 'type': 'codeVoice'}, {'text': ' variable to reflect the number of notifications. If you don’t specify a custom string, WatchKit uses the string ', 'type': 'text'}, {'code': '%d Notifications', 'type': 'codeVoice'}, {'text': ' to reflect the number of notifications that arrived.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Has Dynamic Interface', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'A checkbox indicating whether the app supports dynamic interfaces for notifications of this type. WatchKit displays dynamic interfaces whenever possible, but it may fall back to using your static interface because of power restrictions or when your WatchKit extension doesn’t respond in a timely manner. ', 'type': 'text'}, {'identifier': 'spacer', 'type': 'image'}, {'text': ' Apple Watch always displays the static interface in Notification Center.', 'type': 'text'}]}] |

## Topics

### Initializing the Interface Controller
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/init()))
  Initializes and returns the interface controller using the specified remote notification data.
### Processing the Notification
- [func didReceive(UNNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)))
  Delivers a notification object to your interface controller for processing.
- [func didReceive(UNNotification, withCompletion: (WKUserNotificationInterfaceType) -> Void)](didreceive(_:withcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:withcompletion:)))
  Delivers a notification object to your interface controller for processing.
### Working with Actions
- [var notificationActions: [UNNotificationAction]](notificationactions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/notificationactions))
  The actions associated with the current notification.
- [func performNotificationDefaultAction()](performnotificationdefaultaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performnotificationdefaultaction()))
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](performdismissaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performdismissaction()))
  Dismisses the notification interface controller.
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/dismiss()))
  Dismisses the notification interface controller.
### Offering Suggestions for Text Input
- [func suggestionsForResponseToAction(withIdentifier: String, for: UNNotification, inputLanguage: String) -> [String]](suggestionsforresponsetoaction(withidentifier:for:inputlanguage:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/suggestionsforresponsetoaction(withidentifier:for:inputlanguage:)))
  Returns an array of attributed strings representing the text suggestions to display during text input.
### Constants
- [enum WKUserNotificationInterfaceType](wkusernotificationinterfacetype.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype))
  The type of notification interface to display.

## Relationships

### Inherits From
- [WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)*