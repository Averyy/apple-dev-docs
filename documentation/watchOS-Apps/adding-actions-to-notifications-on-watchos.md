# Adding actions to notifications on watchOS

**Framework**: Watchos Apps

Provide a set of responses to a notification.

#### Overview

An  is a notification with associated actions, letting the user respond directly from the notification’s long-look interface.

To create an actionable notification:

- Define a notification category.
- Associate actions with the category.
- Assign the category to a notification.

On Apple Watch, the long-look interface displays the actions as buttons below the notification’s content. Your watchOS app can also provide suggested responses for text input actions and can respond to actions from notifications received on the watch.

> **Note**: Interactive notifications and actionable notifications play similar but distinct roles. An interactive notification enables direct interaction with the notification from the long-look interface, but the system keeps the interactive notification on screen as it calls the notification controller’s action methods. You typically use interactive notifications to modify the notification’s appearance, such as showing or hiding additional information. Actionable notifications, on the other hand, pass control back to your app. Use actionable notifications to enable users to trigger actions based on the notification. For more information, see [`Customizing your long-look interface`](customizing-your-long-look-interface.md).

Interactive notifications and actionable notifications play similar but distinct roles. An interactive notification enables direct interaction with the notification from the long-look interface, but the system keeps the interactive notification on screen as it calls the notification controller’s action methods. You typically use interactive notifications to modify the notification’s appearance, such as showing or hiding additional information. Actionable notifications, on the other hand, pass control back to your app. Use actionable notifications to enable users to trigger actions based on the notification. For more information, see [`Customizing your long-look interface`](customizing-your-long-look-interface.md).

##### Register Actions with the Category

Before you can add actions to a notification, you must create a notification category and register the actions for that category. A category is just a string identifier that specifies a type of notification used by your app.

To register an action for the category, start by creating the action.

```swift
let action = UNNotificationAction(identifier: "my_action",
                                  title: "My Action",
                                  options: [])
```

When you create an action, you specify the title for the action button and the action’s identifier. By default, the system launches your app in the background to handle the action. If you want your app to handle actions in the foreground, you must specify the [`foreground`](https://developer.apple.com/documentation/UserNotifications/UNNotificationActionOptions/foreground) option when creating the action.

Next, create a category that uses the action.

```swift
let category = UNNotificationCategory(identifier: "my_category",
                                      actions: [action],
                                      intentIdentifiers: [],
                                      options: [])
```

Then, register the category with the shared notification center.

```swift
UNUserNotificationCenter.current().setNotificationCategories([category])
```

Additionally, in the watchOS app, you can check the current actions and dynamically disable any of these actions using the notification controller’s [`notificationActions`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/notificationActions) property during its [`didReceive(_:)`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/didReceive(_:)) method.

Create the category and actions on the notification’s target. For example, if you send a local or remote notification to the user’s iPhone, define the category and action in the iOS app — even if the system automatically forwards the notification to their Apple Watch. However, if you send notifications directly to both iPhone and Apple Watch, create the category and actions on both devices.

For more information about creating actions, see [`Declaring your actionable notification types`](https://developer.apple.com/documentation/UserNotifications/declaring-your-actionable-notification-types).

##### Set the Notifications Category

To add the actions to a notification, specify the category in the notification’s content. For local notifications, specify the category name using the [`categoryIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent/categoryIdentifier) property of your [`UNMutableNotificationContent`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent) object. For remote notifications, set the category name as the value of the `category` key in the notification’s payload.

When the system receives a notification, it uses the category name to look up the associated actions. It then creates buttons for each action and attaches those buttons to the notification interface.

##### Offer Text Input Suggestions

Most actions simply create a button that the user can select, but text input actions let the user type in a response. When the user selects a text input action, the system displays a control that lets the user enter or dictate text. The system then includes this text in the response object that it delivers to your app. For more information, see [`UNTextInputNotificationAction`](https://developer.apple.com/documentation/UserNotifications/UNTextInputNotificationAction).

On watchOS, you can provide suggested responses, making it easier for users to respond. To provide suggested responses, override the notification interface controller’s [`suggestionsForResponseToAction(withIdentifier:for:inputLanguage:)`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/suggestionsForResponseToAction(withIdentifier:for:inputLanguage:)) method and return an array of strings. When the user selects the associated action, watchOS presents these strings as suggestions.

##### Respond to Actions

When the user taps an action button, the system launches your app and calls your notification delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method. The response parameter’s [`actionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationResponse/actionIdentifier) property contains the identifier for the selected action. Implement your delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method to check this identifier, and then perform the corresponding task. For more information, see [`Handling notifications and notification-related actions`](https://developer.apple.com/documentation/UserNotifications/handling-notifications-and-notification-related-actions).

When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](https://developer.apple.com/documentation/UserNotifications/UNNotificationActionOptions/destructive) option, and won’t delete user data or change the app irrevocably.

The following rules define where the system handles the action:

- The system always handles foreground actions on the device where the user selected the action. For example, if you send a remote notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it on the watch.
- The system always handles background actions on the device that was the notification’s target. For example, if you send a notification to the user’s iPhone and the system automatically forwards it to their Apple Watch, tapping the action runs it in the background on their iPhone.

## See Also

- [Taking advantage of notification forwarding](taking-advantage-of-notification-forwarding.md)
  Deliver notifications to the user’s iPhone or Apple Watch.
- [Customizing your long-look interface](customizing-your-long-look-interface.md)
  Create custom interfaces for your watchOS app’s notifications.
- [Grouping notifications](grouping-notifications.md)
  Organize notifications into threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/adding-actions-to-notifications-on-watchos)*