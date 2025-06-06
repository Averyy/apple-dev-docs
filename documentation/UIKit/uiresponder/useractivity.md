# userActivity

**Framework**: Uikit  
**Kind**: property

An object encapsulating a user activity supported by this responder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var userActivity: NSUserActivity? { get set }
```

#### Discussion

By setting the [`userActivity`](uiresponder/useractivity.md) property on a responder, the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object becomes managed by UIKit. User activities managed by UIKit are saved automatically at appropriate times. You can lazily add state data representing the user’s activity using the [`updateUserActivityState(_:)`](uiresponder/updateuseractivitystate(_:).md) override. Multiple responders can share a single [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) instance, in which case they all get an [`updateUserActivityState(_:)`](uiresponder/updateuseractivitystate(_:).md) callback.

> **Note**:  Prior to invoking [`updateUserActivityState(_:)`](uiresponder/updateuseractivitystate(_:).md) on all of the associated objects, the `userInfo` dictionary for the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object is cleared.

A responder object can set its [`userActivity`](uiresponder/useractivity.md) property to `nil` if it no longer wants to participate. Any [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects that are managed by UIKit but which have no associated responders (or documents) are automatically invalidated.

## See Also

- [func restoreUserActivityState(NSUserActivity)](uiresponder/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](uiresponder/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/useractivity)*