# watchDirectoryURL

**Framework**: Watchconnectivity  
**Kind**: property

A directory for storing information specific to the currently paired and active Apple Watch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
var watchDirectoryURL: URL? { get }
```

#### Discussion

You must activate the current session before accessing this URL. Use this directory to store preferences, files, and other data that is relevant to the specific instance of your Watch app running on the currently paired Apple Watch. If more than one Apple Watch is paired with the same iPhone, the URL in this directory changes when the active Apple Watch changes.

When the value in the [`activationState`](wcsession/activationstate.md) property is [`WCSessionActivationState.notActivated`](wcsessionactivationstate/notactivated.md), the URL in this directory is undefined and should not be used. When a session is active or inactive, the URL corresponds to the directory for the most recently paired Apple Watch. Even when the session becomes inactive, the URL remains valid so that you have time to update your data files before the final deactivation occurs.

If the user uninstalls your app or unpairs their Apple Watch, iOS deletes this directory and its contents. If there is no paired watch, the value of this property is `nil`.

## See Also

- [var isPaired: Bool](wcsession/ispaired.md)
  A Boolean indicating whether the current iPhone has a paired Apple Watch.
- [var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool](wcsession/iosdeviceneedsunlockafterrebootforreachability.md)
  A Boolean value indicating whether the paired iPhone must be in an unlocked state to be reachable.
- [var isWatchAppInstalled: Bool](wcsession/iswatchappinstalled.md)
  A Boolean value indicating whether the currently paired and active Apple Watch has installed the app.
- [var isCompanionAppInstalled: Bool](wcsession/iscompanionappinstalled.md)
  A Boolean value indicating whether the companion has installed the app.
- [var isComplicationEnabled: Bool](wcsession/iscomplicationenabled.md)
  A Boolean value indicating whether the Watch app’s complication is in use on the currently paired and active Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/watchdirectoryurl)*