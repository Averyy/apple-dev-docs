# updateUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method

Updates the state of the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateUserActivityState(_ activity: NSUserActivity)
```

#### Discussion

Subclasses override this method to update the state of the given user activity. You should add state representing the user’s activity into the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object using its [`addUserInfoEntries(from:)`](https://developer.apple.com/documentation/Foundation/NSUserActivity/addUserInfoEntries(from:)) method. When the state is dirty, you should set the [`needsSave`](https://developer.apple.com/documentation/Foundation/NSUserActivity/needsSave) property of the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) to [`true`](https://developer.apple.com/documentation/swift/true), and this method will be called at an appropriate time.

When an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object managed by UIKit is updated, an empty `userInfo` dictionary is given to the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object, and all of the objects associated with the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) are then sent an [`updateUserActivityState(_:)`](uiresponder/updateuseractivitystate(_:).md) message.

## Parameters

- `activity`: The user activity to be updated.

## See Also

- [var userActivity: NSUserActivity?](uiresponder/useractivity.md)
  An object encapsulating a user activity supported by this responder.
- [func restoreUserActivityState(NSUserActivity)](uiresponder/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/updateuseractivitystate(_:))*