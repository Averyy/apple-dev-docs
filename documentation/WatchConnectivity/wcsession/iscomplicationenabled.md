# isComplicationEnabled

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the Watch app’s complication is in use on the currently paired and active Apple Watch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
var isComplicationEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isComplicationEnabled) BOOL complicationEnabled;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the app’s complication is installed on the active clock face. When the value of this property is [`false`](../../Swift/false.md), calls to the [`transferCurrentComplicationUserInfo(_:)`](./transfercurrentcomplicationuserinfo%28_%29.md) method fail immediately.

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](./activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](../wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.

## See Also

### Getting the Paired Device Information
- [var isPaired: Bool](./ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool](./iosdeviceneedsunlockafterrebootforreachability.md)
  A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.
- [var isWatchAppInstalled: Bool](./iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isCompanionAppInstalled: Bool](./iscompanionappinstalled.md)
  A Boolean value indicating whether the companion has installed the app.
- [var watchDirectoryURL: URL?](./watchdirectoryurl.md)
  A directory for storing information specific to the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/iscomplicationenabled)*