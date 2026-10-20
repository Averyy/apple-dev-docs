# iOSDeviceNeedsUnlockAfterRebootForReachability

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL iOSDeviceNeedsUnlockAfterRebootForReachability;
```

#### Discussion

When the [`isReachable`](./isreachable.md) property is [`false`](../../Swift/false.md), use this property to determine if the iPhone is unreachable because it needs to be unlocked first. A recently rebooted iPhone remains unreachable until the user unlocks it for the first time. Until the user unlocks the iPhone, the value of this property is [`true`](../../Swift/true.md). When the value is [`true`](../../Swift/true.md), you might display an alert from your Watch app asking the user to unlock the iPhone to continue. After the user unlocks the iPhone, the value of the property changes to [`false`](../../Swift/false.md).

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](./activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](../wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.

## See Also

### Getting the Paired Device Information
- [var isPaired: Bool](./ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var isWatchAppInstalled: Bool](./iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isCompanionAppInstalled: Bool](./iscompanionappinstalled.md)
  A Boolean value indicating whether the companion has installed the app.
- [var isComplicationEnabled: Bool](./iscomplicationenabled.md)
  A Boolean value indicating whether the Watch app’s complication is in use on the currently paired and active Apple Watch.
- [var watchDirectoryURL: URL?](./watchdirectoryurl.md)
  A directory for storing information specific to the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/iosdeviceneedsunlockafterrebootforreachability)*