# restoreUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Restores the state necessary to continue the specified user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

Implement this method to restore an object’s state using the specified user activity. The system calls this method on any objects passed to the restoration handler in [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:continue:restorationHandler:)). Your implementation should use the state data contained in the specified user activity’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary to restore the object.

## Parameters

- `userActivity`: The user activity to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuseractivityrestoring/restoreuseractivitystate(_:))*