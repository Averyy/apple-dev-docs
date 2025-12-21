# iOSDeviceNeedsUnlockAfterRebootForReachability

**Framework**: Watch Connectivity  
**Kind**: property

A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }
```

#### Discussion

When the [`isReachable`](wcsession/isreachable.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), use this property to determine if the iPhone is unreachable because it needs to be unlocked first. A recently rebooted iPhone remains unreachable until the user unlocks it for the first time. Until the user unlocks the iPhone, the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). When the value is [`true`](https://developer.apple.com/documentation/Swift/true), you might display an alert from your Watch app asking the user to unlock the iPhone to continue. After the user unlocks the iPhone, the value of the property changes to [`false`](https://developer.apple.com/documentation/Swift/false).

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](wcsession/activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.

## See Also

- [var isPaired: Bool](wcsession/ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var isWatchAppInstalled: Bool](wcsession/iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isCompanionAppInstalled: Bool](wcsession/iscompanionappinstalled.md)
  A Boolean value indicating whether the companion has installed the app.
- [var isComplicationEnabled: Bool](wcsession/iscomplicationenabled.md)
  A Boolean value indicating whether the Watch app’s complication is in use on the currently paired and active Apple Watch.
- [var watchDirectoryURL: URL?](wcsession/watchdirectoryurl.md)
  A directory for storing information specific to the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/iosdeviceneedsunlockafterrebootforreachability)*