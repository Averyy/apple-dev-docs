# userActivity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object encapsulating a user activity supported by this responder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSUserActivity * userActivity;
```

#### Discussion

By setting the [`userActivity`](./useractivity.md) property on a responder, the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object becomes managed by UIKit. User activities managed by UIKit are saved automatically at appropriate times. You can lazily add state data representing the user’s activity using the [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md) override. Multiple responders can share a single [`NSUserActivity`](../../Foundation/nsuseractivity.md) instance, in which case they all get an [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md) callback.

> **Note**:  Prior to invoking [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md) on all of the associated objects, the `userInfo` dictionary for the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object is cleared.

A responder object can set its [`userActivity`](./useractivity.md) property to `nil` if it no longer wants to participate. Any [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects that are managed by UIKit but which have no associated responders (or documents) are automatically invalidated.

## See Also

### Supporting user activities
- [func restoreUserActivityState(NSUserActivity)](./restoreuseractivitystate%28_%29.md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](./updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/useractivity)*