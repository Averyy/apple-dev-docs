# Notifications

**Framework**: Application Services

Define the notifications that can be broadcast by an accessibility object.

## Topics

### Constants
- [var kAXMainWindowChangedNotification: String](kaxmainwindowchangednotification.md)
  The main window has changed.
- [var kAXFocusedWindowChangedNotification: String](kaxfocusedwindowchangednotification.md)
  The focused window has changed.
- [var kAXFocusedUIElementChangedNotification: String](kaxfocuseduielementchangednotification.md)
  The focused accessibility object has changed.
- [var kAXApplicationActivatedNotification: String](kaxapplicationactivatednotification.md)
  The application was activated (that is, brought to front).
- [var kAXApplicationDeactivatedNotification: String](kaxapplicationdeactivatednotification.md)
  The application was deactivated.
- [var kAXApplicationHiddenNotification: String](kaxapplicationhiddennotification.md)
  The application was hidden.
- [var kAXApplicationShownNotification: String](kaxapplicationshownnotification.md)
  The application was shown (that is, a hidden application is now visible).
- [var kAXWindowCreatedNotification: String](kaxwindowcreatednotification.md)
  A window was created. Carbon automatically sends this notification when window is created, as long as the window is implemented using Carbon window mechanisms.
- [var kAXWindowMovedNotification: String](kaxwindowmovednotification.md)
  The window was moved (this notification is sent at the end of the window-move operation, not during it).
- [var kAXWindowResizedNotification: String](kaxwindowresizednotification.md)
  The window was resized (this notification is sent at the end of the window-resize operation, not during it).
- [var kAXWindowMiniaturizedNotification: String](kaxwindowminiaturizednotification.md)
  The application was minimized (that is, moved into the Dock).
- [var kAXWindowDeminiaturizedNotification: String](kaxwindowdeminiaturizednotification.md)
  The window was moved out of the Dock.
- [var kAXDrawerCreatedNotification: String](kaxdrawercreatednotification.md)
  A drawer was created (that is, a drawer now extends from this window).
- [var kAXSheetCreatedNotification: String](kaxsheetcreatednotification.md)
  A sheet was created (that is, a modal dialog now extends from this window).
- [var kAXHelpTagCreatedNotification: String](kaxhelptagcreatednotification.md)
  A help tag is now visible for this accessibility object.
- [var kAXValueChangedNotification: String](kaxvaluechangednotification.md)
  The value of an accessibility object’s value attribute was changed.
- [var kAXUIElementDestroyedNotification: String](kaxuielementdestroyednotification.md)
  An accessibility object was disposed of.
- [var kAXMenuOpenedNotification: String](kaxmenuopenednotification.md)
  A menu was opened.
- [var kAXMenuClosedNotification: String](kaxmenuclosednotification.md)
  A menu was closed.
- [var kAXMenuItemSelectedNotification: String](kaxmenuitemselectednotification.md)
  A menu item was selected.
- [var kAXRowCountChangedNotification: String](kaxrowcountchangednotification.md)
  The number of rows in this table was changed.
- [var kAXSelectedChildrenChangedNotification: String](kaxselectedchildrenchangednotification.md)
  A different subset of this accessibility object’s children were selected.
- [var kAXResizedNotification: String](kaxresizednotification.md)
  The window has changed size.
- [var kAXMovedNotification: String](kaxmovednotification.md)
  The position of this accessibility object was changed.
- [var kAXCreatedNotification: String](kaxcreatednotification.md)
  An accessibility object was created.

## See Also

- [Roles](carbon_accessibility/roles.md)
  Define the values an accessibility object’s role attribute can have.
- [Subroles](carbon_accessibility/subroles.md)
  Define the values for an accessibility object’s subrole attribute.
- [Attributes](carbon_accessibility/attributes.md)
  Define the attributes available for accessibility objects. 
- [Parameterized Attributes](carbon_accessibility/parameterized_attributes.md)
  Define the parameterized attributes an accessibility object can have.
- [Actions](carbon_accessibility/actions.md)
  Define the actions an accessibility object can perform.
- [Orientations and Sort Directions](carbon_accessibility/orientations_and_sort_directions.md)
  Define the values for the orientation and sort-direction attributes of some accessibility objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/carbon_accessibility/notifications)*