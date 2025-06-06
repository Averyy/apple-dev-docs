# UIUserNotificationCategory

**Framework**: UIKit  
**Kind**: class

Information about custom actions that your app can perform in response to a local or push notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIUserNotificationCategory
```

#### Overview

Each instance of `UIUserNotificationCategory` represents a group of actions to display in conjunction with a single notification. The title of each action is uses as the title of a button in the alert displayed to the user. When the user taps a button, the system reports the selected action to your app delegate.

Typically, you create an instance of the [`UIMutableUserNotificationCategory`](uimutableusernotificationcategory.md) class instead of this class. You use the mutable object to add actions and specify a category name before registering them with a [`UIUserNotificationSettings`](uiusernotificationsettings.md) object.

To display a group of actions for a specific notification, configure the local or push notification with the category name of the group. For local notifications, you specify this name when configuring your [`UILocalNotification`](uilocalnotification.md) object. For push notifications, your server specifies a group of actions by adding a `category` key (whose value is the [`identifier`](uiusernotificationcategory/identifier.md) of the group) to the push notification’s payload.

## Topics

### Creating the action group
- [init()](uiusernotificationcategory/init.md)
  Creates an action group.
- [init?(coder: NSCoder)](uiusernotificationcategory/init(coder:).md)
  Creates an action group from data in an unarchiver.
### Getting the group configuration
- [var identifier: String?](uiusernotificationcategory/identifier.md)
  The name of the action group.
- [func actions(for: UIUserNotificationActionContext) -> [UIUserNotificationAction]?](uiusernotificationcategory/actions(for:).md)
  Returns the actions to be displayed for the given notification context.
### Constants
- [enum UIUserNotificationActionContext](uiusernotificationactioncontext.md)
  Constants indicating the amount of space available for displaying actions in a notification.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
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
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationSettings](uiusernotificationsettings.md)
  The types of notifications that can be displayed to the user by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationcategory)*