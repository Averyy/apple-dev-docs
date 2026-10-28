# restoreUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Restores the state necessary to continue the specified user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

```objc
- (void) restoreUserActivityState:(NSUserActivity *) userActivity;
```

## Discussion

Implement this method to restore an object’s state using the specified user activity. The system calls this method on any objects passed to the restoration handler in [`application(_:continue:restorationHandler:)`](../../AppKit/nsapplicationdelegate/application%28_,continue,restorationhandler%29.md). Your implementation should use the state data contained in the specified user activity’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary to restore the object.

## Parameters

- `userActivity`: The user activity to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuseractivityrestoring/restoreuseractivitystate(_:))*