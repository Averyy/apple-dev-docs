# UIUserNotificationAction

**Framework**: UIKit  
**Kind**: class

A custom action that your app can perform in response to a remote or local notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIUserNotificationAction
```

#### Overview

When a notification is delivered, the system displays a button for each custom action associated with the notification. Tapping a button launches your app (either in the foreground or background) and gives you a chance to perform the indicated action. You use this class to specify the text that is displayed in the button and the information your app needs to perform the corresponding action.

Typically, you create an instance of the [`UIMutableUserNotificationAction`](uimutableusernotificationaction.md) class instead of this class. You use the mutable object to configure the action and then call the setActions:forContext: method of UIMutableUserNotificationActionSettings to add the resulting actions to a group.

For each action you define, you must specify whether execution of that action requires the app to be running in the foreground or background. You can also specify whether the device must be unlocked or can remain locked while the action is performed. Unlocking the device may be necessary if the action involves reading or writing files that are encrypted on disk using the system’s data protection mechanism. When the user selects an action, the system puts your app into the appropriate mode and calls your app delegate’s [`application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:).md) or [`application(_:handleActionWithIdentifier:for:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md) method to perform the action.

## Topics

### Creating the action
- [init()](uiusernotificationaction/init.md)
  Creates a user notification action.
- [init?(coder: NSCoder)](uiusernotificationaction/init(coder:).md)
  Creates a user notification action from data in an unarchiver.
### Getting the action information
- [var identifier: String?](uiusernotificationaction/identifier.md)
  The string that you use internally to identify the action.
- [var title: String?](uiusernotificationaction/title.md)
  The localized string to use as the button title for the action.
### Getting the action’s configuration
- [var activationMode: UIUserNotificationActivationMode](uiusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](uiusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](uiusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](uiusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](uiusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.
### Constants
- [enum UIUserNotificationActivationMode](uiusernotificationactivationmode.md)
  Constants indicating whether the app should activate to the foreground or background.
- [enum UIUserNotificationActionBehavior](uiusernotificationactionbehavior.md)
  Constants indicating additional behavior that the action supports.
- [Action Parameter Key](action-parameter-key.md)
  Key to include among the parameters of the action.
- [Behavior Key](behavior-key.md)
  Key related to action-related behaviors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIMutableUserNotificationAction](uimutableusernotificationaction.md)
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
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction)*