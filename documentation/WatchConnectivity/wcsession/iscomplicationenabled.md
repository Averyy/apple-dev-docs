# isComplicationEnabled

**Framework**: Watchconnectivity  
**Kind**: property

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

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the app’s complication is installed on the active clock face. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), calls to the [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) method fail immediately.

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](wcsession/activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.

## See Also

- [var isPaired: Bool](wcsession/ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool](wcsession/iosdeviceneedsunlockafterrebootforreachability.md)
  A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.
- [var isWatchAppInstalled: Bool](wcsession/iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isCompanionAppInstalled: Bool](wcsession/iscompanionappinstalled.md)
  A Boolean value indicating whether the companion has installed the app.
- [var watchDirectoryURL: URL?](wcsession/watchdirectoryurl.md)
  A directory for storing information specific to the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/iscomplicationenabled)*