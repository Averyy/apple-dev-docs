# AXNotificationConstants.h

**Framework**: Application Services

#### Overview

Assistive applications can register to be notified about certain events in a target application. For example, creation of a window or the destruction of a UIElement. To receive notifications you must first create an observer and specify a callback function; second, add the observer's run loop source to the run loop on which you want the callback executed; and third, register the observer for one or more notifications.

When you create the observer, you specify the application being observed. An observer can receive notifications only from UIElements in that application. To handle multiple applications, you have to create at least one observer per application.

When you register an observer for a notification, you specify the UIElement you are interested in observing. When you want to receive a notification from any element in an application, use the application UIElement; you then receive the notification regardless of which element in the application sends the notification. This is useful if the UIElement does not exist yet, such as when a new window is created, or if you care about state changes, such as the keyboard focus moving, without having to observe every element separately. When the callback function is executed it is passed the UIElement that was affected by the notification.

Observers are represented by the AXObserverRef type, which is a CFType. Like all CFTypes they are reference counted (CFRetain/CFRelease).

## Topics

### Callbacks
- [typealias CFIndex](../corefoundation/cfindex.md)
  Priority values used for kAXPriorityKey
### Constants
- [Miscellaneous Defines](axnotificationconstants_h/miscellaneous_defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axnotificationconstants_h)*