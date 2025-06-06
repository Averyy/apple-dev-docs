# didBecomeVisibleNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when a window becomes visible.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let didBecomeVisibleNotification: NSNotification.Name
```

#### Discussion

The notification object is the visible window. This notification doesn’t contain a `userInfo` dictionary.

Switching between apps doesn’t generate visibility-related notifications for windows. Window visibility changes reflect changes to the window’s [`isHidden`](uiview/ishidden.md) property and reflect only the window’s visibility within the app.

The system posts this notification on the main actor.

## See Also

- [class let didBecomeHiddenNotification: NSNotification.Name](uiwindow/didbecomehiddennotification.md)
  A notification that posts when a window becomes hidden.
- [class let didBecomeKeyNotification: NSNotification.Name](uiwindow/didbecomekeynotification.md)
  A notification that posts whenever a window becomes the key window.
- [class let didResignKeyNotification: NSNotification.Name](uiwindow/didresignkeynotification.md)
  A notification that posts whenever a window resigns its status as main window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/didbecomevisiblenotification)*