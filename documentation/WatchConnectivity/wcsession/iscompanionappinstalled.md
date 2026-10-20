# isCompanionAppInstalled

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the companion has installed the app.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
var isCompanionAppInstalled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCompanionAppInstalled) BOOL companionAppInstalled;
```

#### Discussion

Use this property on independent watchOS apps to determine whether the paired iPhone has installed the app.

## See Also

### Getting the Paired Device Information
- [var isPaired: Bool](./ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool](./iosdeviceneedsunlockafterrebootforreachability.md)
  A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.
- [var isWatchAppInstalled: Bool](./iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isComplicationEnabled: Bool](./iscomplicationenabled.md)
  A Boolean value indicating whether the Watch app’s complication is in use on the currently paired and active Apple Watch.
- [var watchDirectoryURL: URL?](./watchdirectoryurl.md)
  A directory for storing information specific to the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/iscompanionappinstalled)*