# didBecomeVisibleNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when a window becomes visible.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
nonisolated
class let didBecomeVisibleNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIWindowDidBecomeVisibleNotification;
```

#### Discussion

The notification object is the visible window. This notification doesn’t contain a `userInfo` dictionary.

Switching between apps doesn’t generate visibility-related notifications for windows. Window visibility changes reflect changes to the window’s [`isHidden`](../uiview/ishidden.md) property and reflect only the window’s visibility within the app.

The system posts this notification on the main actor.

## See Also

### Responding to window-related notifications
- [class let didBecomeHiddenNotification: NSNotification.Name](./didbecomehiddennotification.md)
  A notification that posts when a window becomes hidden.
- [class let didBecomeKeyNotification: NSNotification.Name](./didbecomekeynotification.md)
  A notification that posts whenever a window becomes the key window.
- [class let didResignKeyNotification: NSNotification.Name](./didresignkeynotification.md)
  A notification that posts whenever a window resigns its status as main window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/didbecomevisiblenotification)*