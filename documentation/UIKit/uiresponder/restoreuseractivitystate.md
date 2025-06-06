# restoreUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method

Restores the state needed to continue the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func restoreUserActivityState(_ activity: NSUserActivity)
```

#### Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The system calls it on any objects passed to the restoration handler given to [`application(_:continue:restorationHandler:)`](uiapplicationdelegate/application(_:continue:restorationhandler:).md). The override should use the state data contained in the given user activity’s `userInfo` dictionary to restore the object.

You may also call this method directly if the app delegate chooses not to use the restoration handler.

## Parameters

- `activity`: The user activity to be continued.

## See Also

- [var userActivity: NSUserActivity?](uiresponder/useractivity.md)
  An object encapsulating a user activity supported by this responder.
- [func updateUserActivityState(NSUserActivity)](uiresponder/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/restoreuseractivitystate(_:))*