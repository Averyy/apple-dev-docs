# UIStoryboardPopoverSegue

**Framework**: UIKit  
**Kind**: class

A specific type of segue for presenting content in a popover.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class UIStoryboardPopoverSegue
```

#### Overview

For popover segues, the destination view controller contains the content to be displayed in the popover. This class provides an additional [`popoverController`](uistoryboardpopoversegue/popovercontroller.md) property so that your custom code has access to the popover controller object. For example, you might want to store the popover controller elsewhere in your code so that you can dismiss the popover programmatically.

## Topics

### Accessing the segue attributes
- [var popoverController: UIPopoverController](uistoryboardpopoversegue/popovercontroller.md)
  The popover controller used to display the destination view controller.

## Relationships

### Inherits From
- [UIStoryboardSegue](uistoryboardsegue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue)*