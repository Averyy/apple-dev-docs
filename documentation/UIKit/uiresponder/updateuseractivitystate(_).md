# updateUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the state of the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func updateUserActivityState(_ activity: NSUserActivity)
```

```objc
- (void) updateUserActivityState:(NSUserActivity *) activity;
```

#### Discussion

Subclasses override this method to update the state of the given user activity. You should add state representing the user’s activity into the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object using its [`addUserInfoEntries(from:)`](../../Foundation/nsuseractivity/adduserinfoentries%28from%29.md) method. When the state is dirty, you should set the [`needsSave`](../../Foundation/nsuseractivity/needssave.md) property of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) to [`true`](../../Swift/true.md), and this method will be called at an appropriate time.

When an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object managed by UIKit is updated, an empty `userInfo` dictionary is given to the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object, and all of the objects associated with the [`NSUserActivity`](../../Foundation/nsuseractivity.md) are then sent an [`updateUserActivityState(_:)`](./updateuseractivitystate%28_%29.md) message.

## Parameters

- `activity`: The user activity to be updated.

## See Also

### Supporting user activities
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object encapsulating a user activity supported by this responder.
- [func restoreUserActivityState(NSUserActivity)](./restoreuseractivitystate%28_%29.md)
  Restores the state needed to continue the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/updateuseractivitystate(_:))*