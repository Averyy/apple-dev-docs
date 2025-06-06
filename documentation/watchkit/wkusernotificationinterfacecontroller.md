# WKUserNotificationInterfaceController

**Framework**: Watchkit  
**Kind**: class

An interface controller object that manages a dynamic user interface for a local or remote notification.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
class WKUserNotificationInterfaceController
```

#### Overview

Apps that support notifications can define one or more subclasses of [`WKUserNotificationInterfaceController`](wkusernotificationinterfacecontroller.md) and use them to implement their dynamic notification interfaces. For example, you might use a dynamic interface to display custom data from the notification payload or add related graphics.

To create the custom notification interface, add a notification interface controller to your storyboard. Interface Builder provides a static interface and you can add a dynamic interface as needed. Set the class of the dynamic interface controller to the name of your [`WKUserNotificationInterfaceController`](wkusernotificationinterfacecontroller.md) subclass.

Apps can include multiple notification interfaces in their storyboard file, and associate each interface with a different category. Categories define the purpose of an incoming notification and are custom to your app. In Interface Builder, specify the category information for each of your notification interfaces using the notification category object attached to the static notification interface controller. When sending notifications to a user, add the appropriate category string to the remote notification payload or set the string in the [`categoryIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent/categoryIdentifier) property of a local notification.

After initializing your interface controller, WatchKit calls the [`didReceive(_:)`](wkusernotificationinterfacecontroller/didreceive(_:).md) method to provide you with the payload data from the notification. Your implementations of those methods should update any interface objects and call the provided completion handler as quickly as possible. If you don’t call the completion handler in a timely manner, WatchKit displays your static notification interface instead.

##### Actionable Notifications

For each category your app supports, you can also register actions for that category. When a category has registered actions, WatchKit adds a button for each action to the corresponding static or dynamic notification interface. Because the system automatically adds the buttons, don’t manually add your own to your custom notification interface. For more information about registering actions, see [`Declaring your actionable notification types`](https://developer.apple.com/documentation/UserNotifications/declaring-your-actionable-notification-types).

When the user taps an action button, the system launches your app and calls your notification delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method. The response parameter’s [`actionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationResponse/actionIdentifier) property contains the identifier for the selected action. Implement your delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method to check this identifier, and then perform the corresponding task. For more information, see [`Handling notifications and notification-related actions`](https://developer.apple.com/documentation/UserNotifications/handling-notifications-and-notification-related-actions).

The following rules define where the system handles the action:

- The system always handles foreground actions on the device where the user selected the action. For example, if you send a remote notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it on the watch.
- The system always handles background actions on the device that was the notification’s target. For example, if you send a notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it in the background on their iPhone.

##### Interface Builder Configuration Options

Xcode lets you configure information about your notification interface controller in your storyboard file. A notification interface controller supports almost all of the attributes associated with its parent class plus those in the following table.

| Attribute | Description |
| --- | --- |
| Has Dynamic Interface | A checkbox indicating whether the app supports a dynamic interface for notifications of this type. WatchKit displays dynamic interfaces whenever possible, but WatchKit may fall back to using your static interface because of power restrictions or when your WatchKit extension doesn’t respond in a timely manner. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Apple Watch always displays the static interface in Notification Center. |

The notification category object associated with your notification interface controllers also contains configurable attributes. The following table lists the attributes of the notification category object and their meaning.

| Attribute | Description |
| --- | --- |
| Name | The name of the category that this interface supports. For local notifications, this value corresponds to the string in the [`categoryIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent/categoryIdentifier) property of the [`UNNotificationContent`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent) object. For remote notifications, it’s the string in the `category` key in the payload. When a notification arrives, WatchKit uses the category string in the notification to decide which of your interface controllers to display. |
| Sash Color | The color to apply to the sash at the top of the long-look notification interface. |
| Wants Sash Blur | A checkbox indicating whether the sash includes a blur effect over the background. |
| Title Color | The color to apply to the text displayed in the sash. |
| Description | The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the `%d` variable to reflect the number of notifications. If you don’t specify a custom string, WatchKit uses the string `%d Notifications` to reflect the number of notifications that arrived. |
| Has Dynamic Interface | A checkbox indicating whether the app supports dynamic interfaces for notifications of this type. WatchKit displays dynamic interfaces whenever possible, but it may fall back to using your static interface because of power restrictions or when your WatchKit extension doesn’t respond in a timely manner. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Apple Watch always displays the static interface in Notification Center. |

## Topics

### Initializing the Interface Controller
- [init()](wkusernotificationinterfacecontroller/init.md)
  Initializes and returns the interface controller using the specified remote notification data.
### Processing the Notification
- [func didReceive(UNNotification)](wkusernotificationinterfacecontroller/didreceive(_:).md)
  Delivers a notification object to your interface controller for processing.
- [func didReceive(UNNotification, withCompletion: (WKUserNotificationInterfaceType) -> Void)](wkusernotificationinterfacecontroller/didreceive(_:withcompletion:).md)
  Delivers a notification object to your interface controller for processing.
### Working with Actions
- [var notificationActions: [UNNotificationAction]](wkusernotificationinterfacecontroller/notificationactions.md)
  The actions associated with the current notification.
- [func performNotificationDefaultAction()](wkusernotificationinterfacecontroller/performnotificationdefaultaction.md)
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](wkusernotificationinterfacecontroller/performdismissaction.md)
  Dismisses the notification interface controller.
- [func dismiss()](wkusernotificationinterfacecontroller/dismiss.md)
  Dismisses the notification interface controller.
### Offering Suggestions for Text Input
- [func suggestionsForResponseToAction(withIdentifier: String, for: UNNotification, inputLanguage: String) -> [String]](wkusernotificationinterfacecontroller/suggestionsforresponsetoaction(withidentifier:for:inputlanguage:).md)
  Returns an array of attributed strings representing the text suggestions to display during text input.
### Constants
- [enum WKUserNotificationInterfaceType](wkusernotificationinterfacetype.md)
  The type of notification interface to display.

## Relationships

### Inherits From
- [WKInterfaceController](wkinterfacecontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)*