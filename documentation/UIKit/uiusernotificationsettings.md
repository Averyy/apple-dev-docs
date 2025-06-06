# UIUserNotificationSettings

**Framework**: UIKit  
**Kind**: class

The types of notifications that can be displayed to the user by your app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIUserNotificationSettings
```

#### Overview

Apps that use visible or audible alerts in conjunction with a local or push notification must register the types of alerts they employ. UIKit correlates the information you provide with the user’s preferences to determine what types of alerts your app is allowed to employ.

Use this class to encapsulate your initial registration request and to view the request results. After creating an instance of this class and specifying your preferred settings, call the [`registerUserNotificationSettings(_:)`](uiapplication/registerusernotificationsettings(_:).md) method of the [`UIApplication`](uiapplication.md) class to register those settings. After checking your request against the user preferences, the app delivers the results to the [`application(_:didRegister:)`](uiapplicationdelegate/application(_:didregister:).md) method of its app delegate. The object passed to that method specifies the types of notifications that your app is allowed to use.

In addition to registering your app’s alert types, you can also use this class to register groups of custom actions to display in conjunction with local or push notifications. Custom actions represent immediate tasks your app can perform in response to the notification. You define groups of actions and associate the entire group with a given notification. When the corresponding alert is displayed, the system adds buttons for each action you specified. When the user taps the button for one of the actions, the system wakes your app and calls the [`application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:).md) or [`application(_:handleActionWithIdentifier:for:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md) method of its app delegate. Use those methods to perform the requested action.

## Topics

### Creating a settings object
- [convenience init(types: UIUserNotificationType, categories: Set<UIUserNotificationCategory>?)](uiusernotificationsettings/init(types:categories:).md)
  Creates and returns a settings object that you can use to register your requested notification and action types.
### Getting the configured settings
- [var types: UIUserNotificationType](uiusernotificationsettings/types.md)
  A bitmask of the notification types that your app is allowed to use.
- [var categories: Set<UIUserNotificationCategory>?](uiusernotificationsettings/categories.md)
  The app’s registered groups of actions.
### Constants
- [struct UIUserNotificationType](uiusernotificationtype.md)
  Constants indicating how the app alerts the user when a local or push notification arrives.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](uipreviewaction.md)
  A preview action, or , that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UISearchDisplayController](uisearchdisplaycontroller.md)
  An object that manages the display of a search bar, along with a table view that displays search results.
- [class UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationsettings)*